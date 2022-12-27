# Import writer class from csv module
from csv import writer
 
# List that we want to add as a new row
List = [6, 'William', 5532, 1, 'UAE']
 
# Open our existing CSV file in append mode
# Create a file object for this file
with open('event.csv', 'a') as f_object:
 
    # Pass this file object to csv.writer()
    # and get a writer object
    writer_object = writer(f_object)
 
    # Pass the list as an argument into
    # the writerow()
    writer_object.writerow(List)
 
    # Close the file object
    f_object.close()
    
#################
# Import DictWriter class from CSV module
from csv import DictWriter

# list of column names
field_names = ['ID', 'NAME', 'RANK',
			'ARTICLE', 'COUNTRY']

# Dictionary that we want to add as a new row
dict = {'ID': 6, 'NAME': 'William', 'RANK': 5532,
		'ARTICLE': 1, 'COUNTRY': 'UAE'}

# Open CSV file in append mode
# Create a file object for this file
with open('event.csv', 'a') as f_object:

	# Pass the file object and a list
	# of column names to DictWriter()
	# You will get a object of DictWriter
	dictwriter_object = DictWriter(f_object, fieldnames=field_names)

	# Pass the dictionary as an argument to the Writerow()
	dictwriter_object.writerow(dict)

	# Close the file object
	f_object.close()

  
