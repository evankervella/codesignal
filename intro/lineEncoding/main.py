def lineEncoding(s: str) -> str:
    s = list(s)
    sub_strings = []
    current_char = s[0]
    current_chain = []
    for char in s:
        if char == current_char:
            current_chain.append(char)
        else:
            sub_strings.append(current_chain)
            current_char = char
            current_chain = [char]
    sub_strings.append(current_chain)
    output_s = []
    for sub_string in sub_strings:
        if len(sub_string) > 1:
            output_s.append(str(len(sub_string)))
        output_s.append(sub_string[0])
    return ''.join(output_s)
