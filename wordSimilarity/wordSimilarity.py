#coding:utf-8
import codecs
import math
import csv

###read word2vec file
def init(path):
    dictMap = {}
    fin = codecs.open(path,"r","utf-8")
    for line in fin.readlines():
        dictMap[line[0:line.index(" ")].strip()] = line[line.index(" "):].strip()
    return dictMap

###read LDA file
def ldaWordMapInit(path, n):
    vec = ""
    fin = codecs.open(path,"r","utf-8")
    for topicID in range(0,100):
        if topicID%33==0:
            print topicID
        line = fin.readline()
        word = line.strip().split()
        vec += word[n] + " "
    return vec 

###the module of vector(List)  
def lengt(v):
    sum = 0.0
    for num in v:
        print num
        sum += math.pow(float(num), 2)
    return math.sqrt(sum)

###cosine similarity(String)
def distance(v1,v2):
    sum = 0.0
    v1 = v1.strip().split(" ")
    v2 = v2.strip().split(" ")
    for i in range(len(v1)):
        sum += float(v1[i]) * float(v2[i])
    return sum/(lengt(v1)*lengt(v2))
   
    
if __name__ == "__main__":
    pathMatrix = "../ldaData/model-final.phi"       #topic*word matrix    raw:topic column:word
    pathMap = "../ldaData/wordmap.txt"
    dictMap = init(pathMap)                         #wordMap    key:word, value:index
    
    csvfilew = file('../similarity/result.csv', 'wb')
    writer = csv.writer(csvfilew)
    
    csvfiler = file('../similarity/combinedWord.csv','rb')
    reader = csv.reader(csvfiler)
    for line in reader:
        v1 = ldaWordMapInit(pathMatrix, (int)(dictMap[line[0].lower()]))
        v2 = ldaWordMapInit(pathMatrix, (int)(dictMap[line[1].lower()]))
        dis = distance(v1,v2)
        print line[0]+":"+dictMap[line[0].lower()] + "\t" + line[1]+":"+dictMap[line[1].lower()] + "\t" + (str)(dis)
        writer.writerow([line[0],line[1],dis])
#         print "1: " + v1 + "2: " + v2

#     print "love\t" + "sex:\t" + str(distance(v1, v2)*10)

    csvfilew.close()
    csvfiler.close()
    print "end!"