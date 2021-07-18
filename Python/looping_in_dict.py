user_info={
    "name":"harshit",
    "age":24,
     "fav_movies":["coco","kimi no na wa"],
     "fav_tune":["awakening","fairy tail"],
}

'''if "name" in user_info:
    print("present")
else:
    print("not present")

if "harshit" in user_info.values():
    print("present")
else:
    print("not present")'''

for i in user_info.values():
    print(i)

user_info_values=user_info.values()
print(user_info_values)

user_info_keys=user_info.keys()
print(user_info_keys)

for i in user_info:
    print(user_info[i])

user_items=user_info.items()
print(user_items)

for key,value in user_info.items():
    print("Key is {} and value is {}".format(key,value))