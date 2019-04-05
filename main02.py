def myData():
    values = []
    letters = "abcdefghijklmnopqrstuvwxyz"
    myInt = 0
    for letter in letters:
        myInt += 1
        values.append((letter, myInt))
        #print ("{} : {}".format(letter, myInt))
    #values('a')=15
    return values

def getWordValue(aWord, valueArray):
    returnValue = 0
    for item in valueArray:
        #print("{}".format(item[0]))
        for letter in aWord:
            if letter == item[0]:
                #print("Match found!!! Value of: {}".format(item[1]))
                returnValue += item[1]
    #print("Length of word({}): {}".format(aWord, len(aWord)))
    try:
        # Trying a new thing for returnValue.
        # Instead of going by the lookup table (see def myData)
        # I'm going by the length of the word.
        returnValue = len(aWord)
        #returnValue = round(returnValue/len(aWord))
    except:
        print("Can't do that!")
        returnValue = 0
    return returnValue

def formatSentence(lSentence):
    sentenceArray = lSentence.split(' ')
    return sentenceArray

def getSentenceValues(lSentence, valueArray):
    #print("-- beginning of getSentenceValues --")
    mySum = 0
    #print(lSentence)
    for word in lSentence:
        wv = getWordValue(word, valueArray)
        #print("{} : {}".format(word, wv))
        mySum += wv
    sentenceVal = mySum/len(lSentence)+len(lSentence)
    sentenceVal = round(sentenceVal)
    #print("Sentence value: {} ({} {})".format(sentenceVal, mySum/len(lSentence), len(lSentence)))
    #print("-- end of getSentenceValues --")
    return sentenceVal

def main():
    # Initialize
    targetSentence = "the cat slept on the mat"
    targetSentence = "python is a wonderful language"
    valueArray = myData()
    # Do the work
    print("Analysing sentence: {}".format(targetSentence))
    sentenceArray = formatSentence(targetSentence)
    sentenceValues = getSentenceValues(sentenceArray, valueArray)
    print("Value of sentence: {}".format(sentenceValues))

if __name__=='__main__':
    print("==== program begin ====")
    main()
    print("==== program end ====")
