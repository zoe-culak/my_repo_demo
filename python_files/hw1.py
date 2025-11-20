# Zoe Culak
# used https://www.geeksforgeeks.org/python/python-string-methods/ to look at string methods to use for the samesunmoon function

def last_4_doubled(string):
    """
    Given a string, return a new string made of 2 copies of the last 4 characters of the original string.
    The string length will be at least 4.
    """
    str=string[-4:len(string)]*2
    return str

def has_789(nums):
    """
    Given an list of ints, return True if the sequence of numbers
    7, 8, 9 appears in the list somewhere. 7, 8, 9 must occur in order.
    """
    for i in range(len(nums)):
        if nums[i:i+3]==[7, 8, 9]:
            return True
    return False

def count_x_o(string):
    """
    Return the number of times that the string "x-o" appears anywhere in the given string,
    except we'll accept any character for the '-', so "xao", "xbo", etc. count.
    """
    count=0
    for i in range(len(string)):
        if string[i]=='x' and string[i+2]=='o':
            count+=1
    return count

def samesunmoon(string):
    """
    Return True if the string "sun" and "moon" appear the same number of times in the given string.
    *** This can be simplified using a Python string method ***
    """
    if string.count("sun")==string.count("moon"):
        return True
    return False

def trimmed_average(nums):
    """
    Return the "trimmed" average of a list of ints, which is the mean average of the
    values, except ignoring the largest and smallest values in the list. If there are
    multiple copies of the smallest value, ignore just one copy, and likewise for the largest value.
    Use floor division to produce the final average. You may assume that the list is length 3 or more.
    """
    min=nums[0]
    max=nums[0]
    total=0
    for num in nums:
        if num<min:
            min=num
        if num>max:
            max=num
    for num in nums:
        if num!=max and num!=min:
            total+=num
    return total/(len(nums)-2)


# Test functions - Do not modify these.
assert last_4_doubled("HelloThere") == 'herehere', 'last_4_doubled("HelloThere") expected ereere'
print("Test 1 for last_4_doubled passed")
assert last_4_doubled("abcdefgh") == 'efghefgh', 'last_4_doubled("abcdefgh") expected efghefgh'
print("Test 2 for last_4_doubled passed")
assert last_4_doubled("ComputerScience") == 'enceence', 'last_4_doubled("ComputerScience") expected enceence'
print("Test 3 for last_4_doubled passed")
print("-" * 20)

assert has_789([7, 7, 8, 9, 7]) is True, '[7, 7, 8, 9, 7] has 789'
print("Test 1 for has_789 passed")
assert has_789([7, 7, 8, 1, 9]) is False, '[7, 7, 8, 1, 9] does not have 789'
print("Test 2 for has_789 passed")
assert has_789([7, 7, 8, 7, 8, 9]) is True, '[7, 7, 8, 7, 8, 9] has 789'
print("Test 3 for has_789 passed")
print("-" * 20)

assert count_x_o("x-ox_ox.o") == 3, 'x-ox_ox.o has 3'
print("Test 1 for count_x_o passed")
assert count_x_o("xxox.o") == 2, 'xxox.o has 2'
print("Test 2 for count_x_o passed")
assert count_x_o("xrooo") == 1, 'xrooo has 1'
print("Test 3 for count_x_o passed")
print("-" * 20)

assert samesunmoon("sunmoon") is True, 'sunmoon has same sun/moon count'
print("Test 1 for samesunmoon passed")
assert samesunmoon("sunlightmoon") is True, 'sunlightmoon has same sun/moon count'
print("Test 2 for samesunmoon passed")
assert samesunmoon("sunmoonmoon") is False, 'sunmoonmoon does not have same sun/moon count'
print("Test 3 for samesunmoon passed")
print("-" * 20)

assert trimmed_average([1, 2, 3, 4, 100]) == 3, 'average [1, 2, 3, 4, 100] is 3'
print("Test 1 for trimmed_average passed")
assert trimmed_average([1, 1, 5, 5, 10, 8, 7]) == 5, 'average [1, 1, 5, 5, 10, 8, 7] is 5'
print("Test 2 for trimmed_average passed")
assert trimmed_average([-10, -4, -2, -4, -2, 0]) == -3, 'average [-10, -4, -2, -4, -2, 0] is -3'
print("Test 3 for trimmed_average passed")
print("-" * 20)
print("All tests passed! Great job!")