import time

print(time.ctime(0)) # convert a time expression in seconds since epoch to a readable string
#                     # epoch = when your computer thinks time began (reference point)

# print(time.ctime(1000000))
# print(time.time()) # return current seconds since epoch

# print(time.ctime(time.time())) current time

# time_object = time.localtime()
# print(time_object)
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)
# time_string = "20 April, 2021"

# time_object = time.strptime(time_string, "%d %B, %Y")
# print(time_object)

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)
