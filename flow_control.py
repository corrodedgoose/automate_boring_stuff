# Chapter 2 of Automating the Boring Stuff with Python
# Flow Controls
# This covers conditions, loops, booleans, Modules.
# These are also suppose to be ran in IDLE

seperator = '============='
spam = True
x = spam == 2 + 2
print(x)
print(seperator)
print( 42 == 42)
print(seperator)
print( 2 != 3)
print(seperator)
print('hello' == 'Hello')
print(seperator)
print('dog' != 'cat')
print(seperator)
print(42 == '42')
print(seperator)

name = 'Mary'
password = 'swordfish'

if name == 'Mary':
    print('Hello ' + name)
    if password == 'swordfish':
        print('Access Granted')
else:
    print('Wrong Password')