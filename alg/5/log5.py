 
def ReadFile():
        fileName=raw_input('Enter the file name : ')
        fp=open(fileName,'r')
        return fp
   
def ReadContent():
        fp=ReadFile()
        sl=set()
        for eachLine in fp:
            sl.add(eachLine.split(' ')[0])
        return sl
        
def PrintSet():
        sl=ReadContent()
        print "unique IP : ",len(sl)
        for eachElem in sl:
            print(eachElem)
            
            
        
if __name__=='__main__':
        PrintSet()
