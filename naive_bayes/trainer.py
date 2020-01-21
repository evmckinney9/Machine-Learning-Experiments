import headline_scanner as hs
#hs.readHeadlines("fake"))
#hs.readHeadlines("real"))

#we need to make a map that has word:occurences


def getdictFake():
    dictFakeFreq = {}
    #fill in values from fake news
    fakeHeadlines = hs.readHeadlines("fake")
    for headline in fakeHeadlines:
        for word in headline.split():
            if dictFakeFreq.get(word) == None:
                dictFakeFreq[word] =1
            else:
                dictFakeFreq[word] = dictFakeFreq.get(word) + 1
    #sortedfake = sorted(dictFakeFreq, key = dictFakeFreq.get, reverse = True)
    #for k in range(100):
        #print(sortedfake[k])
        #print(dictFakeFreq.get(sortedfake[k]))
    return dictFakeFreq

def getdictReal():
    #fill in values from real news
    dictRealFreq = {}
    readHeadlines = hs.readHeadlines("real")
    for headline in readHeadlines:
        for word in headline.split():
            if dictRealFreq.get(word) == None:
                dictRealFreq[word] =1
            else:
                dictRealFreq[word] = dictRealFreq.get(word) + 1
    #sortedreal = sorted(dictRealFreq, key = dictRealFreq.get, reverse = True)
    #for k in range(100):
        #print(sortedreal[k])
        #print(dictRealFreq.get(sortedreal[k]))
    return dictRealFreq

def getdictTotal():
    totaluniquewords = 0
    dictTotal = {}
    headlines = hs.readHeadlines("real")
    for headline in headlines:
        for word in headline.split():
            if dictTotal.get(word) == None:
                dictTotal[word] =1
            else:
                dictTotal[word] = dictTotal.get(word) + 1
    headlines = hs.readHeadlines("fake")
    for headline in headlines:
        for word in headline.split():
            if dictTotal.get(word) == None:
                dictTotal[word] =1
            else:
                dictTotal[word] = dictTotal.get(word) + 1         
   
    return dictTotal

