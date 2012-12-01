#!/usr/bin/env python
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
        	n = i % len(index_key)
		cypherIndex.append((index_plaintext[i]+index_key[n]) % len(alphabet))
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
	return encryptedMessage

# DECRPYTION
	
def decrypt(plaintext,key):
	index_plaintext = indexValuesOfPlaintext(plaintext)
	index_key = indexValuesOfPlaintext(key)
	decypherIndex = decypherNumbers(index_plaintext,index_key)
	decryptedMessage = "".join(cypherText(decypherIndex))
	return decryptedMessage
	
def decypherNumbers(index_plaintext,index_key):
	decypherIndex = []
	for i in range(len(index_plaintext)):
		n = i % len(index_key)
		decypherIndex.append((index_plaintext[i]-index_key[n]) % len(alphabet))
	return decypherIndex

def main():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
            help="write report to FILE", metavar="FILE")
    parser.add_option("-q", "--quiet",
            action="store_false", dest="verbose", default=True,
    help="don't print status messages to stdout")

    (options, args) = parser.parse_args()

if __name__ == "__main__":
    main()