# str.format() = optional method that gives users
#                 more control when displaying output

animal = "cow"
item = "moon"

# print("The "+animal+" jumped over the "+item) 

# print("The {} jumped over the {}".format(animal, item))   # also you can use the variable values
# print("The {1} jumped over the {0}".format(animal, item))   
# print("The {animal} jumped over the {item}".format(animal = "cow", item="moon"))   #using keyword argument

# print("The {1} jumped over the {1}".format(animal, item))   positional argument

# text = "The {} jumped over the {}"
# print(text.format(animal, item))

name = "Clinton"
print("Hello, my name is {}".format(name)) #adding padding to any side of the text
# print("Hello, my name is {:10}. Nice to meet you".format(name)) 
print("Hello, my name is {:<10}. Nice to meet you".format(name))  #left aligning the text.
print("Hello, my name is {:>10}. Nice to meet you".format(name))  #The name is going to be right aligned
print("Hello, my name is {:^10}. Nice to meet you".format(name)) #centering the name

#formatting numbers
# number = 3.14159
number = 1000

print("The number is {:.2f}".format(number)) #displays the number in 2 signifincant figures
print("The number is {:,}".format(number)) #displays the number with a comma
print("The number is {:b}".format(number)) #displays the number as a binary number
print("The number is {:o}".format(number))  #displays an octal number
print("The number is {:X}".format(number)) #displays a hexadecimal number
print("The number is {:E}".format(number)) #displays the scientific notation of the number