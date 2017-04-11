import sys

def tokenize(file):
    import re #regular expression library to detect spaces and special characters
    file = open(file,'r')
    txt = file.read()
    ListOfWords = re.compile('\W').split(txt.lower())
    return ListOfWords

def FrequencyCalculation(ListOfWords):
    from collections import Counter
    frequencyList = Counter(ListOfWords)
    del frequencyList['']
    return frequencyList

def printOutput(frequencyList):
    #frequencyList.sort(key = lambda x:x[1], reverse = True)
    #frequencyList.sort(key = lambda x:x[0], reverse = False)
    for x in sorted(frequencyList.items(),key = lambda x:(-x[1],x[0])):
        print(str(x[0]) +" - "+ str(x[1]))

    #for x in frequencyList.items():
        
if len(sys.argv) < 2:
    print("Please specify a file name")
    sys.exit(0)
    
ListOfWords = tokenize(sys.argv[1])
frequencyList = FrequencyCalculation(ListOfWords)
printOutput(frequencyList)
