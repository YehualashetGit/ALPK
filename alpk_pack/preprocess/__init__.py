from alpk_pack.preprocess.to_CV import to_CV
from alpk_pack.preprocess import Regexpp
from alpk_pack.preprocess import punkt

normalize_rules_dir = "corpus/replace_rules/"


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
    
def normalize(text, removeEnglish = True, similarizePunctuations = True, similarizePhonetics = True, noAbbreviations = True):
    """
    Normalize given text by removing english, similarizing the same phone to same character
    and changing abbreviations to their normal form
    """
    if (removeEnglish):
        englishRemovalDict = getRegexDict(normalize_rules_dir + "english_removal.json")
        text = replace(text, englishRemovalDict)

    if (similarizePunctuations):
        punktSimilarizationDict = getRegexDict(normalize_rules_dir + "punkt_character_similarization.json")
        text = replace(text, punktSimilarizationDict)
    
    if (similarizePhonetics):
        phoneSimilarizationDict = getRegexDict(normalize_rules_dir + "phone_character_similarization.json")
        text = replace(text, phoneSimilarizationDict)
    
    if(noAbbreviations):
        abbreviationsDict = getRegexDict(normalize_rules_dir + "abbreviations.json")
        text = replace(text, abbreviationsDict)

    return text
