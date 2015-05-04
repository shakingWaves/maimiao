#!/usr/bin/env python
import pymongo
#connection
conn=pymongo.Connection("127.0.0.1",2201)
db=conn.test
#insert
u=dict(name="lixiaobo",age=23)
db.lixb.save(u)
v=dict(name="2222",age=24)
db.lixb.save(v)
for i in range(10):
	db.lixb.save({"name":"li"+str(i),"age":i+10})
result=db.lixb.find()
u=dict(name=listtt,age=25)
db.lixb.insert(u)
print list(result),
#update single
u2=db.lixb.find_one({"name":"listtt"})
if u2 and hasattr(u2,age):
	u2['age']+=3
db.lixb.save(u2)
#update multiply records
db.lixb.update({},{"$inc":{"age":10}},nulti=True)
db.lixb.update({"name":"lixiaobo"},{"$inc":{"age":10},"$set":{"sex":1}})

