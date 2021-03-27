import numpy as np
import tensorflow as tf
from tensorflow import keras
import nltk
nltk.download('wordnet')
import json
from nltk.stem import WordNetLemmatizer
import random
import pickle


def load_chatbot(path):
	model = keras.models.load_model(path)
	return model

def input_bag(sen,words):
    bag=[0]*len(words)
    wrds=nltk.word_tokenize(sen)
    wrds=[lemm.lemmatize(w.lower()) for w in wrds]

    for s in wrds:
        for i,j in enumerate(words):
            if j==s:
                bag[i]=1
    return (np.array(bag))

def ezpz_bot(model, textInput):
	with open('dependencies/ezpz_intents.json') as file:
		data = json.load(file, strict=False)

	words = pickle.load(open('dependencies/words_ed.pkl','rb'))
	labels = pickle.load(open('dependencies/labels_ed.pkl','rb'))

	while True:
		if textInput.lower() == 'exit':
			return "😴"

		bag = input_bag(textInput, words)
		result = model.predict(np.array([bag]))[0]
		pred_index = np.argmax(result)

		tag = labels[pred_index]
		#st.write(tag)

		for val in data['intents']:
			if val['tag'] == tag:
				resp = val['responses']
				break

		return (random.choice(resp),tag)
