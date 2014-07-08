import os,sys,re,string

inFolder='FoursquarePages'

files=os.listdir(inFolder)

fw=open('infos.txt','w')

search=[]


for musuems in files:

    photoNum=-1
    venueName=''
    Description=''
    rating=-1
    visitor= -1
    Comments=''
    data=[]


    f=open(inFolder+'/'+musuems)

    html=f.read()

    regPhoto= re.compile(r'See\sall\s(\d+)')

    # <h1 class="venueName" itemprop="name">El Museo del Barrio</h1>
    regName=re.compile(r'<h1\sclass="venueName"\sitemprop="name">(.*?)</h1>')

    # <p class="venueDescription">The Metropolitan Museum of Art, located in New York City, is the largest art museum in the United States with among the most significant art collections. Its permanent collection contains more than two million works, divided among nineteen curatorial departments.</p>
    regDescript=re.compile(r'<p\sclass="venueDescription">(.*?)</p>')

    # <span itemprop="ratingValue">8.9</span>
    regRating=re.compile(r'<span\sitemprop="ratingValue">(.*?)</span>')

    # <div class="venueStat">Total Visitors<br /><strong class="venueStatCount" data-count="6057">
    regVistor=re.compile(r'<div\sclass="venueStat">Total\sVisitors<br\s/><strong\sclass="venueStatCount"\sdata-count="(\d+)">')

    # <h3 class="tipCount">69 Tips</h3>
    regTip=re.compile(r'<h3\sclass="tipCount">([\d,]+)\sTips</h3>')

    # <p class="tipText">
    regComment=re.compile(r'<p\sclass="tipText">(.*?)</p>')
    # get tag contents with compiled regex objects
    try:
     	photoNum= re.search(regPhoto,html)
        if photoNum is not None:
            photoNumYes=str(photoNum.group(1))
        else :
            photoNumYes='empty' 


     	venueName= re.search(regName,html)
        if venueName is not None:
            venueNameYes=str(venueName.group(1))
        else :
            venueNameYes='empty' 

    	Description=re.search(regDescript,html)
        if Description is not None:
            DescriptYes=str(Description.group(1))
        else :
            DescriptYes='empty' 

        rating=re.search(regRating,html)
        if rating is not None:
            ratingYes=str(rating.group(1))
        else :
            ratingYes='empty' 

        visitor=re.search(regVistor,html)
        if visitor is not None:
            visitorYes=str(visitor.group(1))
        else :
            visitorYes='empty' 

        tipCount=re.search(regTip,html)
        if tipCount is not None:
            tipCountYes=str(tipCount.group(1))
        else :
            tipCountYes='empty' 

        CommentWithLink=re.findall(regComment,html)
        # adjust format for comments
        Comment= '\n--'.join(CommentWithLink)
        # replace amp& with &
        Comments=re.sub(r'<a.*?</a>',r' ',Comment)

        venueNamefix=string.replace(venueNameYes,'&amp;','&')
        # write all the information into info.txt
        fw.write("#name:#\n"+venueNamefix+'\n#Photo Number:#\n'+ photoNumYes + '\n#description:#\n' + DescriptYes + '\n#rating:#\n' + ratingYes + '\n#total visitor:# \n' + visitorYes+ '\n#total tips:# \n' + tipCountYes+ '\n#Comments:#\n--' + Comments+'\n#end here#\n\n\n')
        # store a list with all the information for searching funtion
        data=[venueNamefix,photoNumYes,DescriptYes,ratingYes,visitorYes,tipCountYes,Comments]

        search.append(data)

        #print search


    except AttributeError as e:
        print sys.exc_info()

print 'All done!'

    
