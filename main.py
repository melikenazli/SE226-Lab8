from abc import ABC, abstractmethod

class Count (ABC):
    address = ''
    def __init__(self, file_address):
        Count.address = file_address

    @abstractmethod
    def calculateFreqs(self):
        pass

class ListCount (Count):

    def __init__(self, some_address):
        Count.__init__(self, some_address)

    def calculateFreqs(self):
        wordList = []
        wordFreqList = []
        with open(ListCount.address, 'r') as f:
            for line in f:
                for word in line.split():
                    wordList.append(word)
            f.close()

        print("List:\n", wordList)

        for item in range(0, len(wordList)):
            if item not in wordFreqList:
                item_count = wordList.count(wordList[item])
                wordFreqList.append(str(str(wordList[item]) + ' = ' + str(item_count)))

        print("Frequency list:\n", wordFreqList)

class DictCount(Count):
    def __init__(self, another_address):
        Count.__init__(self, another_address)

    def calculateFreqs(self):
        wordDict = {}
        wordFreqDict = {}
        with open(DictCount.address, 'r') as f:
            for line in f:
                for word in line.split():
                    wordDict[word] = 0
                    if word in wordFreqDict:
                        wordFreqDict[word] += 1
                    else:
                        wordFreqDict[word] = 1
            f.close()

        print("Dictionary:\n", wordDict)
        print("Words with frequencies:\n", wordFreqDict)


obj1 = ListCount("C:\\Users\\melik\\Desktop\\strange.txt")
obj1.calculateFreqs()

print()

obj2 = DictCount("C:\\Users\\melik\\Desktop\\strange.txt")
obj2.calculateFreqs()




