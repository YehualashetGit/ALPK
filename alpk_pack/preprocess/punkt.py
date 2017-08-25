

class tokenize:
    def __init__(self, text, tokenizer):
        self.__punkts = ['፠', '፡', '።', '፣', '፤', '፥', '፦', '፧', '፨', '?', '"', '!', ' ', '“', "::", ]
        self.__sent_delimiters = ['።', '፤', '፦', '፧', '?']
        #self.__word_delimiters = ['፠', '፡', '።', '፣', '፤', '፥', '፦', '፧', '?',' ']
        self.tokenizer = tokenizer
    def get_punkt_rules(self):
        return self.__punkts
    def sent_tokenize(self, text):
        sents = self.tokenizer.parse(self.__sent_delimiters)
        new_sents = []
        sentence = " "
        for i in range(len(sents)):
        	if (i % 2 == 0):
        		sentence = sents[i]
        	elif (i %2 !=0):
        		sentence += sents[i]
        		new_sents.append(sentence)
        return new_sents
    def word_tokenize(self, text):
        words = self.tokenizer.parse(self.__punkts)
        words = [word for word in words if word != ' ']
        return words

    #count words
    #count count sentences
