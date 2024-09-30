# Original terms
glossary = {
    'argument': 'a value passed to a function/method when called', 
    'f-string': 'a string in which "f" precedes it, allowing for '
    'replacement fields', 
    'function': 'statements that return a value to a caller', 
    'list': 'a Python sequence akin to an array', 
    'slice': 'an object containing a part of a sequence'
    }

# Additional terms
glossary['statement'] = 'a(n) expression/construct part of a block of code'
glossary['text file'] = 'a file object that can read and write str objects'
glossary['Zen of Python'] = '''a list of Python design principles and \
philosophies'''
glossary['callback'] = '''a subroutine function passed to an argument to be \
executed in the future'''
glossary['class'] = 'a template for creating user-defined objects'

# Display
print("--  Python Glossary  --\n")
for word, meaning in glossary.items():
    print(f"{word}: {meaning}")