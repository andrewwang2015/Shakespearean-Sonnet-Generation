########################################
# CS/CNS/EE 155 2017
# Problem Set 5
#
# Author:       Avishek Dutta
# Description:  Set 5
########################################
import copy

class Utility:
    '''
    Utility for the problem files.
    '''

    def __init__():
        pass
       

    @staticmethod
    def load_shakespeare_hidden():
        '''
        Loads the file 'shakespeare.txt'.

        Returns:
            lines:      Sequences of observations, i.e. a list of lists.
                        Each sequence represents a single line of the sonnet
            lines_map:  A hash map that maps each observation to an integer.
        '''
        lines = []
        lines_map = {}
        allWords = []
        counter = 0
        
        file = open("shakespeare.txt", "r") 
        
        for line in file:
            line = line.strip()
            if line == '' or line[0].isdigit():
                continue
            wordsInLine = line.split()
            lines.append(wordsInLine)
            
        numberedLines = copy.deepcopy(lines)        # analogous list of lists but w/ numbers
         
        for i in range(len(numberedLines)):
            for j in range(len(numberedLines[i])):
                if numberedLines[i][j] not in lines_map:
                    lines_map[numberedLines[i][j]] = counter
                    numberedLines[i][j] = counter
                    counter += 1
                else:
                    numberedLines[i][j] = lines_map[numberedLines[i][j]]
        
        return numberedLines, lines_map

    def load_shakespeare_hidden_stripped():
            '''
            Loads the file 'shakespeare.txt'.
    
            Returns:
                lines:      Sequences of observations, i.e. a list of lists.
                            Each sequence represents a single line of the sonnet
                lines_map:  A hash map that maps each observation to an integer.
            '''
            lines = []
            lines_map = {}
            allWords = []
            counter = 0
            
            file = open("shakespeare.txt", "r") 
            
            for line in file:
                line = line.strip()
                if line == '' or line[0].isdigit():
                    continue
                wordsInLine = line.split()
                for i in range(len(wordsInLine)):
                    if wordsInLine[i] != 'I':
                        wordsInLine[i] = wordsInLine[i].lower()
                    wordsInLine[i] = "".join(c for c in wordsInLine[i] if c not in ('!','.',':', '?', ',', '-', '(', ')'))
                        
                lines.append(wordsInLine)
                
            numberedLines = copy.deepcopy(lines)        # analogous list of lists but w/ numbers
             
            for i in range(len(numberedLines)):
                for j in range(len(numberedLines[i])):
                    if numberedLines[i][j] not in lines_map:
                        lines_map[numberedLines[i][j]] = counter
                        numberedLines[i][j] = counter
                        counter += 1
                    else:
                        numberedLines[i][j] = lines_map[numberedLines[i][j]]
            
            return numberedLines, lines_map
        
 
    def load_shakespeare_hidden_stripped_poems():
            '''
            Loads the file 'shakespeare.txt'.
    
            Returns:
                lines:      Sequences of observations, i.e. a list of lists.
                            Each sequence represents a single line of the sonnet
                lines_map:  A hash map that maps each observation to an integer.
            '''
            rhymingList = []
            lst13 = []
            lst24 = []
            lst57 = []
            lst68 = []
            lst911 = []
            lst1012 = []
            lst1314 =[]
            poems_map = {}
            counter = 0
            poems = []
            file = open("combined.txt", "r") 
            poemWords = []
            count = 0
            lineCount = 0
            lastWords = []
            
    
            for line in file:
                line = line.strip()
                if (line == '' or line[0].isdigit() or len(line) < 15) and poemWords != []:
                    if count > 151:
                        poems.append(poemWords)   # This is where spencer.txt comes in
                    else:
                        poems.append(poemWords[1:]) # For some reason, the numbers by sonnets are added to beginning
                    poemWords = []
                    count += 1
                    continue
                
                wordsInLine = line.split()

                
                for i in range(len(wordsInLine)):
                    if wordsInLine[i] != 'I':
                        wordsInLine[i] = wordsInLine[i].lower()
                    wordsInLine[i] = "".join(c for c in wordsInLine[i] if c not in ('!','.',':', ';', '?', ',', '-', '(', ')'))
                if len(wordsInLine) > 3:
                        lastWord = wordsInLine[-1]
                        lastWords.append(lastWord)  
                        
                poemWords.extend(wordsInLine)
                
            poems = [x for x in poems if x != [] and len(x) > 15]
            numberedPoems = copy.deepcopy(poems)        # analogous list of lists but w/ numbers
             
            for i in range(len(numberedPoems)):
                for j in range(len(numberedPoems[i])):
                    if numberedPoems[i][j] not in poems_map:
                        poems_map[numberedPoems[i][j]] = counter
                        numberedPoems[i][j] = counter
                        counter += 1
                    else:
                        numberedPoems[i][j] = poems_map[numberedPoems[i][j]]
            for i in range(len(lastWords)):
                lineCount += 1
                if i % 14 == 0 or i % 14 ==2:
                    lst13.append(lastWords[i])
                elif i % 14 == 1 or i % 14 == 3:
                    lst24.append(lastWords[i])
                elif i % 14 == 4 or i%14 == 6:
                    lst57.append(lastWords[i])
                elif i % 14 == 5 or i % 14 == 7:
                    lst68.append(lastWords[i])
                elif i % 14 == 8 or i % 14 == 10:
                    lst911.append(lastWords[i])
                elif i % 14 == 9 or i% 14 == 11:
                    lst1012.append(lastWords[i])
                else:
                    lst1314.append(lastWords[i])
                
                if lineCount == 14:
                    lineCount = 0
                    rhymingList.append(lst13)
                    rhymingList.append(lst24)
                    rhymingList.append(lst57)
                    rhymingList.append(lst68)
                    rhymingList.append(lst911)
                    rhymingList.append(lst1012)
                    rhymingList.append(lst1314)
                    lst13 = []
                    lst24 = []
                    lst57 = []
                    lst68 = []
                    lst911 = []
                    lst1012 = []
                    lst1314 = []
            originalRhyme = copy.deepcopy(rhymingList)
            currentRhyme = []
            newRhyme = []
            for i in range(len(rhymingList)):
                currentRhyme = []
                for j in range(i, len(rhymingList)):
                    if set(rhymingList[i]) & set(rhymingList[j]):
                        currentRhyme.extend(list(set().union(rhymingList[i], rhymingList[j])))
                newRhyme.append(currentRhyme)
            for i in range(len(newRhyme)):
                newRhyme[i] = list(set(newRhyme[i]))
                
                       
                
            numberedRhymingList = copy.deepcopy(newRhyme)
            for i in range(len(numberedRhymingList)):
                for j in range(len(numberedRhymingList[i])):
                    numberedRhymingList[i][j] = poems_map[numberedRhymingList[i][j]]
            return numberedPoems, poems_map, numberedRhymingList
        
#for i in Utility.load_shakespeare_hidden_stripped_poems()[2]:
    #print (i)

#print (len(Utility.load_shakespeare_hidden_stripped_poems()[2]))

