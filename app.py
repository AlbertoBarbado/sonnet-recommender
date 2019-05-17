# -*- coding: utf-8 -*-
"""
@author: Alberto Barbado González
@mail: alberto.barbado.gonzalez@gmail.com

"""

from flask import Flask, render_template, redirect, url_for, request
from program.query_web import embedding_query_stanza
from program.data_features import (enrich_affective_df, docs2dict, obtain_bert_embeddings, 
                                   bert_embedding_composition_iter, word2vec_embedding_composition,
                                   feature_adding_affective)
            
app = Flask(__name__)  
    
@app.route('/')
def home():
   return None

@app.route('/result',methods = ['POST', 'GET'])
def result_sonnet():
   if request.method == 'GET':
      result = request.get_json()
      
      print("Variables introduced: {0}, {1}, {2}".format(
            result['composition_type'], result['metric'], result['log']))
      print("query_text introduced", result['query_text']) # results passes the input param as a dict
      sonnet = embedding_query_stanza(result['query_text'], composition_type=result['composition_type'], metric=result['metric'], user_filter=False, log=bool(result['log']))
      print("Sonnet: ")
      print(sonnet)
      return str(sonnet)
  

@app.route('/create_corpus',methods = ['POST', 'GET'])
def create_corpus():
    if request.method == 'POST':
        
        # Enrich affective df's with ngrams
        enrich_affective_df()
        # Obtain dict with all the sonnets and their affective features
        docs2dict()
        # Obtain BERT embeddings for all the words
        obtain_bert_embeddings(type_embedding="whole_text", generate_new=True)
        # Obtain composition embeddings [BERT, JOINT]
        bert_embedding_composition_iter(type_embedding="whole_text", composition_type="joint")
        # Obtain composition embeddings [BERT, SUM]
        bert_embedding_composition_iter(type_embedding="whole_text", composition_type="sum")
        # Obtain composition embeddings [W2V, JOINT]
        word2vec_embedding_composition(composition_type="joint")
        # Obtain composition embeddings [W2V, SUM]
        word2vec_embedding_composition(composition_type="sum")
        

@app.route('/create_ontology',methods = ['POST', 'GET'])
def create_ontology():
    if request.method == 'POST':
        # Modify XML TEI's adding affective values within that structure
        feature_adding_affective()
  

if __name__ == "__main__":
    app.run(debug=True)
