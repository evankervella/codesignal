def boxBlur(image):
    filter_size_h = 3
    filter_size_l = 3
    output_image = []
    for i in range(len(image)-filter_size_h+1):
        line = []
        for j in range(len(image[0])-filter_size_l+1):
            n = 0
            for k in range(i, i+filter_size_h):
                for l in range(j, j+filter_size_l):
                    n += image[k][l]
            line.append(int(n/(filter_size_h*filter_size_l)))
        output_image.append(line)
    return output_image