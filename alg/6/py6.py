#!/usr/bin/env python
# -*- encoding=utf8 -*-
import re
import operator
from functools import reduce

def WordSplit():#split
    strSrc=raw_input('Enter your sentence : ')
    strSrc=re.sub('[.,?]', "", strSrc)#regular express replace
    strSrc=strSrc.lower().split()#split words
    print(strSrc)
    
    fileName=raw_input('Enter your text file :' )
    fp=open(fileName,'r')
    
    wordUnion=[]#union of strStr and strDst
    similar={}#percent of similarity of two sentences
    for eachLine in fp:
        strDst=eachLine.lower()
        strDst=re.sub('[.,?]',"",strDst)
        strDst=strDst.split()                
        wordUnion=list(set(strSrc).union(set(strDst)))#union
        #print(wordUnion)    
        vSrc=[]#source string vector
        vDst=[]#dst string vector
        for item in wordUnion:
            vSrc.append(strSrc.count(item))#vector
            vDst.append(strDst.count(item))
        #print(vSrc)
        #print(vDst) 
        
        mulSD=reduce(lambda x,y:x+y,[vSrc[i]*vDst[i] for i in range(len(vSrc))])
        sqrtS=reduce(lambda x,y:x+y,(map(lambda x:x*x,vSrc)))**(1.0/2)
        sqrtD=reduce(lambda x,y:x+y,(map(lambda y:y*y,vDst)))**(1.0/2)
        #print(mulSD)
        #print(sqrtS)
        #print(sqrtD)
        similar[eachLine.replace('\r\n','')]=mulSD/(sqrtS*sqrtD)
        #print(similar)
    return similar

def SimilarityN():#找出最相似的N个字符串
    similarDict=WordSplit()    
    similarDict=sorted(similarDict.items(),key=operator.itemgetter(1),reverse=True)#
    N=int(input('Input the N: '))
    cnt=0#
    for (k,v) in similarDict:
        print "String ",repr(k)," have ",v," similar"    
        cnt+=1
        if(cnt>N):
            break  

if __name__=='__main__':
    SimilarityN();    
