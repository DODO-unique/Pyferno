# print n binary string 

def generate_binary(n):
    res = []

    def backtrack(path):
        if len(path) == n:
            # for string in path:
            #     if string.count('(') == string.count(')'):
                res.append("".join(path))
            return
        
        
        for bit in ["(", ")"]:
            path.append(bit)
            backtrack(path)
            path.pop()

    backtrack([])
    return res

print(generate_binary(6))