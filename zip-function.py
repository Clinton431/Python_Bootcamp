#zip(*iterables) = aggregate elements from two or more iterables (lists, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ["Clinton", "Dude", "Mister"]
passwords = ("p@ssword", "abcd123", "guests")

login_date= ["1/1/2021","1/3/2023","1/2/2023"]
users = zip(usernames,passwords,login_date)

for i in users:
    print(i)

# users = dict(zip(usernames, passwords))

# print(type(users))

# for key,value in users.items():
#     print(key+" : "+value)