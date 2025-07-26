'''
#Task 1: Perform Basic Mathematical Operations
#1.  Takes two numbers as input from the user.
first = float(input('Enter the first number: '))
second = float(input('Enter the second number: '))

#2.  Performs the basic mathematical operations on these two numbers:
add = first+second
sub = first-second
mul = first*second
div = first/second

#3.  Displays the results of each operation on the screen.
print('Addition: \t',add,'\nSubtraction: \t',sub,'\nMultiplication: \t',mul,'\nDivision: \t',div)
'''


#Task 2: Create a Personalized Greeting
#1.  Takes a user's first name and last name as input.
fname = input('Enter your first name: ')
lname = input('Enter your last name: ')

#2.  Concatenates the first name and last name into a full name.
fullName = fname + ' ' + lname

#3.  Prints a personalized greeting message using the full name.
print('Hello, ', fullName , '! Welcome to the Python program.')