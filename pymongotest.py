#!/usr/bin/env python
import pymongo
conn=pymongo.Connection("127.0.0.1",2201)
db=conn.test
u=dict(name="lixiaobo",age=23)
db.lixb.save(u)
v=dict(name="2222",age=24)
db.lixb.save(v)
for i in range(10):
	db.lixb.save({"name":"li"+str(i),"age":i+10})
result=db.lixb.find()
print list(result),

