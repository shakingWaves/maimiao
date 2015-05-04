#!/usr/bin/env python
import re
import pymongo
#connection
def connect():
    conn=pymongo.Connection("127.0.0.1",2201)
    db=conn.test
    return db
#insert
def insertOp(db):
    u=dict(name="l2ixiaobo",age=23)
    db.lixb.save(u)
    for i in range(10):
        db.lixb.save({"name":"li"+str(i),"age":i+10})
    u=dict(name="l3isttt",age=25)
    db.lixb.insert(u)
#update single
def updateOp(db):
    u2=db.lixb.find_one({"name":"l3isttt"})
    if u2 and hasattr(u2,"age"):
        u2['age']+=3
        db.lixb.save(u2)
    elif u2:
        db.lixb.update({"name":"l3isttt"},{"name":"l3isttt","age":25,"sex":2})
        print  db.lixb.find_one({"name":"l3isttt"})
    #update multiply records
    db.lixb.update({},{"$inc":{"age":10}},multi=True)
    print "before update:" ,list(db.lixb.find({"name":"l2ixiaobo"}))
    db.lixb.update({"name":"l2ixiaobo"},{"$inc":{"age":10},"$set":{"sex":1}})
    print "after update:" ,list(db.lixb.find({"name":"l2ixiaobo"}))
    #search
    result=db.lixb.find()
    for i in result: 
        print  i
#delete
def deleteOp(db):
    #regx=re.compile('^2*')
    #result=db.lixb.find({'name':regx})
    result=db.lixb.find({'name':{'$regex':'l*'}})
    print "after delete:"
    for i in result: 
        print  i
        db.lixb.remove(i)
    
    for i in result: 
        print  i

if __name__=='__main__':
    db=connect()
    db.lixb.drop()
    insertOp(db)
    updateOp(db)
    deleteOp(db)
