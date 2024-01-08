# text = "Yoooooo\n This is some text\nHave a nice day!"
text = "Have a great day! See ya"


with open('test-write.txt', 'a') as file:  # a for append
    file.write(text)