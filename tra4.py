

#this function will count the occurrences of same element from an iterable list / array

def counter(item):
    counts = {}
    for i in item:
        counts[i] = counts.get(i, 0) + 1
    return counts

#this function will compare the list and find the mode of said list 
def compare(low, high):
    data = x
    mode = dict(data)       
    print(mode)
    mode = [num for num, item in mode.items() if item == max(list(data.values()))]
    if len(mode) == a:
        mode = "no mode"
        print(mode)
    else:
        str_mode = str(mode).lstrip('[').rstrip(']')
        print("The mode is : {}".format(str_mode))


A=[1,1,2,3,2,4,1,2]
a = len(A)
A.sort()
start = A[0]
end = A[-1]
x = counter(A)
compare(start, end)

