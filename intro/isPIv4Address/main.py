def isIPv4Address(inputString: str) -> bool:
    input_numbers = inputString.split('.')
    if len(input_numbers) == 4:
        for number in input_numbers:
            try:
                if int(number) not in range(0,255+1) :
                    return False
            except ValueError:
                return False
        return True
    return False