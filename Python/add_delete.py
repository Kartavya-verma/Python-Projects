user_info={
    "name":"harshit",
    "age":24,
     "fav_movies":["coco","kimi no na wa"],
     "fav_tune":["awakening","fairy tail"],
}

user_info["fav_songs"]=["song1","song2"]
print(user_info)

popped_item=user_info.pop("fav_tune")
print("popped item is {}".format(popped_item))
print(user_info)

popped_item=user_info.popitem()
print(popped_item)
print(user_info)