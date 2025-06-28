# The code from the book is intended to be ran in IDLE;
# But I'm doing this as exercises, so it will be done here and 
# with some additions to the book to just play around

print('Hello World')
myName = input('Enter Your Name: ')
print('Hello ' + myName)
print('The length of your name is:' )
print(len(myName))
myAge = input('What is your age?: ')
print('You are ' + myAge + ' years old?')

## Here is where i add some fun of my own ##
daysInYear = 365
daysOld = daysInYear * int(myAge)
print('You\'re roughly ' + str(daysOld) + 'Days old.' )