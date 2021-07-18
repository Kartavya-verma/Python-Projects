from itertools import combinations


def checkIfDuplicates_1(listOfElems):
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

def sub_lists(my_list):
    subs = []
    c = 0
    for i in range(0, len(my_list)+1):
        temp = [list(x) for x in combinations(my_list, i)]
        if len(temp) > 0:
            subs.extend(temp)
    for j in subs:
        res = checkIfDuplicates_1(j)
        if res:
                print(j)
                c += 1
                print(c)
    # return subs

l1 = [2, 2, 3, 3, 5]
# print(sub_lists(l1))
sub_lists(l1)