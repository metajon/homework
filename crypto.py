import random
import string

# The alphabet in a list:
alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# Generate a key N chars long.
def generateKey(length):
	keyString = ''.join(random.choice(string.ascii_uppercase) for n in range(length))
	key = list(keyString)
	return key

def return_index(letter):
	return alphabet.index(letter) # +1

def enterPlaintext():
	plaintext = raw_input('Enter plaintext: ')
	plainTextList = list(plaintext)
	return plainTextList

def indexValuesOfPlaintext(pt_list):
	indexOfPlaintext = []
	for i in range(len(pt_list)):
		indexOfPlaintext.append(return_index(pt_list[i]))
	return indexOfPlaintext

def cypherNumbers(index_plaintext,index_key):
	cypherIndex = []
	for i in range(len(index_plaintext)):
		cypherIndex.append((index_plaintext[i]+index_key[i]) % len(alphabet))
	return cypherIndex

def cypherText(cypherIndex):
	cypher_text = []
	for i in range(len(cypherIndex)):
		cypher_text.append(alphabet[cypherIndex[i]])
	return cypher_text

def encrypt(plaintext,key):
	index_plaintext = indexValuesOfPlaintext(plaintext)
	index_key = indexValuesOfPlaintext(key)
	cypherIndex = cypherNumbers(index_plaintext,index_key)
	encryptedMessage = "".join(cypherText(cypherIndex))
	print encryptedMessage
	
# Sketch for the handling of keys smaller than the message:

# endlist=[]
# for i in range(len(longlist)):
# 	n = i % len(shortlist)
# 	endlist.append(longlist[i]+shortlist[n])



# Early testing code follows:

#key=["O","L","E","Z","J","W","A","I"]

#plaintext="THEBROWNFOX"

# pt_list = list(plaintext)
# for i in range(len(cyphertext)):
# 	print alphabet[cyphertext[i]]

# for i in range(len(pt_list)):
# 	return_index(pt_list[i])

# for i in range(len(key)):
# 	return_index(key[i])

