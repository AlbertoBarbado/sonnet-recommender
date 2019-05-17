# Sonnet Recommender System

This is the main API used in the poetry assistant SAREK (https://github.com/AlbertoBarbado/sarek-web and https://github.com/AlbertoBarbado/sarek-desktop)
That API can be integrated with other platforms using it's different endpoints.

The purpose of the system is to offer an IR engine that can process spanish poetry (sonnets) using different NLP techniques (such as word embeddings and sentence composition) and that can receive an input query and then recommend the sonnet from among the corpus that it's more similar to that query from a semantic point of view.
For the embeddings the system uses BERT (https://github.com/google-research/bert) and word2vec (https://www.kaggle.com/rtatman/pretrained-word-vectors-for-spanish/downloads/pretrained-word-vectors-for-spanish.zip/1)


## 1. Requirements
* Python 3.6.1 
* Pip

## 2. Setup
After cloning/downloading the repo install the requirements
```
$ pip install -r requirements.txt
```

After that, install Spacy language model with the following command

```
$ python -m spacy download es_core_news_sm
```

Then download the datasets needed for the application from:
```
https://unedo365-my.sharepoint.com/:f:/g/personal/abarbado5_alumno_uned_es/Eh6rYEkgXRdIsKgXjvv5NXoBFHMq1HNkayFHmGk_RY-_zg?e=PaZPoG
```
And move all files to the **datasets** folder before executing the application.

Then execute the app.py file

```
$ python app.py
```

After that the app will be running on localhost:5000 and it can be accessed from two endpoints:

* [POST] /create_corpus | This endpoint doesn't need input arguments; it will lead to process the necessary input data to obtain the files already available in the OneDrive folder aforementioned [NO NEED TO USED IT]
* [GET] /results | This endpoint receives a query and other parameters to perform the IR task and retreive the most suitable sonnet. By default the word embedding technique in this case will always be BERT. The arguments in the body of the request should be:

|parameter|values|description|
|---|---|---|
|query_text||Input query sent|
|composition_type|"joint" or "sum"||
|metric|"cosine" or "icm"||
|log|"True" or "False"|To indicate if the user wants to see the scoring obtained for the last top of retreived sonnets.|

To modify the DISCO ontology, you can access the following endpoint:
* [POST] /create_ontology

But to do that YOU MUST PREVIOUSLY DO the following task:
- Download all the 'per-sonnet' folders from DISCO (TEI XMLs) and copy all of their content's within a unique per-sonnet folder within the /poems folder. Due to this, the folders to download will be:
	- https://github.com/pruizf/disco/tree/master/tei/15th-17th/per-sonnet
	- https://github.com/pruizf/disco/tree/master/tei/18th/per-sonnet
	- https://github.com/pruizf/disco/tree/master/tei/19th/per-sonnet
- The zip folder per-sonnet available right now within /poems already contains the original files from DISCO with the affective values added.
	


## 3. Additional considerations
* The machine used to run the program shoudl have at least 4 gb of RAM and 2 cores
* As it's said, it takes a while for the program to start (around 2-5 min) 
