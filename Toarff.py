'''Read date from mongodb and export as course.arff'''
import pymongo

def findkey(dictobject,key):
	if dictobject.has_key(key):
		return True
	else:
		return False
# file to be written

fw=open('nnnnn.arff','w')
fw.write('@relation courses\n')
fw.write('@attribute provider STRING\n')
fw.write('@attribute catogary STRING\n')
fw.write('@attribute voteCount NUMERIC\n')
fw.write('@attribute voteValue NUMERIC\n')
fw.write('@attribute simiCount NUMERIC\n')
fw.write('@attribute bookCount NUMERIC\n')
fw.write('@attribute bookExist {0,1}\n')
fw.write('@attribute voteOrnot {0,1}\n')
fw.write('@attribute freeOrnot {0,1}\n')
fw.write('@data\n\n')



#connect to db
connection=pymongo.Connection('localhost',27017)
db=connection.courses
savecourse=db.sixteen_courses
#all courses sort by vote value
test=savecourse.find().sort([("voteValue",-1)])
for n in test:
	if findkey(n,"provider")is True:
		provider="'"+n['provider']+"'" 
	else:
		provider='?'

	if findkey(n,"catogary")is True:
		catogary="'"+",".join(n['catogary'])+"'"
	else:
		catogary='?'
	#voteCount
	if findkey(n,"voteCount")is True:
		voteCount=n['voteCount']
		voteOrnot=1 
	else:
		voteCount=0
		voteOrnot=0
	#vote value
	if findkey(n,"voteValue")is True:
		voteValue=n['voteValue'] 
	else:
		voteValue=0
	#similar course count
	if findkey(n,"SimiCourse")is True:
		simiCount=len(n['SimiCourse'])
	else:
		simiCount=0
	#book count
	if findkey(n,"relatedBooks")is True:
		books=len(n['relatedBooks'])
		bookExist=1
	else:
		books=0
		bookExist=0
	# free or not
	if findkey(n,"free")is True:
		freeOrnot=1
	else:
		freeOrnot=0

	fw.write(provider+',')
	fw.write(catogary+',')
	fw.write(str(voteCount)+',')
	fw.write(str(voteValue)+',')
	fw.write(str(simiCount)+',')
	fw.write(str(books)+',')
	fw.write(str(bookExist)+',')
	fw.write(str(voteOrnot)+',')
	fw.write(str(freeOrnot)+'\n')


print test.count()