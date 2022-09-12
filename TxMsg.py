'''
Created on Feb 1, 2012

@author: hughgs
'''

def all_vowels(string):
    
    vows = string.count("a") + string.count("e") + string.count("i") \
                + string.count("o") + string.count("u")
    
    return(vows == len(string))

def getMessage(original):

    tx_msg = ""
#    print original

    words = original.split(" ")
    for string in words:
        if (not all_vowels(string)):
            tx_word = ""
            string = string.replace("a"," ")
            string = string.replace("e"," ")
            string = string.replace("i"," ")
            string = string.replace("o"," ")
            string = string.replace("u"," ")
            cons = string.split(" ")
            for sub in cons:
                if (sub != ""):
                    tx_word = tx_word + sub[0]
        else:
            tx_word = string

        tx_msg = tx_msg + " " + tx_word
        
    return(tx_msg[1:])