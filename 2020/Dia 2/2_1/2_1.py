filename = 'input'


def checkPass(min, max, letter, password):
    count = 0
    for x in range(len(password)-1):
        if password[x] == letter:
            count = count + 1
    if int(min) <= count <= int(max):
        return True


global filehandle
global contadorPass

contadorPass = 0
filehandle = open(filename, 'r')

while True:
    line = filehandle.readline()
    if not line:
        break

    passArr = line.split(' ')

    minMax = passArr[0].split('-')
    ruleLetter = passArr[1][0]
    password = passArr[2]

    if checkPass(minMax[0], minMax[1], ruleLetter, password):
        contadorPass = contadorPass + 1

print(contadorPass)
