__new__ comes first when a function is called- this is the true constructor, the second function is __init__ which initializes by assigning attributes.
so you can do this in your code:
class Trickster:
    def __new__(cls):
        print("haha nope, you get a dict")
        return {}
    def __init__(self):
        print("you’ll never see this")

This gives output of:
t = Trickster()
print(type(t))  # dict 

A rabbit hole: Want me to show you what happens if you half-return a dict but still let Python think it’s a Trickster (so repr lies)?