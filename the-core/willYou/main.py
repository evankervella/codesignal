def willYou(young: bool, beautiful: bool, loved: bool) -> bool:
    statement = ((young == beautiful) and (young != loved))
    c_statement = (loved == 1 and not ((loved == young) and (loved == beautiful)))
    if statement:
        return True
    if c_statement:
        return True
    return False