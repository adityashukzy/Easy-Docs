from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.text_rank import TextRankSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

LANGUAGE = "english"

def summarize_url(url, sentences_count = 10):
	'''
	Generate summary from provided url
	'''
	parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
	stemmer = Stemmer(LANGUAGE)

	summarizer = Summarizer(stemmer)
	summarizer.stop_words = get_stop_words(LANGUAGE)

	summary = []
	for sentence in summarizer(parser.document, sentences_count):
		summary.append(str(sentence))
	
	summary = " ".join(summary)
	return summary

def summarize_doc(text, sentences_count):
	'''
	Generate summary from provided string of text
	'''
	parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
	stemmer = Stemmer(LANGUAGE)

	summarizer = Summarizer(stemmer)
	summarizer.stop_words = get_stop_words(LANGUAGE)

	summary = []
	for sentence in summarizer(parser.document, sentences_count):
		summary.append(str(sentence))
	
	summary = " ".join(summary)
	return summary

if __name__ == "__main__":
	summarize_url()
