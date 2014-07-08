'''
	This is the Mongodb query for finding average rate, course amount and average population who vote for this course
'''

import pymongo,json
# find if the key exists in database
def findkey(dictobject,key):
	if dictobject.has_key(key):
		return True
	else:
		return False

connection=pymongo.Connection('localhost',27017)
db=connection.courses
# aggregate of 1600 courses group by catogary,get the result and print
r=db.sixteen_courses.aggregate(
		[
			{"$unwind":"$catogary"},
			{"$group":{"_id":"$catogary","avgRate":{"$avg":"$voteValue"},"sumCourse":{"$sum":1},"avgVote":{"$avg":"$voteCount"}}}
		],
	)

for x in range(0,len(r['result'])):
	print "catogary=="+r['result'][x]["_id"]+":"
	print r['result'][x]["avgRate"]
	print r['result'][x]["sumCourse"]
	print r['result'][x]["avgVote"]
	print "###############"
