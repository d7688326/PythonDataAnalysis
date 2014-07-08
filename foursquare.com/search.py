import info,re

database= info.search

# User input String for search
inputstring= raw_input('pleaze input what you looking for in the museums:')
# traverse the list 
for x in range(len(database)):
		comment=database[x][6]
		# desc=database[x][2]
		# if the input is found in description or comments
		if comment.rfind(inputstring) is not -1:
			# print the name, rating, and total visitor of that museum
			print database[x][0] + ' Has it! '+ '\nrating is ' + database[x][3] + '\n' + database[x][4] +' people has been there!\n\n' 
		else:
			# print not found 
			print '  No  ' + inputstring + '  in  '+ database[x][0]+ '\n'

			


