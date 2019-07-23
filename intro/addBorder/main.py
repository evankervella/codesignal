def addBorder(picture: list) -> list:
    borderedPicture = ['*'+char+'*' for char in picture]
    borderedPicture.insert(0, '*' * (2+len(picture[0])))
    borderedPicture.append('*'*(2+len(picture[0])))
    return borderedPicture