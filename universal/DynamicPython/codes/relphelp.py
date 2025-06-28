'''
#Write a function inject_variable(varname, value) that takes a string varname and assigns value to it globally using exec.

def inject_variable(varname, value):

    exec(f"{varname} = {value}", globals())

inject_variable("Hello", 412)
print(Hello)
'''

'''
#Function injection
# Create a tstring represting a full function and define it in the global scope using exec

#injection
code = """
def greet(name):
    return f'Hello, {name}'
"""

def inject_function(code):
    exec(f"{code}", globals())

inject_function(code)

print(greet("victor"))

#note that this is dangerous because you can pass exec a malicious code (literal injection). here, though, we are giving it our own code (and not user input)
'''
'''
# Global state
env = {}

# Inside a loop, define and update a counter stored in env using exec
# Then print it each time
# Expected output: 1, 2, 3, ...

for i in range(10):
    exec(f"counter = {i}", env)
    print(env['counter'], end=', ')
'''

#exec sandbox

safe_env = {"__builtins__": {"print": print, "len" : len, "str": str}}

def space(code):
    exec(code, safe_env)

code = '''
print(str("Hello!"))
print(int(3))
'''

space(code)