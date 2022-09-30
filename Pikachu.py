"""
Created on Nov 3, 2015

@author: George S. Hugh
"""


def check(word):
    """ return String based on parameter word, a String """

    pikachu = ['pi', 'ka', 'chu']
    vowel_list = ['a', 'i', 'u']    
    print("==================================")
    print(word)
    syllable = []
    for letter in word:
        syllable.append(letter)
        if letter in vowel_list:
            print("".join(syllable))
            if "".join(syllable) not in pikachu:
                return "NO"
            syllable = []
    
    if len(syllable) > 0:
        if "".join(syllable) not in pikachu:
            return "NO"
    return "YES"
    # Iterate through word
    #    if (letter is in vowel list
    #        get syllable
    #        if (syllable not in syllable list)
    #           return("NO")
    # return("yes"))
