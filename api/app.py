from flask import Flask, jsonify, request
from summarization.summarize import summarize_url

app = Flask(__name__)

@app.route('/api')
def home():
	return jsonify({"test message": "This API works lol!"})

@app.route('/api/summarize-url')
def summarize():
	query_parameters = request.args
	url = query_parameters.get("url")
	sentences_count = query_parameters.get("sentences")

	summary = summarize_url(url, sentences_count)
	return jsonify({"url_provided": url, "sentences": sentences_count, "summary": summary})

if __name__ == "__main__":
	app.run(debug=True)