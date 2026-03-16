#Python List - ordered,mutable,zero based index
#retreive using index
cities = ['Los Angeles', 'London', 'Tokyo']
print(cities[0])
print(cities[-1])#Negative index
developer = 'Jessica'
print(list(developer)) #list constructor
names = []
names.append(developer)
print(names)
#len
numbers = [1, 2, 3, 4, 5]
print(len(numbers)) # 5
print(len(cities))
#Update - Mutable
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print(programming_languages) # ['JavaScript', 'Java', 'C++', 'Rust']
developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer) # ['Jane Doe', 'Python Developer']
print('Rust' in programming_languages) # True
print('JavaScript' in programming_languages) # False

#Nested List
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
print(developer[2][1]) # Rust

developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer
print(name, age, job)

#Slicing
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie']
desserts[1:3] # ['Cookies', 'Ice Cream']
numbers = [1, 2, 3, 4, 5, 6]
numbers[1::2] # [2, 4, 6]

#List Methods
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) # [1, 2, 3, 4, 5, 6]

numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)
print(numbers) # [1, 2, 2.5, 3, 4, 5]

numbers = [1, 2, 3, 4, 5, 5, 5]
numbers.remove(5)
print(numbers) # [1, 2, 3, 4, 5, 5]

numbers = [1, 2, 3, 4, 5]
numbers.pop(1) # The number 2 is returned
#If you don't specify an element for the pop method, then the last element is removed

numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)

numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()
print(numbers) # [1, 2, 19, 35, 41, 67]


numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)
print(sorted_numbers) # [1, 2, 19, 35, 41, 67]
print(numbers) # [19, 2, 35, 1, 67, 41]
#sorted(): A built-in function that returns a new sorted list instead of modifying the original list:

numbers = [6, 5, 4, 3, 2, 1]
numbers.reverse()
print(numbers) # [1, 2, 3, 4, 5, 6]

programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('Java') # 1


#Create a list squares which has the squares of the numbers in i.
input_list = [4, 5, 2, 4, 2, 3, 5, 1]

squares = [n**2 for n in input_list]
print(squares)

#You are given a list of integers. Your task is to remove all duplicate values and return a list with only unique elements, preserving the original order.
def dup_check(input_list):
    result = []
    for num in input_list:
       if num not in result:
            result.append(num)
    return result
        
print(dup_check(input_list))

##Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
str1 = "PyNaTive"
#Expected Output: yaivePNT
lower = []
upper = []
for chr in str1:
    if chr.islower():
        lower.append(chr)
    else:
        upper.append(chr)
    result = "".join(lower+upper)
print(result)

#Write a Python function called find_common_elements that takes in two lists of integers as input and returns a new list containing the common elements between the two input lists. If there are no common elements, the function should return an empty list. Your task is to implement this function and test it with sample inputs.
 
# Test cases
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
def find_common_elements(list1, list2):
    result = []
    for num in list1:
        if num in list2:
            result.append(num)
    return result
        
print("Common elements:", find_common_elements(list1, list2))  # Output should be [4, 5]
