#numbers=list(range(1,11))
#print(numbers)
#popped_item=numbers.pop()
#print(numbers)
#print(popped_item)

numbers=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,1]

#print(numbers.index(1,11,15))

def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(numbers))