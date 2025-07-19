import dis

def climb_trash():
    food = "mango peel"
    return food

def main():
    raccoon = "Victor"
    snack = climb_trash()
    print(snack)

dis.dis(main)