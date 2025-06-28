'''#Write a function inject_variable(varname, value) that takes a string varname and assigns value to it globally using exec.

def inject_variable(varname, value):

    exec(f"{varname} = {value}", globals())

inject_variable("Hello", 412)
print(Hello)
'''

'''#Function injection
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
'''# Global state
env = {}

# Inside a loop, define and update a counter stored in env using exec
# Then print it each time
# Expected output: 1, 2, 3, ...

for i in range(10):
    exec(f"counter = {i}", env)
    print(env['counter'], end=', ')
'''
"""#exec sandbox

safe_env = {"__builtins__": {"print": print, "len" : len, "str": str}}

def space(code):
    exec(code, safe_env)

code = '''
print(str("Hello!"))
print(int(3))
'''

space(code)
"""

'''# Global state
env = []

# Inside a loop, define and update a counter stored in env using exec
# Then print it each time
# Expected output: 1, 2, 3, ...

for i in range(10):
    exec(f"counter = {i}", env)
    print(env)'''
# So exec() globals must be dictionaries
'''code = """
x = 10
y = 20
z = x + y
"""
# Use compile and exec on this
execCode = compile(source=code, filename='test', mode="exec")
print(type(execCode))

env={}
exec(execCode, env)

print(env['z'])
'''
'''Write a REPL that:
    -takes input
    -compiles it using mode='eval'
    -evaluates it using custom globals
'''
'''expression = input(">>>")
# no equals sign work here

compiled_code = compile(expression, 'evaluating', "eval")
env={}

print(eval(compiled_code, env))
print(env)
'''
"""def test():
    '''So exec() naturally assigns the numbers to gloabl symbol table, 
    when python interpreter to be precise the PVM, sees x in the stream, it firs checks x as Local, 
    but since it is not local, it gives an NameError. 
    SO the solution here would be to store that expression in local group
    I did this by creating a local dict first then loading it to locals'''
    env={}
    exec("x = 123", globals=None, locals=env)
    print(env['x'])
test()
"""

# Write a function:
'''
This will use:

compile() to make code object

exec() to inject the function

and retrieve it from the injected globals'''

env={}

def create_function(args_str, body_str):
    name="func"
    code = f'''
def {name}({args_str}):
    {body_str}
    '''
    compiled_code = compile(code, 'test', 'exec')
    # print(compiled_code)
    exec(compiled_code, env)
    return env['func']
# Usage:

f = create_function("a, b", "return a * b")
print(f(4, 5))

# create_function("a, b", "return a * b")
# print(env['func'](4, 5))  # 20
'''
What I did in this example is, I simply switched the name of the local func to whatever the usage wanted
This way, when calling the function was called properly.
I also had to align the sample there neatly for indentation errors
I also had to make sure the env was originally defined in global namespace as written below, 
another thing is, to respect the formats of how you feed your functions what'''


