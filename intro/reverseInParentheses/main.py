def reverse(list_: list) -> list:
    list_ = list_[::-1]
    for i in range(len(list_)):
        if list_[i] == '(':
            list_[i] = ')'
        elif list_[i] == ')':
            list_[i] = '('
    return list_

def reverseInParentheses(inputString: str) -> str:
    inputString = list(inputString)
    count = 0
    i = 0
    while i < len(inputString):
        if inputString[i] == '(':
            if count == 0:
                start = i
            count += 1
        if inputString[i] == ')':
            count -= 1
            if count == 0:
                end = i
                inputString = inputString[:start]+reverse(inputString[start+1:end])+inputString[end+1:]
        i += 1
    outputString = ''.join(inputString)
    if '(' in inputString:
        return reverseInParentheses(outputString)
    else:
        return outputString