'''LeetCode #20: Valid Parentheses'''

class Solution:
    def isValid(self, s: str) -> bool:
        opcl = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        cl = [char for char in opcl.values()]
        if s[0] in cl:
            return False
        stack = []
        for char in s:
            if not char in cl:
                stack.append(char)
            elif stack and opcl[stack[-1]] == char:
                del stack[-1]
            else:
                return False
        if stack != []:
            return False
        return True

'''
I thought of it in steps first, so in a loop, check:
Is it a closing bracket?
No? -> add it to a 'stack' list
Yes? -> check the last added element in a list, if it is the closing of the bracket that should end first? Yes: Delete that one, No: return False

when the loop ends, you will have two situations, 1: the stack is not empty so in strings like "[", it is added in stack but since it is not closed, it is not removed either, so that makes for a good and very smart check.
2: if stack is empty, and if the control escaped the loop, then it's all well completed

In essence this problem would have two main errors:
1: a bracket opens, does not close
2: a bracket opens, does not close properly; so it either closes after someone else opens
3: a bracket closes, opens never existed (the stack[-1] check cleans this too)

and yeah, you made this algorithm with 0 help, my guy


My word:
I actually felt it was stack, then had to check the topics to confirm if it was not something complicated...

Cause my very first intuition was creating a opening and closing list, and then compare them likewise, but that did not make sense to me the more I thought.
I thought of a table, I needed a table, but then I thought a dict should work here too... and then when I actually wrote, I realized that I did not have to compare it as semantically as I thought I would ahve to- like with variables such as 'closing, opening' and all... I simply had to compare the positions of the values with keys...

Actuallyit was this one example which helped me imagine what I am actually chasing-
Example 5:

Input: s = "([)]"

Output: false

And then I went ahead and got two submission errors, one was not checking if a stack is empty, the second was when I did not check if stack is empty inside the loop
'''