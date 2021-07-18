strs = ["flower", "flow", "flight"]
if len(strs) == 0:
    print("")
prefix = strs[0]
for i in range(1, len(strs)):
    strs[i].startswith(prefix)
    while strs[i].startswith(prefix) == False:
        prefix = prefix[0:len(prefix)-1]
print(prefix)
