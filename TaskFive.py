"""
Author : G Gopi Kumar
Date : 31/01/2024

Program 1 : What is the expected output of the following Python code given below :-

data = (10, 501, 22, 37, 100, 999, 87, 351]
result filter (lambda x: x > 4, data)
print (list (result))

Logic : Here We are Trying to Filter the Given List and Print the List Values which are greater than 4 only . 
And in the Given List all values are greater than 4 so the :

Expected Output is [10, 501, 22, 37, 100, 999, 87, 351]

"""

"""
Author : G Gopi Kumar
Date : 31/01/2024

Program 2 : Write a Python code using Lambda function to check every element of a List is an Integer or String ?

Logic : Here We have taken a List which contains multiple String and Integar Value , and in the Lambda function we are checking 
the instance of with the help of isinstance and integrating it with the help of map and finally printted the result

"""
#Positive Test case :

data = [1234, 'CrazyDay', 7234697, 'vishu', "Radha"]
#The below function is used to check whether each element in the list data is an instance of either int or str
result = list(map(lambda x: isinstance(x, (int, str)), data))
#Print the List Result , which will provided the output as true or false or the each element 
print(result)

#Negative Test case :

data = [1234, 37.5 , 7234697, True , 83.7777]
#The below function is used to check whether each element in the list data is an instance of either int or str
result = list(map(lambda x: isinstance(x, (int, str)), data))
#Print the List Result , which will provided the output as true or false or the each element 
print(result)

"""
Author : G Gopi Kumar
Date : 31/01/2024

Program 3 :  Using the Python Lambda function create a Fibonacci series from 1 to 50 elements ?

Logic : Here i have taken the List with first two elements and then in Lambda function append the next value of the series by 
adding last two elements with the help of for loop iterated for 50 elemets
"""
result = [0, 1]

# Define a lambda function to append the next Fibonacci number to the list
fibo = lambda n: [result.append(result[-1] + result[-2]) for i in range(n-2)]

# Call the lambda function with n=10, appending the next eight Fibonacci numbers to the list
fibo(50)

# Print the final result stored in the 'result' list
print(result)

"""
Author : G Gopi Kumar
Date : 31/01/2024

Program 4 :  Write a Python function to validate the Regular Expression for the following:-
a.) Email Address
b.) Mobile numbers of Bangladesh
c.) Telephone numbers of USA
d.) 16 character Alpha-Numeric password composed of alphabets of Upper Case, Lower Case, Special Characters, Numbers
Logic : 

"""
import re

def validate_email(email):
    #Partten Characters Before @ are Alphanumeric and Characters After @ are Alphanumeric till . and then 
    #domain is only Alphabet with size restriction from
    email_pattern = "^[a-zA-Z0-9.]+@[a-zA-Z0-9.-]+.+[a-zA-Z]{2,6}$"
    return bool(re.match(email_pattern, email))

def validate_bangladesh_mobile_number(mobile_number):
    """
    Typical format for a mobile phone number
    is 01XXX NNNNNN, e.g. 01054 694200 when dialed inside Bangladesh, and +880 1XXX NNNNNN when dialed internationally
    here we will do as internationally so first five digits +8801 and remaing 9 characters can be numbers
    """
    mobile_pattern = "^[+8801]{5}[0-9]{9}$"
    return bool(re.match(mobile_pattern, mobile_number))

def validate_usa_telephone_number(telephone_number):

# First two didits is +1 and others can be number 
    usa_telephone_pattern = "^[+1]{2}[0-9]{10}$"
    return bool(re.match(usa_telephone_pattern, telephone_number))

# Password must be greater than 3 and must be alpha numeric 
def validate_alpha_numeric_password(password):
    password_pattern = "^[a-zA-Z0-9]{3,}$"
    return bool(re.match(password_pattern, password))

# Examples of usage:
email = "gopiremo619@gmail.com"
mobile_number = "+8801712345678"
telephone_number = "+14081234582"
alpha_numeric_password = "Abcdefg12"

print(validate_email(email))  # True
print(validate_bangladesh_mobile_number(mobile_number))  # True
print(validate_usa_telephone_number(telephone_number))  # True
print(validate_alpha_numeric_password(alpha_numeric_password))  # True





