from math import log10
import trainer as t
#t.getdictFake()
#t.getdictReal()
#t.getdictTotal()

print("Training...\n")
#from number of training data
fakelength = 12124
reallength = 910111
totallength = 922235
#variables
dictFake = t.getdictFake()
dictReal = t.getdictReal()
dictTotal = t.getdictTotal()
fakeWordCount = len(dictFake.keys())
realWordCount = len(dictReal.keys())
totalWordCount = len(dictTotal.keys())

#given a string determine if more likely real or fake headline

#define some equations
def fakeGivenString(header):
    #calc = log10(fakelength/totallength)
    calc = .5
    for word in header.split():
        calc += log10(wordGivenFake(word))
    return calc
def realGivenString(header):
    #calc = log10(reallength/totallength)
    calc = .5
    for word in header.split():
        calc += log10(wordGivenReal(word))
    return calc

def wordGivenFake(w):
    c = 0
    if dictFake.get(w) != None:
       c = dictFake[w]
    numerator = 1 + c
    denominator = fakelength + totalWordCount
    return numerator/denominator
    
def wordGivenReal(w):
    c = 0
    if dictReal.get(w) != None:
       c = dictReal[w]
    numerator = 1 + c
    denominator = reallength + totalWordCount
    return numerator/denominator

def runner(s):
    p1 = fakeGivenString(s)
    p2 = realGivenString(s)
    if p1 > p2:
        print("I think it is fake\n")
    else:
        print("I think it is real\n")

def main():
    h = ""
    while (h != "f"):
        print("Type a news headline\n")
        h = input()
        h = h.lower()
        runner(h)
main()
