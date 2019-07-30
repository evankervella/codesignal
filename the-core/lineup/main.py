def lineUp(commands: str) -> int:
    counts = []
    count = 0
    output = 0
    for char in commands:
        if char == 'L':
            count += 1
        if char == 'R':
            count -= 1
        counts.append(count)
    for count in counts:
        if count % 2 == 0:
            output += 1
    return output