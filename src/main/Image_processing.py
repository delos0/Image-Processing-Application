inp_filename, operation, out_filename = input().split()


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

def read_imagefile(f):
    form = f.readline().split()
    width = form[1]
    height = form[2]
    matrix = []
    for line in f.readlines():
        rows = []
        for digit in line.split():
            rows.append(int(digit))
        matrix.append(rows)
    return matrix



def misalign(matrix):
    temp = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            temp[j][i] = matrix[i][j]

    for i in range(len(temp)):
        if i%2==1:
            temp[i] = temp[i][::-1]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = temp[j][i]
    return matrix

def write_imagefile(f, matrix):
    width = len(matrix[0])
    height = len(matrix)
    f.write(f'P2 {width} {height} 255\n')
    for i in matrix:
        line = ''
        for j in i:
            line = line + (str(j) + ' ')
        line = line.rstrip()
        line += '\n'
        f.write(line)

def sort_columns(matrix):
    temp = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            temp[j][i] = matrix[i][j]

    for i in range(len(temp)):
        temp[i].sort()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = temp[j][i]
    return matrix


def sort_rows_border(matrix):

    for i in range(len(matrix)):
        start = 0
        end = len(matrix[i])
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                end = j
                temp = sorted(matrix[i][start:end])
                for k in range(start, end):
                    matrix[i][k] = temp[k-start]
                start = j+1
        end = len(matrix[i])
        temp = sorted(matrix[i][start:end])
        for k in range(start, end):
            matrix[i][k] = temp[k - start]
    return matrix

def convolution(matrix, kernel):
    temp = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum = 0
            for k in range(-1, 2):
                for t in range(-1, 2):
                    if i+k >= len(matrix): pass
                    elif i+k < 0: pass
                    elif j+t < 0: pass
                    elif j+t >= len(matrix[i]): pass
                    else: sum += (matrix[i+k][j+t]*kernel[k+1][t+1])
            if sum < 0: sum = 0
            if sum > 255: sum = 255
            temp[i][j] = sum
    return temp



# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
f = open(inp_filename, "r")
img_matrix = read_imagefile(f)
f.close()

if operation == "misalign":
    img_matrix = misalign(img_matrix)

elif operation == "sort_columns":
    img_matrix = sort_columns(img_matrix)

elif operation == "sort_rows_border":
    img_matrix = sort_rows_border(img_matrix)

elif operation == "highpass":
    kernel = [
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ]
    img_matrix = convolution(img_matrix, kernel)

f = open(out_filename, "w")
write_imagefile(f, img_matrix)
f.close()
