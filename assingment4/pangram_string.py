# Write a Python function to check whether a string is a pangram or not.
def panagram(string):
    alphabet_set=set('abcdefghijklmnopqrstuvwxyz')
    
    is_input=set(string.lower())
    
    return alphabet_set.issubset(is_input)
    
    
string="i am sunny from rajampeta"
print(panagram(string))

