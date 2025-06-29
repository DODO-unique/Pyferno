import re

def variable_name(s):
    pattern = r'^[a-zA-Z_]\w*'
    return bool(re.fullmatch(pattern, s))

def zip_code(s):
    pattern = r'\d{5}'
    return bool(re.fullmatch(pattern, s))

def email(s):
    pattern = r'^[\w\.-]+@[\w\.-]+\.(com|org|net)'
    return bool(re.fullmatch(pattern, s))

def hashtags(s):
    pattern = r'#\w+'
    return re.findall(pattern, s)

text = "Learning #Python3 is fun! #regex_power 💥 #100DaysOfCode!"

print(hashtags(text))

def apostrophe(s):
    pattern = r'[\w](?<=\w)\'(?=\w)'