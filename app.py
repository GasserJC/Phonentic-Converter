import eng_to_ipa as ipa
import numpy as np

def FeatureOptimize( phrase ):
    #Convert to IPA
    phrase = ipa.convert(phrase)

    #Cut Phrase to a length of 100
    phrase = phrase[0:100]

    #convert to ascii values
    num_phrase = []
    for char in phrase:
        char = ord(char)
        num_phrase.append(char)

    #Zero Fill from the front
    #num_phrase = num_phrase.zfill(100)

    #There are 107 IPA characters

    #Return Feature Optimized Phrase
    return num_phrase

phrase = "I make elevating music you make elevator music"
print(phrase)
print("Feature Optimize . . .")
phrase = FeatureOptimize(phrase)
print(phrase)