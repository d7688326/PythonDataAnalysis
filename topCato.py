'''
This is the query for finding top catogaries from the database
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


r= db.sixteen_courses.aggregate(
	[
		{"$unwind":"$catogary"},
		{"$group":{"_id":"$catogary","avgRate":{"$avg":"$voteValue"},"sumCourse":{"$sum":1},"avgVote":{"$avg":"$voteCount"}}},
		{"$sort":{"avgVote":-1}}
	]
)
for x in range(0,len(r['result'])):
	if r['result'][x]["_id"] is not None:
		print r['result'][x]["_id"]
