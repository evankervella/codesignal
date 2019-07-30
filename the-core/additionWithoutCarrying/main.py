def additionWithoutCarrying(param1: int, param2: int) -> int:
    param1 = list(str(param1))
    param2 = list(str(param2))
    to_add = max(len(param1), len(param2)) - min(len(param1), len(param2))
    if len(param1) < len(param2):
        param1 = to_add * ['0'] + param1
    elif len(param1) > len(param2):
        param2 = to_add * ['0'] + param2
    result = [int(x)+int(y) for (x,y) in zip(param1,param2)]
    result = [str(nb)[-1] for nb in result]
    return int(''.join(result))