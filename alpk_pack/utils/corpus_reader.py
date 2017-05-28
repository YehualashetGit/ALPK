import os
import alpk_pack

amharic_character_set = "corpus/amharic_character_set.csv"
amh_vowels = ['አ', 'ኡ', 'ኢ', 'አ', 'ኤ', 'እ', 'ኦ']

def get_char_set():
	amh_char_set = alpk_pack.pd.read_csv(amharic_character_set, names=[1, 2, 3, 4, 5, 6, 7])
	return amh_char_set
	
def __normalize_vec(letter):
	amh_char_set = get_char_set()
	
	columns = amh_char_set.columns
	
	for col_name in columns:
		if letter in amh_char_set[col_name].values:
			return amh_char_set.iloc[amh_char_set.loc[amh_char_set[col_name] == letter].index.values[0], 6] + amh_vowels[col_name - 1]
	return None
	
def word_normalize(word):
	word_array = alpk_pack.np.array(list(word))
	vectorized_normalize = alpk_pack.np.vectorize(__normalize_vec)
	return list(vectorized_normalize(word_array))
