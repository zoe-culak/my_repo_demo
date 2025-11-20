#Zoe Culak
def not_string(str):
    """
    Given a string, return a new string where "not" has been added to the front.
    However, if the string already begins with "not", return the string unchanged.
    not_string("cat") returns "notcat"
    not_string("not") returns not
    """
    if (str.startswith("not")):
        return str
    else:
        return "not"+str

def swap(lst):
    """
    Given a list, find the minimum element in the list and swap it with the first
    element in the list. Return the list.
    swap([5,4,3,2,1]) returns [1, 4, 3, 2, 5]
    """
    min=lst[0]
    pos=0
    for i in range(len(lst)):
        if lst[i]<min:
            min=lst[i]
            pos=i
    lst[pos]=lst[0]
    lst[0]=min
    return lst

def count_spaces(string):
    """
    Use comprehension to count the number of spaces in a string.
    *** Important: your code must use comprehensions and should not be more than
    two lines of code including the return statement ***
    count_spaces("the cow jumped over the moon") returns 5
    """
    spaces=[i for i in string if i==" "]
    return len(spaces)
    
def sum67(nums):
    '''
    Return the sum of the numbers in the array, except ignore sections 
    of numbers starting with a 6 and extending to the next 7 
    (every 6 will be followed by at least one 7). 
    Return 0 for no numbers.
    sum67([1, 2, 2]) → 5
    sum67([1, 2, 2, 6, 99, 99, 7]) → 5
    sum67([1, 1, 6, 7, 2]) → 4
    '''
    sum=0
    skip=False
    for num in nums:
        if skip:
            if num==7:
                skip=False
            continue
        if num==6:
            skip=True
        else:
            sum+=num
    return sum

def minmaxdiff(nums):
    """
    Given an array length 1 or more of ints, return the difference between the largest
    and smallest values in the array.
    minmaxdiff([1,2,3,4,5]) returns 4
    """
    min=nums[0]
    max=nums[0]
    for num in nums:
        if num<min:
            min=num
        if num>max:
            max=num
    return max-min

print('not_string("cat") expected: notcat')
print('not_string("cat") actual:', not_string("cat"))

print('swap([5,4,3,2,1]) expected: [1, 4, 3, 2, 5]')
print('swap([5,4,3,2,1]) actual:',swap([5,4,3,2,1]))

print('count_spaces("the cow jumped over the moon") expected: 5')
print('count_spaces("the cow jumped over the moon") actual:', count_spaces("the cow jumped over the moon"))

print('sum67([1, 2, 2, 6, 99, 99, 7]) expected: 5')
print('sum67([1,2,2]) actual:', sum67([1, 2, 2, 6, 99, 99, 7]))

print('minmaxdiff([1,2,3,4,5]) expected: 4')
print('minmaxdiff([1,2,3,4,5]) actual:',minmaxdiff([1,2,3,4,5]))