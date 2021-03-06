# O(n) time | O(n) space
def checkBalancedBrackets(string):
    openingBrackets='({['
    closingBrackets=')}]'
    mapping={')':'(','}':'{',']':'['}
    stack=[]
    for char in string:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if len(stack)==0:
                return False
            if mapping[char]==stack[-1]:
                stack.pop()
            else:
                return False
    return len(stack)==0

print(checkBalancedBrackets('[((){})]'))