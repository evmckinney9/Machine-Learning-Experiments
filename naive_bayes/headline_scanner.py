def real():
    #read from real news
    readpath = "headline-data\\real_news.txt"
    return readpath

def fake():
    #read from fake news
    readpath = "headline-data\\fake_news.txt"
    return readpath

def readHeadlines(c):
    if (c == "real"):
        readpath = real()
    if (c == "fake"):
        readpath = fake()
        
    file = open(readpath, "r")
    headlines = file.read().split("\n")
    return headlines

