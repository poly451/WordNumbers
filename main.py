

letters = "abcdefghijklmnopqrstuvwx"
translation_string=""

def initArray():
    letterArray=dict()
    value = 0
    for letter in letters:
        value += 1
        letterArray[value]=[(letter, False)]
        #print("{} : {}".format(letter, value))
    return letterArray

def evaluateWord(lArray, aword):
    for mychar, therest in lArray.items():
        if therest[0][0] in aword:
            #print("{} : {}".format(mychar, therest))
            lArray[mychar] = [(therest[0][0], True)]
            print(lArray[mychar])
            #print(therest[0][1])
        #print(therest[0][0])
    return lArray

def drawCharDict(lArray):
    print("======================")
    #print(lArray[1])
    mynum = 0
    for mychar, therest in lArray.items():
        print("{} : {}".format(mychar, therest))
        print("{}={}".format(therest[0][0], therest[0][1]))
        mynum += 1
    print("======================")
    print (lArray)
    print(" a b c d e f g h i j k l m n o p q r s t u v w x")
    print("|X| | |x| | | | | | | | | |x| | | | | | | | | | | |")

def drawGrid(lArray):
    print("---- drawGrid start ----")
    ff = "| "
    tt = "|X"
    printString = ""
    for firstElem, secondElem in lArray.items():
        print("{} : {}".format(lArray[firstElem][0][0], lArray[firstElem][0][1]))
        if lArray[firstElem][0][1]==False:
            #print("false!!!!")
            printString += ff
        else:
            #print("true!!!!")
            printString += tt
    print(" a b c d e f g h i j k l m n o p q r s t u v w x")
    print(printString)
    print('---- drawGrid end ----')

def stripToGrid(lArray):
    myArray = []
    for firstElem, secondElem in lArray.items():
        #print(lArray[firstElem])
        if lArray[firstElem][0][1]==False:
            myArray.append(False)
        else:
            myArray.append(True)
    return myArray

def getMapping(theValue, myMap):
    for myvalue, myresult in myMap:
        if theValue == myvalue:
            return myresult
    return -1

def mapGrid(myArray, myMap):
    #if (myArray[0] == True) and (myArray[1] == True) and (myArray[2] == True):
    myNums = []
    print("myArray: {}".format(myArray))
    print("myArray, first three: {} {} {}".format(myArray[0], myArray[1], myArray[2]))
    if myArray[0]==False and myArray[1]==False and myArray[2]==False:
        # The value of this is 0, so we plug "0" into myMap to get the value we need.
        theValue = getMapping(0, myMap)
        #print("Map: {} : {}".format(myMap[0][0], myMap[0][1])
    if myArray[0]==False and myArray[1]==False and myArray[2]==True:
        myNums.append(1)
    if myArray[0]==False and myArray[1]==True and myArray[2]==False:
        myNums.append(2)
    myMap=[(True, True, True),(True, True, False)]
    print("Yea!!! :-) {} : {}".format(myMap[0][0], myMap[1]))

def main():
    print("==== start ====")
    letterArray = initArray()
    letterArray = evaluateWord(letterArray, "lovely")
    drawCharDict(letterArray)
    drawGrid(letterArray)
    myArray = stripToGrid(letterArray)
    myMap = []
    newArray = mapGrid(myArray, myMap)
    print("==== end ====")

if __name__=="__main__":
    main()
