from alpk_pack.preprocess.to_CV import to_CV
from alpk_pack.preprocess import Regexpp
from alpk_pack.preprocess import punkt



def sent_tokenize(text):
    regex_tokenizer = Regexpp.Regex(text)
    punkt_sent_tokenizer = punkt.tokenize(text, regex_tokenizer)
    return punkt_sent_tokenizer.sent_tokenize(text)



def word_tokenize(text):
    regex_tokenizer = Regexpp.Regex(text)
    sents = sent_tokenize(text)
    punkt_word_tokenizer = punkt.tokenize(text, regex_tokenizer)
    words = punkt_word_tokenizer.word_tokenize(text)
    return words
    
def normalize(text):
	pass
