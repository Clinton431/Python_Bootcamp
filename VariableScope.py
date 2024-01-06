# scope = The region that a variable is recognized
#           A variable is only available from inside the region it is created.
#           A global and locally scoped versions of a variable can be created


name = "Clinton"  # global scope

def display_name():
    name = "Nyakoe"   # local scope
    print(name)
    
display_name()
print(name)