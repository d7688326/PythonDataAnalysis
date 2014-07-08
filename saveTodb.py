'''
    Script for reading downloaded website file(.txt) and store data into Mongodb
'''
import os,sys,re,string
import pymongo
# connect to mongodb
connection=pymongo.Connection('localhost',27017)
db=connection.courses
savecourse=db.sixteen_courses

nameGlobal=''

f=open('rating_pages1600.txt')
# read line by line
for line in f:
    thislink=line.strip()
    # regex for find the data we want from the file
    regName = re.compile(r'<h3>\s*<span\s*>(.*)</span\s*>')
    regCategory = re.compile(r'<a\shref="/category/\d+/(.*)\.htm"\s>')
    regProvider = re.compile(r'<a\s*href="/providers/\d+/.*"\s*>(\w+)</a>')
    regFree = re.compile(r'<span\s*class="freecourse"\s*>(.*?)</span>')
    regVote = re.compile(r'<span\sclass="votes"\s*id=.*>(\d+)\svotes</span>')
    regVValue = re.compile(r'<div\s*class="ratingstar"\s*id=.*data-rating="(.*)"\s*style=.*>')
    regSimilar = re.compile(r'<div\s*class="limittitle"\s*>\s*<a.*>(.*)</a></div>')
    regBook = re.compile(r'<span\s*class="title">(.*)</span\s*>')
    regiTunes = re.compile(r'<h3>iTunes\s*Podcasts</h1>.*<span\s*class="title">(.*)</span>')

    try:
        # store name into database
     	nameOfCourse = re.search(regName, line)
        if nameOfCourse is not None:
           name = str(nameOfCourse.group(1))
           name=name.decode('utf-8','ignore')
           name=name.encode('utf-8')
           nameToAdd={"courseName":name}
           savecourse.insert(nameToAdd)
           nameGlobal=name
           

        categoryOfCourse = re.search(regCategory, line)
        if categoryOfCourse is not None:
            cate = str(categoryOfCourse.group(1))
            cate = string.replace(cate,'+',' ')
            savecourse.update(
                {"courseName":nameGlobal},
                {"$addToSet": { "catogary": cate } }
            )   

        provider = re.search(regProvider, line)
        if provider is not None :
           prov = str(provider.group(1))
           savecourse.update(
                {"courseName":nameGlobal},
                {"$set": { "provider": prov } }
            )   


        free=re.search(regFree,line)
        if free is not None:
            fre=str(free.group(1))
            savecourse.update(
                {"courseName":nameGlobal},
                {"$set": { "free": fre } }
            )   

        votes = re.search(regVote,line)
        if votes is not None:
            vote=int(votes.group(1))
            savecourse.update(
                {"courseName":nameGlobal},
                {"$set": { "voteCount": vote } }
            )   
            # w.write("vote num:"+vote+"\n")

        voteValue=re.search(regVValue,line)
        if voteValue is not None:
            value=float(voteValue.group(1))
            savecourse.update(
                {"courseName":nameGlobal},
                {"$set": { "voteValue": value } }
            ) 

        similar=re.search(regSimilar,line)
        if similar is not None:
            simi=str(similar.group(1))
            simi=simi.decode('utf-8','ignore')
            simi=simi.encode('utf-8')
            savecourse.update(
                {"courseName":nameGlobal},
                {"$addToSet": {"SimiCourse":simi} }
            )   

        books=re.search(regBook,line)
        if books is not None:
            book=str(books.group(1))
            savecourse.update(
                {"courseName":nameGlobal},
                {"$addToSet": {"relatedBooks":book} }
            )   
            w.write("Related books are:"+book+"\n")


    except AttributeError as e:
        print sys.exc_info()

print 'All done!'

    
