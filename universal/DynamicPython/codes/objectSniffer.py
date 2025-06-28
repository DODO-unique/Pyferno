def sniff(obj):
    """
    For any object passed:
    - Print its type, class, module
    - Print its __dict__ (if any)
    - List all callable methods (dunder and public)
    - Dynamically add a `.sniffed = True` attribute if mutable
    - Return a summary dict
    """

    # printing its type, class and module
    data_type = type(obj)
    class_name = obj.__class__
    module = type(obj).__module__
    print(data_type, class_name, module)

    #print its dictionary
    attributes = type(obj).__dict__
    print(attributes)

    # print all callable methods
    all_callable_methods = dir(obj)
    print(all_callable_methods)

    try:
        setattr(obj, ".sniffed", True)
    except:
        print("Not mutable or other error")
    
    hlep = help(obj)
    print(hlep)

    # summary:
    summary = {
        "type" : data_type,
        "class" : class_name,
        "module" : module,
        "attributes" : attributes,
        "Callable methods" : all_callable_methods,
        "was sniffed" : hasattr(obj, "sniffed")
    }

    return summary

example = "hello raccoon boi at 4:41 AM"

print (sniff(example))

'''
Notes of what we learned new here:
    1. Apparently some dunders only work on class, so you gotta specify what class to search for, and to be more specific what method to search for. 
    2. Meaning, __dict__ and __module__ don't work for objects, they work for classes
    3. Note that __mod__ and __module__ is different thing, and apparently __mod__ does not need to work on class
    4. dir() gives all methods, for callable filter through callable(getattr(obj, name, None))
    5. if no such attribute found then whatever is written in the default of getattr will be returned instead of a AttributeError
'''