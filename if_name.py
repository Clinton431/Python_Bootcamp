# Python interprates sets "special variables", one of which is __name__
# Python will assign the __name__ variable a value of '__main__' if it's
# the initial module being run

if __name__ =='__main__':
    print("running this module directly")
else:
    print("running other module indirectly")
print(__name__)
