'''
This is the query for deviding vote value into several sections and 
find relation how many courses in this section are provided by certain provider
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

# query for finding 
r= db.sixteen_courses.aggregate(
	[
		{"$match":{"voteValue":{"$gt":4.5}}},
		{"$group":{"_id":"$provider","avgRate":{"$avg":"$voteValue"},"sumCourse":{"$sum":1},"avgVote":{"$avg":"$voteCount"}}}
	]
)
for x in range(0,len(r['result'])):
	if r['result'][x]["_id"] is not None:
		print "provider=="+r['result'][x]["_id"]+":"
		print r['result'][x]["avgRate"]
		print r['result'][x]["sumCourse"]
		print r['result'][x]["avgVote"]
		print "###############"

