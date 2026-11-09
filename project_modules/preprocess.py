import string
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
nltk.download("stopwords")

stemmer = PorterStemmer()
stop = stopwords.words('english')

def preprocess(text):
    return text.translate(str.maketrans("","", string.punctuation)).lower()

def tokenize(text):
    return [ stemmer.stem(word) for word in text.split() if word not in stop]
