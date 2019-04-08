import requests
import json
from flask import Flask, jsonify, request
from pprint import pprint as pp
# NLP related
import MeCab
from sklearn.externals import joblib
from gensim.models import word2vec

app = Flask(__name__)

DEFAULT_LANGUAGE = 'jp'

"""
API Route Definitions
"""
@app.route("/mecab")
def search_foods():
	# Parameters
	sentence = request.args.get('sentence', '')
	language = request.args.get('language', '')
	option = request.args.get('option', '')

	# Parameter settings 
	if not language:
		language = DEFAULT_LANGUAGE

	# Run Mecab
	m = MeCab.Tagger ("mecabrc")
	tokenized_sentence = m.parse(sentence)

	return jsonify(tokenized_sentence)


@app.route("/")
def root():
	msg = {
		"msg": "This is test mecab api"
	}
	return json.dumps(msg)


"""
Functions
"""
def sample_function(sample_id):
	"""
	Search Solr for a keyword.
	"""
	# TODO
	return None


if __name__ == "__main__":
    # Only for debugging while developing
    # app.run(host='0.0.0.0', debug=True, port=80)
    app.run(host='0.0.0.0', debug=True)

