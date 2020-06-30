# 23rd of May, 2020
# Saturday
# multiplication persistence of a number
def per(n):
    if len(str(n)) == 1:
        print(n)
        return "done"
    digits = [int(x) for x in str(n)]

    result = 1
    for items in digits:
        result = result * items
    print(result)
    per(result)

'''
start_num = a
number of terms = l
sqnce = [a,a^2, (a^2)^4....]
for i in range (l):
    a = a^2
    sqnce.append(a)
'''

# printing out series where every other term is a square of the previous one
def square_series(a, l):
    sqnce = []
    sqnce.append(a)
    for i in range(l-1):
        a = a**2
        sqnce.append(a)
    return sqnce


'''
number of bits = a
list = []
for i in range (0, a):
    items = 2^i
    list.append(items)
'''

# printing out 2^n sereis
# Problem: infinite loop at the moment
def binary_series(a):
    array = []
    j = False
    while j == False:
        if int(a) < 0:
            print("Please positive values only")
            j==False
        else:
            for i in range(a):
                items = 2**i
                array.append(items)
                j == True
    return array

# printing out the geometric series for the given data
def geometric_series(a, r, l):
    array = []
    i = 1
    for i in range(l+1):
        items = a*r**(i-1)
        array.append(items)
    array.pop(0) # every time i run a 1 is added so to get rid of that
    return array

# printing out the arithmetic series for the given data.
def arithmetic_series(a, d, l):
    array=[]
    for i in range(l):
        elements = a + (d * i)
        array.append(elements)
    return array
