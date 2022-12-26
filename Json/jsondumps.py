#Use the sort_keys parameter to specify if the result should be sorted or not:
json.dumps(x, indent=4, sort_keys=True)

#Use the separators parameter to change the default separator:
json.dumps(x, indent=4, separators=(". ", " = "))


