'''
This is the query for caculationg the average rating of courses
with or without related books
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
sumofvote=0
sumofcourse=0

r= db.sixteen_courses.find({"relatedBooks":{"$exists":False}},{"voteValue":1,"_id":0})
for x in range(0,r.count()):
	if len(r[x]) ==1:
		sumofvote = sumofvote + r[x]['voteValue']
		sumofcourse=sumofcourse+1

print "avg: "+str(sumofvote/sumofcourse)

