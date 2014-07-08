'''
This is the query for finding the relation between related books 
and vote value
'''

import pymongo,json
def findkey(dictobject,key):
	if dictobject.has_key(key):
		return True
	else:
		return False

connection=pymongo.Connection('localhost',27017)
db=connection.courses
savecourse=db.course_list
rateValue=0.0
rateCount=0
norate=0

r= db.sixteen_courses.aggregate(
		[
			{"$unwind":"$relatedBooks"},
			{"$group":{"_id":{"name":"$courseName","rate":"$voteValue"},"size":{"$sum":1}}},
			{"$match":{"size":{"$gt":15,"$lt":20}}},

		]
	)

for x in range(0,len(r['result'])):
	if len(r['result'][x]['_id']) is 2:
		rateValue+=r['result'][x]['_id']['rate']
		rateCount+=1
	else:
		norate+=1

print "simi course 15-20 avgrate: " +str(rateValue/rateCount)
print "no rate courses "+str(norate)
