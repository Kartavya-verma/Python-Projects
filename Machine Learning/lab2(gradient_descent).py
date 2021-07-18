curr_x = 3
lr = 0.01
precision = 0.000001
rate_of_change_of_x = 1
max_iteration = 10000   #if something trapped between local minima
iter = 0

gradient = lambda x: 2*(x+5)

# training mein loop lagta hai
while rate_of_change_of_x > precision and iter < max_iteration:
    prev_x = curr_x
    curr_x = curr_x - lr*gradient(prev_x)  #to remove ambiguity we use prev x
    rate_of_change_of_x = abs(curr_x - prev_x) # this value may be -ve therefore we use abs
    iter  += 1
    print("Iteration",iter,"Value of X is",curr_x)
print("The global minima occurs at ",curr_x)