# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword argument

def hello(**kwargs): # any word can work don't forget(**)
    #print("Hello "+ kwargs['first] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")
        
hello(title="Mr.",first="Clinton",middle="Dude",last="Nyakoe")