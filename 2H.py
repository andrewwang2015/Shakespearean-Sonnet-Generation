########################################
# CS/CNS/EE 155 2017
# Problem Set 5
#
# Author:       Andrew Kang
# Description:  Set 5
########################################

from HMM import unsupervised_HMM
from Utility import Utility
import re
import copy 

def unsupervised_learning(n_states, n_iters):
    '''
    Trains an HMM using supervised learning on the file 'ron.txt' and
    prints the results.

    Arguments:
        n_states:   Number of hidden states that the HMM should have.
    '''
    genres, genre_map, rhyming = Utility.load_shakespeare_hidden_stripped_poems()

    # Train the HMM.
    HMM = unsupervised_HMM(genres, n_states, n_iters)

    # Print the transition matrix.
    print("Transition Matrix:")
    print('#' * 70)
    for i in range(len(HMM.A)):
        print(''.join("{:<12.3e}".format(HMM.A[i][j]) for j in range(len(HMM.A[i]))))
    print('')
    print('')

    # Print the observation matrix. 
    print("Observation Matrix:  ")
    print('#' * 70)
    for i in range(len(HMM.O)):
        print(''.join("{:<12.3e}".format(HMM.O[i][j]) for j in range(len(HMM.O[i]))))
    print('')
    print('')
    
    return HMM, genre_map, rhyming

    
def syllables(word):
    '''
    This function counts number of syllables in a word
    '''
    
    count = 0
    vowels = 'aeiouy'
    word = word.lower().strip(".:;?!")
    if word[0] in vowels:
        count +=1
    for index in range(1,len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            count +=1
    if word.endswith('e'):
        count -= 1
    if word.endswith('le'):
        count+=1
    if count == 0:
        count +=1
    return count

def sylco(word) :
 
    word = word.lower()
 
    # exception_add are words that need extra syllables
    # exception_del are words that need less syllables
 
    exception_add = ['serious','crucial']
    exception_del = ['fortunately','unfortunately']
 
    co_one = ['cool','coach','coat','coal','count','coin','coarse','coup','coif','cook','coign','coiffe','coof','court']
    co_two = ['coapt','coed','coinci']
 
    pre_one = ['preach']
 
    syls = 0 #added syllable number
    disc = 0 #discarded syllable number
 
    #1) if letters < 3 : return 1
    if len(word) <= 3 :
        syls = 1
        return syls
 
    #2) if doesn't end with "ted" or "tes" or "ses" or "ied" or "ies", discard "es" and "ed" at the end.
    # if it has only 1 vowel or 1 set of consecutive vowels, discard. (like "speed", "fled" etc.)
 
    if word[-2:] == "es" or word[-2:] == "ed" :
        doubleAndtripple_1 = len(re.findall(r'[eaoui][eaoui]',word))
        if doubleAndtripple_1 > 1 or len(re.findall(r'[eaoui][^eaoui]',word)) > 1 :
            if word[-3:] == "ted" or word[-3:] == "tes" or word[-3:] == "ses" or word[-3:] == "ied" or word[-3:] == "ies" :
                pass
            else :
                disc+=1
 
    #3) discard trailing "e", except where ending is "le"  
 
    le_except = ['whole','mobile','pole','male','female','hale','pale','tale','sale','aisle','whale','while']
 
    if word[-1:] == "e" :
        if word[-2:] == "le" and word not in le_except :
            pass
 
        else :
            disc+=1
 
    #4) check if consecutive vowels exists, triplets or pairs, count them as one.
 
    doubleAndtripple = len(re.findall(r'[eaoui][eaoui]',word))
    tripple = len(re.findall(r'[eaoui][eaoui][eaoui]',word))
    disc+=doubleAndtripple + tripple
 
    #5) count remaining vowels in word.
    numVowels = len(re.findall(r'[eaoui]',word))
 
    #6) add one if starts with "mc"
    if word[:2] == "mc" :
        syls+=1
 
    #7) add one if ends with "y" but is not surrouned by vowel
    if word[-1:] == "y" and word[-2] not in "aeoui" :
        syls +=1
 
    #8) add one if "y" is surrounded by non-vowels and is not in the last word.
 
    for i,j in enumerate(word) :
        if j == "y" :
            if (i != 0) and (i != len(word)-1) :
                if word[i-1] not in "aeoui" and word[i+1] not in "aeoui" :
                    syls+=1
 
    #9) if starts with "tri-" or "bi-" and is followed by a vowel, add one.
 
    if word[:3] == "tri" and word[3] in "aeoui" :
        syls+=1
 
    if word[:2] == "bi" and word[2] in "aeoui" :
        syls+=1
 
    #10) if ends with "-ian", should be counted as two syllables, except for "-tian" and "-cian"
 
    if word[-3:] == "ian" : 
    #and (word[-4:] != "cian" or word[-4:] != "tian") :
        if word[-4:] == "cian" or word[-4:] == "tian" :
            pass
        else :
            syls+=1
 
    #11) if starts with "co-" and is followed by a vowel, check if exists in the double syllable dictionary, if not, check if in single dictionary and act accordingly.
 
    if word[:2] == "co" and word[2] in 'eaoui' :
 
        if word[:4] in co_two or word[:5] in co_two or word[:6] in co_two :
            syls+=1
        elif word[:4] in co_one or word[:5] in co_one or word[:6] in co_one :
            pass
        else :
            syls+=1
 
    #12) if starts with "pre-" and is followed by a vowel, check if exists in the double syllable dictionary, if not, check if in single dictionary and act accordingly.
 
    if word[:3] == "pre" and word[3] in 'eaoui' :
        if word[:6] in pre_one :
            pass
        else :
            syls+=1
 
    #13) check for "-n't" and cross match with dictionary to add syllable.
 
    negative = ["doesn't", "isn't", "shouldn't", "couldn't","wouldn't"]
 
    if word[-3:] == "n't" :
        if word in negative :
            syls+=1
        else :
            pass  
 
    #14) Handling the exceptional words.
 
    if word in exception_del :
        disc+=1
 
    if word in exception_add :
        syls+=1    
 
    # calculate the output
    return numVowels - disc + syls

if __name__ == '__main__':
    print('')
    print('')
    print('#' * 70)
    print("{:^70}".format("Running Code For Question 2H"))
    print('#' * 70)
    print('')
    print('')

    HMM, mapping, rhyming = unsupervised_learning(8,100)
    inv_map = {v: k for k, v in mapping.items()}
    numLines = 0
    count = 0
    # Average word count per line: 8.08641975308642
    #while numLines != 14:
        #numSyllables = 0
        #currentLine = (HMM.generate_emission(8))
        #currentNumberLine = copy.deepcopy(currentLine)
        #for i in range(len(currentLine)):
            #currentLine[i] = inv_map[int(currentLine[i])]
        #currentLine[0] = currentLine[0][0].upper() + currentLine[0][1:]
        #for i in currentLine:
            #if syllables(i) == sylco(i):
                #numSyllables += syllables(i)
        #if numSyllables == 10:
            #print (" ". join(currentLine))
            #print()
            #numLines += 1
    for i in range(1):
        print()
        lst =[]
        lst2 = [] 
        count = 0
        while (count < 7):
    
            flag = 0
            numSyllables = 0
            numSyllables2 = 0
            currentLine = (HMM.generate_emission(8))
            currentLine2 = (HMM.generate_emission(8))
            lastNum1 = currentLine[-1]
            lastNum2 = currentLine2[-1]
            if (lastNum1 == lastNum2):
                continue
            for i in rhyming:
                if lastNum1 in i and lastNum2 in i:
                    flag = 1
                    break
            if flag == 0:
                continue
            for i in range(len(currentLine)):
                currentLine[i] = inv_map[int(currentLine[i])]
                currentLine2[i] = inv_map[int(currentLine2[i])] 
            currentLine[0] = currentLine[0][0].upper() + currentLine[0][1:]
            currentLine2[0] = currentLine2[0][0].upper() + currentLine2[0][1:]
            
            for i in range(len(currentLine)):
                if syllables(currentLine[i]) == sylco(currentLine[i]) and syllables(currentLine2[i]) == sylco(currentLine2[i]):
                    numSyllables += syllables(currentLine[i])
                    numSyllables2 += syllables(currentLine2[i])
            if numSyllables == 10 and numSyllables2 == 10:
                lst.append(" ". join(currentLine))
                lst2.append(" ". join(currentLine2))
                count += 1
                
        assert(len(lst) == 7)
        print(lst[0])
        print(lst[1])
        print(lst2[0])
        print(lst2[1])
        print(lst[2])
        print(lst[3])
        print(lst2[2])
        print(lst2[3])
        print(lst[4])
        print(lst[5])
        print(lst2[4])
        print(lst2[5])
        print(lst[6])
        print(lst2[6])
        
            
        
                
                
            
        
        
            
        
