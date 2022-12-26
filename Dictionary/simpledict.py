phone_number_lookup = {
    'alice': '555-4321',
    'bob': '555-1234'
}
 
print("Alice's phone number is %s" % phone_number_lookup['alice'])

##################
# creating a new dictionary
my_dict ={"Java":100, "Python":112, "C":11}
 
# one-liner
print("One line Code Key value: ", list(my_dict.keys())
      [list(my_dict.values()).index(100)])

#########################
dic ={"geeks": "A","for":"B","geeks":"C"}

value = {i for i in dic if dic[i]=="B"}
print("key by value:",value)


##########
# creating a new dictionary
my_dict ={"java":100, "python":112, "c":11}

# list out keys and values separately
key_list = list(my_dict.keys())
val_list = list(my_dict.values())

# print key with val 100
position = val_list.index(100)
print(key_list[position])

##############

# function to return key for any value
def get_key(val):
	for key, value in my_dict.items():
		if val == value:
			return key

	return "key doesn't exist"


# Driver Code
my_dict = {"Java": 100, "Python": 112, "C": 11}

print(get_key(100))
print(get_key(11))


