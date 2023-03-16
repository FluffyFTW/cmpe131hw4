
def palindrome(inp):
    while(len(inp) > 1):
        print(f"comparing {inp[-1]} and {inp[0]}")
        if(inp[-1] == inp[0]):
            inp.pop(-1)
            inp.pop(0)
        else:
            return False
    return True