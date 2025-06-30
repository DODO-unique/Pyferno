'''import re

def variable_name(s):
    pattern = r'^[a-zA-Z_]\w*'
    return bool(re.fullmatch(pattern, s))

def zip_code(s):
    pattern = r'\d{5}'
    return bool(re.fullmatch(pattern, s))

def email(s):
    pattern = r'^[\w\.-]+@[\w\.-]+\.(com|org|net)'
    return bool(re.fullmatch(pattern, s))
'''
'''def hashtags(s):
    pattern = r'#\w+'
    return re.findall(pattern, s)

text = "Learning #Python3 is fun! #regex_power 💥 #100DaysOfCode!"

print(hashtags(text))

def apostrophe(s):
    pattern = r'\b\w+\'\w+\b'
    return re.fullmatch(pattern, s)

text = "I'd say, you're toastin'"

print(apostrophe(text))

#Find all domains from a email:

def domains(ls):
    pattern = r'(?<=@)[\w\.-]+\b'
    result = []
    for s in ls:
        result.append("".join(re.findall(pattern, s)))
    return result

ls = ["alice@gmail.com", "bob@outlook.com", "cat@yahoo.in"]

print(domains(ls))'''

'''def phone_numbers(s):
    #Note a syntax error here that- if you are specifying a number, don't add a + before it for no reason
    # my wrong pattern was: \b[789]\d+{10}, this is wrong on so many plains because you are accepting 10 numbers even though you specified that the number should start with 7, 8 or 9. Also, \d+ suggests 1 or **more** numbers, but then I limit it to 10 is redundant
    pattern = r'\b[789]\d{9}\b'
    # result = []
    return re.findall(pattern, s)

text = "Call me at 9876543210 or at the office 080-12345678. Sometimes 8123456789 works. Avoid 1234567890 or 6000000000."

print(phone_numbers(text))

def text_in_tag(s):
    pattern = r'(?<=>)(.*?)(?=</)'
    return re.findall(pattern, s)

example = '<a href="http://example.com">Visit</a> and <a href="http://test.com">Click here</a>'

print(text_in_tag(example))'''

def link_catcher(s):
    pattern = r''