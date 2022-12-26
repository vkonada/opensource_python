programming_languages = ["JavaScript","Python","Java","C++"]

print(programming_languages.index("Python"))

'''
1
'''
#######################
programming_languages = ["JavaScript","Python","Java","C++"]

print(programming_languages.index("React"))

#output
#line 3, in <module>
#    print(programming_languages.index("React"))
#ValueError: 'React' is not in list

#######################

programming_languages = ["JavaScript","Python","Java","Python","C++","Python"]

try:
    print(programming_languages.index("React"))
except ValueError:
    print("That item does not exist")
    
#output
#That item does not exist

#######################

programming_languages = ["JavaScript","Python","Java","Python","C++","Python"]

print("React" in programming_languages)

#output
#False
#######################

programming_languages = ["JavaScript","Python","Java","Python","C++","Python"]

python_indices = []

for programming_language in range(len(programming_languages)):
  
#######################
  
programming_languages = ["JavaScript","Python","Java","Python","C++","Python"]
python_indices = []

for programming_language in range(len(programming_languages)):
    if programming_languages[programming_language] == "Python":
      python_indices.append(programming_language)

print(python_indices)

#output

#[1, 3, 5]
  
#############

programming_languages = ["JavaScript","Python","Java","Python","C++","Python"]

python_indices  = [index for (index, item) in enumerate(programming_languages) if item == "Python"]

print(python_indices)

#[1, 3, 5]


