# -*- coding: utf-8 -*-
"""
@author: Alberto Barbado González
@mail: alberto.barbado.gonzalez@gmail.com
"""

import xmltodict
import re
import os
from nltk.corpus import stopwords
from nltk import ngrams
import pandas as pd
import numpy as np
from gensim.models.keyedvectors import KeyedVectors
import spacy
nlp = spacy.load('es')

from config import (PATH_POEMS, PATH, WORD_COL, NAME1, NAME2, 
                    NAME3, NAME4, WORD_EMBEDDING_FILE, FILE_NAME_DCT_RESULTS,
                    DOCS_NAME_DCT, TYPE_EMBEDDING, FILE_NAME_VOCAB)
from tools import get_files, file_presistance
from numpy.random import randint
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from data_features import word_grams, word_preprocessing, joint_function

import torch
from pytorch_pretrained_bert import BertTokenizer, BertModel
from bert_utils import read_text, convert_examples_to_features
from data_features import text2bert_embedding
from sklearn.metrics.pairwise import cosine_similarity
from numpy.linalg import norm
from bert_embedding import BertEmbedding


#### Load relevant info (fasttext)
try:
    DF_WORD_EMBEDDING = file_presistance(PATH + "/" + FILE_NAME_DCT_RESULTS + ".p", "generic", None, "load")
    LIST_WORDS_EMBEDDING = list(file_presistance(PATH + "/" + FILE_NAME_VOCAB + ".p", "generic", None, "load").keys())
    DCT_SONNETS = file_presistance(PATH + "/" + DOCS_NAME_DCT + ".p", "generic", None, "load")
except:
    e = "Vocabulary not trained yet! Use 'data_feature' functions first"
    print(e)
    raise Exception(e)
#DCT_RESULTS = file_presistance("datasets/dct_results.p", "generic", None, "load")

#########
### Load Bert models
#########
    
layers = "-1"
layer_indexes = [int(x) for x in layers.split(",")]

# Define tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased', do_lower_case=False)
local_rank = -1
batch_size = 10

# Train model
model = BertModel.from_pretrained('bert-base-multilingual-cased')
device = torch.device("cpu")
model.to(device)


#########
### Load whole text embeddings
#########

### Joint
# Load
DCT_COMPOSITION_EMBEDDING_JOINT = file_presistance(PATH + '/' + 'dct_composition_embeddings_{0}_{1}.p'.format("joint", TYPE_EMBEDDING), "generic", None, "load")
DCT_COMPOSITION_EMBEDDING_JOINT_STANZA = file_presistance(PATH + '/' + 'dct_composition_embeddings_stanza_{0}_{1}.p'.format("joint", TYPE_EMBEDDING), "generic", None, "load")

# Stanzas - sonnet mapping
df_mapping = pd.DataFrame()
df_mapping['stanzas'] = DCT_COMPOSITION_EMBEDDING_JOINT_STANZA['joint']['stanza']
df_mapping['sonnet'] = DCT_COMPOSITION_EMBEDDING_JOINT_STANZA['joint'].index
del DCT_COMPOSITION_EMBEDDING_JOINT_STANZA['joint']['stanza']

### Sum
DCT_COMPOSITION_EMBEDDING_SUM_STANZA = file_presistance(PATH + '/' + 'dct_composition_embeddings_stanza_{0}_{1}.p'.format("sum", TYPE_EMBEDDING), "generic", None, "load")
del DCT_COMPOSITION_EMBEDDING_SUM_STANZA['sum']['stanza']


###############################################################################

#########
### Del poems that are not sonnets
#########

try:
    del DCT_SONNETS[2543]
    DCT_COMPOSITION_EMBEDDING_JOINT_STANZA['joint'].drop(2543, axis=0, inplace=True)
    DCT_COMPOSITION_EMBEDDING_JOINT['joint'].drop(2543, axis=0, inplace=True)
    DCT_COMPOSITION_EMBEDDING_SUM_STANZA['sum'].drop(2543, axis=0, inplace=True)
    
except:
    pass

try:
    del DCT_SONNETS[300]
    DCT_COMPOSITION_EMBEDDING_JOINT_STANZA['joint'].drop(300, axis=0, inplace=True)
    DCT_COMPOSITION_EMBEDDING_JOINT['joint'].drop(300, axis=0, inplace=True)
    DCT_COMPOSITION_EMBEDDING_SUM_STANZA['sum'].drop(300, axis=0, inplace=True)
except:
    pass

###############################################################################




#### Example
query_text = "La autoridad está bajo una alta presión en el alma"
query_text = "Me encantaría poder leer una poesía que trate de fantasía, con algo de acción y que me transporte a un mundo único"

def text2features(query_text):
    """
    # TODO
    Function to obtain the df with the embedding metrics corresponding to a particular
    query text.
    
    It tries to check first if the words of the query are present in the df matrix and in case they are
    not it tries it with different ngrams. In case the word or ngrams are not present, it masks the word
    with a generic UNK that corresponds to a [0,..0] feature array.
    
    """
    
    # Word preprocessing
    _ , words_lem, _, _ = word_preprocessing(query_text)
    # Generate ngrams for words
    word2idx = [k for k in range(len(words_lem))]
    dct_words = {}
    for index, w in zip(word2idx, words_lem):
        words_ngrams = word_grams(w, 1, len(w)+1)
        words_ngrams = words_ngrams[::-1] # reverse list to start later by complete word
        for w_n in words_ngrams:
            if w_n in LIST_WORDS_EMBEDDING:
                dct_words[index] = w_n
                break
            else:
#                dct_words[index] = 'UNK'
                continue
                
    # dict to pandas and join to main df to obtain features
    df_features = pd.DataFrame({'position':list(dct_words.keys()), 'word':list(dct_words.values())}).set_index('word')
    df_features = df_features.join(DF_WORD_EMBEDDING, how='left')
    
    return df_features


def tfidf_query_similairty(query_text, strict=False, return_list=True):
    """
    # TODO
    
    Receive a query and retrieves the most similar sonnet using tf-idf; it builds 
    the tf-idf matrix using the stored documents and the new query and then it checks
    the feature word most similar to the query (last row used) and retrieves the index
    corresponding to that document.
    
    This tfidf function considers both the lemmatized words and the possible ngrams
    as well up to 2grams.
    
    """
    
    # Obtain documents
    documents = [f['ngrams2str'] for f in DCT_SONNETS.values()]
    
    # Obtain ngrams of new text
    _, _, query_words_ngrams, _ = word_preprocessing(query_text)
    text_ngrams = ""
    for w in query_words_ngrams:
        text_ngrams += w
        text_ngrams += " "
    
    # Add retrieval query as a new document
    documents.append(text_ngrams)
    
    # docs2tfidf
    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(documents)
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    
    X_sim = (X_train_tfidf * X_train_tfidf.T).A
#    X_dense = pd.DataFrame(X_train_tfidf.todense())
    words_used = count_vect.get_feature_names()
    
    # Last row corresponds to query similarity to docs
    results =  pd.DataFrame(X_sim[:,-1])
    results.drop(results.tail(1).index, inplace=True) # drop autosimilarity
    
    
    if not return_list:
        # If there's no similarity to any doc, give a random one
        if results[0].max()==results[0].min():
            results = randint(low=0, high=len(results))
        else:
            results = results[0].values.argmax()
        doc_sonnet = DCT_SONNETS[results]
        
    else:
        # By default give all the dict as it is
        doc_sonnet = DCT_SONNETS
        
        if results[0].max() != results[0].min():
            # Preselect only docs with maximum TF-IDF
#            max_value = results[0].max()
#            results = results[results[0]==max_value]
#            mean_value = results[0].mean()
#            results = results[results[0]>=mean_value]
            if strict:
                intermedian_value = results[0].max()
            else:
                intermedian_value = (2*results[0].max() + results[0].mean())/3
            results = results[results[0]>=intermedian_value]
#            results = results.sort_values(by=0, ascending=False)
            doc_sonnet = {key:doc_sonnet[key] for key in list(results.index)} # no need to sort anymore; use filtered dict
    
    return doc_sonnet, words_used



def icm(v1, v2):
    """
    # TODO
    """
#    v1_norm = norm(np.column_stack((v1.values,v1.values)))
#    v2_norm = norm(np.column_stack((v2.values,v2.values)))
    c = 1.4
    c1 = 1
    c2 = 1
    
    v1_norm = norm(v1)
    v2_norm = norm(v2)
    v1_v2 = v1_norm*v2_norm*cosine_similarity(v1,v2)[0][0]
    result = c*v1_v2 + (c1 - c)*v1_norm**2 + (c2 - c)*v2_norm**2
    return result
    



def embedding_query(query_text, composition_type, metric, use_prefilter=True, log=False):
    """
    # TODO
    Doc retrieval using BERT embedding against an input text query
    
    """
    
    if composition_type=="sum":
        DCT_COMPOSITION_EMBEDDING = DCT_COMPOSITION_EMBEDDING_SUM
        composition_type  = "sum"
    elif composition_type=="joint":
        DCT_COMPOSITION_EMBEDDING = DCT_COMPOSITION_EMBEDDING_JOINT
        composition_type = "joint"
    else:
        NotImplementedError("Composition type used is not recognised")
    
    # Process the query text if needed
    # Transfor str to str withoupt uppercases, stopwords and lemmatized
    if TYPE_EMBEDDING == "words_lem_nonstopwords":
        _, list_words, _, _ = word_preprocessing(query_text)
        s = ''
        for w in list_words:
            s += ' '
            s += w
        query_text = s
    
        # Embedding for text query
        examples = read_text(query_text, multiple_lines=False)
        output_json_query = text2bert_embedding(model, examples, tokenizer, local_rank, batch_size, device, layer_indexes)
        df_features = pd.DataFrame([x['layers'][0]['values'] for x in output_json_query[0]['features']])
    
    elif TYPE_EMBEDDING == "fasttext":
        df_features = text2features(query_text)
        df_features = df_features.rename(columns={'position':'index'})
        df_features = df_features.set_index("index")
    else:
        raise NotImplementedError("Embedding defined in config is not recognised")
    
    # Sum of vectors
    if composition_type=="sum":
        vector_compos_query = pd.DataFrame(df_features.sum()).T
        dct_embedding_all = DCT_COMPOSITION_EMBEDDING[composition_type]
    elif composition_type=="mean":
        vector_compos_query = pd.DataFrame(df_features.mean()).T
        dct_embedding_all = DCT_COMPOSITION_EMBEDDING[composition_type]
    elif composition_type=="joint":
        vector_compos_query = pd.DataFrame(df_features)
        # Inverse order (RL_SEQ)
        vector_compos_query.reset_index(inplace=True)
        del vector_compos_query['index']
        vector_compos_query.sort_index(ascending=False, inplace=True)
        key_max = vector_compos_query.index.max()
        v_follow = [0]*vector_compos_query.shape[1]
        # Iterate per word
        for key, vi in vector_compos_query.iterrows():
            # First vector is not joint to anyone yet
            if key == key_max:
                v_follow = vi
            else:
                v_follow = joint_function(v_follow,vi)
        vector_compos_query = pd.DataFrame(v_follow).T
        dct_embedding_all = DCT_COMPOSITION_EMBEDDING[composition_type]
    else:
        raise NotImplementedError("Composition type not included. Try sum, mean or joint")
    
    # If condition pre-filter with TF-IDF
    list_prefilter = list(DCT_SONNETS.keys())
    if use_prefilter:
        doc_aux, _ = tfidf_query_similairty(query_text, strict=False, return_list=True)
        list_prefilter = list(doc_aux.keys())
        dct_embedding_all = dct_embedding_all[dct_embedding_all.index.isin(list_prefilter)]
    
    metric_sim = -1
    key_final = -np.inf
    
    for key, sonnet in DCT_SONNETS.items():
        if key not in list_prefilter:
            continue
        vector_compos_sonnet = pd.DataFrame(dct_embedding_all.loc[key]).T
        
        # Compute metric
        if metric == "cosine":
            metric_sim_aux = cosine_similarity(vector_compos_query, vector_compos_sonnet)[0][0]
        elif metric == "icm":
            metric_sim_aux = np.abs(icm(v1=vector_compos_sonnet, v2=vector_compos_query))
        # Compare metrics
        if metric_sim_aux >= metric_sim:
            metric_sim = metric_sim_aux
            key_final = key
            if log:
                print("Best {0} metric until now {1} for doc nº {2}".format(metric, np.round(metric_sim_aux,4), key))
                print()
                print(DCT_SONNETS[key_final]['text'])
                print("*"*50)
                print("")
                
    
    # Check that sonnet is not more than 4 paragraphs (sum case)
    if composition_type=="sum":
        aux_text = nlp(DCT_SONNETS[key_final]['text'])
        text=''
        k = 0
        list_aux = list(aux_text.sents)
        if len(list_aux) > 4:
            for r in list_aux:
                text += r.text
                if k >1: break
                k +=1
            DCT_SONNETS[key_final]['text'] = text
        
    
    return DCT_SONNETS[key_final]


def embedding_query_stanza(query_text, composition_type, metric, use_prefilter=True, log=False):
    """
    # TODO
    Doc retrieval using BERT embedding against an input text query
    
    """
    
    if composition_type=="sum":
        DCT_COMPOSITION_EMBEDDING = DCT_COMPOSITION_EMBEDDING_SUM_STANZA
        composition_type = "sum"
    elif composition_type=="joint":
        DCT_COMPOSITION_EMBEDDING = DCT_COMPOSITION_EMBEDDING_JOINT_STANZA
        composition_type = "joint"
    else:
        NotImplementedError("Composition type used is not recognised")
    
    # Process the query text if needed
    # Transfor str to str withoupt uppercases, stopwords and lemmatized
    if TYPE_EMBEDDING == "words_lem_nonstopwords":
        _, list_words, _, _ = word_preprocessing(query_text)
        s = ''
        for w in list_words:
            s += ' '
            s += w
        query_text = s
    
        # Embedding for text query
#        examples = read_text(query_text, multiple_lines=False)
#        output_json_query = text2bert_embedding(model, examples, tokenizer, local_rank, batch_size, device, layer_indexes)
#        df_features = pd.DataFrame([x['layers'][0]['values'] for x in output_json_query[0]['features']])
        
        # Using BERT embedding library
        bert_embedding = BertEmbedding()
        result = bert_embedding(list_words)
        df_features = pd.DataFrame([x[1][0] for x in result])
    
    elif TYPE_EMBEDDING == "fasttext":
        NotImplementedError("Composition type used is not recognised")
    else:
        raise NotImplementedError("Embedding defined in config is not recognised")
    
    # Sum of vectors
    if composition_type=="sum":
        vector_compos_query = pd.DataFrame(df_features.sum()).T
        dct_embedding_all = DCT_COMPOSITION_EMBEDDING[composition_type]
    elif composition_type=="mean":
        raise NotImplementedError("Embedding defined in config is not recognised")
    elif composition_type=="joint":
        vector_compos_query = pd.DataFrame(df_features)
        # Inverse order (RL_SEQ)
        vector_compos_query.reset_index(inplace=True)
        del vector_compos_query['index']
        vector_compos_query.sort_index(ascending=False, inplace=True)
        key_max = vector_compos_query.index.max()
        v_follow = [0]*vector_compos_query.shape[1]
        # Iterate per word
        for key, vi in vector_compos_query.iterrows():
            # First vector is not joint to anyone yet
            if key == key_max:
                v_follow = vi
            else:
                v_follow = joint_function(v_follow,vi)
        vector_compos_query = pd.DataFrame(v_follow).T
        dct_embedding_all = DCT_COMPOSITION_EMBEDDING[composition_type]
    else:
        raise NotImplementedError("Composition type not included. Try sum, mean or joint")
    
    # If condition pre-filter with TF-IDF
    list_prefilter = list(DCT_SONNETS.keys())
    if use_prefilter:
        doc_aux, _ = tfidf_query_similairty(query_text, strict=False, return_list=True)
        list_prefilter = list(doc_aux.keys())
        dct_embedding_all = dct_embedding_all[dct_embedding_all.index.isin(list_prefilter)]
    
    metric_sim = -np.inf
    key_final = -np.inf

    for key, sonnet in DCT_SONNETS.items():
        if key not in list_prefilter:
            continue
        
        vector_compos_sonnet = pd.DataFrame(dct_embedding_all.loc[key])
        
        for _, vector_compos_stanza in vector_compos_sonnet.iterrows():
            vector_compos_stanza = pd.DataFrame(vector_compos_stanza).T

            # Compute metric
            if metric == "cosine":
                metric_sim_aux = cosine_similarity(vector_compos_query, vector_compos_stanza)[0][0]
            elif metric == "icm":
                metric_sim_aux = icm(v1=vector_compos_stanza, v2=vector_compos_query)
            
#            print(metric_sim_aux)
            # Compare metrics
            if metric_sim_aux >= metric_sim:
                metric_sim = metric_sim_aux
                key_final = key
                if log:
                    print("Best {0} metric until now {1} for doc nº {2}".format(metric, np.round(metric_sim_aux,4), key))
                    print()
                    print(DCT_SONNETS[key_final]['text'])
                    print("*"*50)
                    print("")
        
    return DCT_SONNETS[key_final]
    
 