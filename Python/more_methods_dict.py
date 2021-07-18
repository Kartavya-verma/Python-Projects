d={"name":"unknown","age":"unknown","height":"unknown"}

#d=dict.fromkeys(["name",'age',"height"],"unkonwn")
#print(d)

print(d.get("name"))

if d.get("name"):
    print("present")
else:
    print("not present")

#print(d.clear())

d1=d.copy()
print(d1)