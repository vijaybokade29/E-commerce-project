# string = "python is AWesome."
# capitalized_string = string.capitalize()
# print('Old String: ', string)
# print('Capitalized String:', capitalized_string)

# string = "Python is awesome"
# new_string = string.center(24,'0')
# print("Centered String: ", new_string)

# string = "PYTHON ISß AWESOME"
# # print lowercase string
# print("Lowercase string:", string.casefold())


# string = "PYTHON ISß AWESOME"
# # print lowercase string
# print("Lowercase string:", string.lower())

# # define string
# string = "Python is awesome, isn't it?"
# substring = "is"
# count = string.count(substring)
# # print count
# print("The count is:", count)
# count = string.count(substring,8)
# # print count
# print("The count is:", count)

# text = "Python is easy to learn."
# result = text.endswith('n', 0,(6))

# # returns False
# print(result)
# result = text.endswith('to learn.')
# # returns True
# print(result)
# result = text.endswith('Python is easy to learn.')
# # returns True
# print(result)

# str = 'xyz\t12345\tabc'
# # no argument is passed
# # default tabsize is 8
# print(len(str))
# result = str.expandtabs()
# print(len(result))

# quote = 'Let it be, let it be, let it be'
# # first occurance of 'let it'(case sensitive)
# result = quote.find('let it',12)
# print("Substring 'let it':", result)

# # find returns -1 if substring not found
# result = quote.find('small')
# print("Substring 'small ':", result)

# # How to use find()
# if (quote.find('be,') != -1):
#     print("Contains substring 'be,'")
# else:
#     print("Doesn't contain substring")
    
# # default arguments
# print("Hello {}, your balance is {}.".format("Adam", 230.2346))

# # positional arguments
# print("Hello {0}, your balance is {1}.".format("Adam", 230.2346))

# # keyword arguments
# print("Hello {name}, your balance is {blc}.".format(name="Adam",blc=230.2346))

# # mixed arguments
# print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))

string = "hello\tworld"
print(string.expandtabs(6),len(string.expandtabs(6)))

# sentence = 'Python programming is fun.'
# result = sentence.index('is fun')
# print("Substring 'is fun':", result)

# result = sentence.index('Java')
# print("Substring 'Java':", result)


# len()

# Example for string method: partition()
string = "helloworld naira"
print(string.partition(' '))  # Output: ('hello', ' ', 'world')