# create a list of dictionaries
# with student data
data = [
    {'name': 'sravan', 'subjects': ['java', 'python']},
    {'name': 'bobby', 'subjects': ['c/cpp', 'java']},
    {'name': 'ojsawi', 'subjects': ['iot', 'cloud']},
    {'name': 'rohith', 'subjects': ['php', 'os']},
    {'name': 'gnanesh', 'subjects': ['html', 'sql']}
]
  
# display first student
print(data[0])
  
# display all student
data


# update first student python subject
# to html
data[0]['subjects'].append('html')
data[0]['subjects'].pop(1)
  
# update third student java subject
# to dbms
data[2]['subjects'].append('dbms')
data[2]['subjects'].pop(1)
  
# update forth student php subject
# to php-mysql
data[3]['subjects'].append('php-mysql')
data[3]['subjects'].pop(0)
  
# display updated list
data



# update first student python subject
# to html
data[0]['subjects'].insert(0, 'html')
data[0]['subjects'].pop(1)
  
# update third student java subject
# to dbms
data[2]['subjects'].insert(0, 'dbms')
data[2]['subjects'].pop(1)
  
# update forth student php subject
# to php-mysql
data[3]['subjects'].insert(1, 'php-mysql')
data[3]['subjects'].pop(0)
  
# display updated list
data
