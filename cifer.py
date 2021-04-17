key1={'a': 'f', 'b': 'b', 'c': 'j', 'd': 'z', 'e': 'h', 'f': 'k', 'g': 's', 'h': 'x', 'i': 'l', 'j': 'd', 'k': 'o', 'l': 'a', 'm': 'm', 'n': 'r', 'o': 'y', 'p': 't', 'q': 'g', 'r': 'n', 's': 'q', 't': 'w', 'u': 'u', 'v': 'c', 'w': 'v', 'x': 'i', 'y': 'p', 'z': 'e'}
text1=("However, this gives the frequency of letters in English text, which is dominated by a relatively small number of common words . For word games, it is often the frequency of letters in English vocabulary, regardless of word frequency, which is of more interest. The following is a result of an analysis of the letters occurring in the words listed in the main entries of the Concise Oxford Dictionary (9th edition, 1995) and came up with the following table:")

import string
lowchars=string.ascii_lowercase
def charcount(text):
# this function gets a text and returns a dictionary sorting the most frequent characters
    text=text.lower()
    chardict={}
    for char in text:
        if char in lowchars:
            chardict[char]= chardict.get(char,0) + 1
    return dict(sorted(chardict.items(), key=lambda x: x[1], reverse=True))

def encodestr(keydict,text):
    #this function gets a dictionary and a string and returns the encoded string by the key - in the dictionary the keys are the clear text chars and the value is the encrypted
    pass

dict1=charcount("However, this gives the frequency of letters in English text, which is dominated by a relatively small number of common words . For word games, it is often the frequency of letters in English vocabulary, regardless of word frequency, which is of more interest. The following is a result of an analysis of the letters occurring in the words listed in the main entries of the Concise Oxford Dictionary (9th edition, 1995) and came up with the following table:	")
print(dict1)


