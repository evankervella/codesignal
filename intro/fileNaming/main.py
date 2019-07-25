def fileNaming(names: list) -> list:
    output_names = []
    for name in names:
        if name not in output_names:
            output_names.append(name)
        else:
            k = 1
            while name+'('+str(k)+')' in output_names:
                k += 1
            output_names.append(name+'('+str(k)+')')
    return output_names