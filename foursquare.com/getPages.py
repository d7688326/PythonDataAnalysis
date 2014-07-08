"""
This script reads the file that was created by findurl.py and downloads
the result page for each url and stores it in a new file name with the museum name

 """ 
 
import urllib2,os,re

browser=urllib2.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0')]

# Download the files to this folder
outFolder='FoursquarePages'

# make this folder if not exist
if not os.path.exists(outFolder): 
    os.mkdir(outFolder)

# open file
fileReader=open('links.txt')
for line in fileReader: 
        # remove the leading and trailing characters 
        link=line.strip() 
        print 'Saving :', link
        
        html=browser.open(link).read()
   		# get file name from the link
        name=re.search(r'v/([\w-]+)',link)
      
        # write file into the folder
        fileWriter=open(outFolder+'/'+str(name.group(1)), 'w')
        fileWriter.write(html)
        fileWriter.close()

   
fileReader.close()