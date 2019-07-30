def mirrorBits(a: int) -> int:
    ouput_a = ''
    for b in bin(a)[2:]:
        ouput_a = b + ouput_a
    return int(ouput_a, 2)