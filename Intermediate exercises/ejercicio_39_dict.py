#function to add a new key/value in an existing dictionary
# help(dict)

def add_element(value,key,dictionary):
    dictionary.update({value:key}) #Add a new tuple in the dictionary
    return dictionary
print(add_element('baptiste',29,{'julien':14,'laurent':13}))
print(add_element('peso',65.3,{}))
