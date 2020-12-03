filename = 'input'

def checkPass(min, max, letter, password):
    if password[min-1] == letter:
        if password[max-1] == letter:
            return False
        else:
            return True
    elif password[max-1] == letter:
        return True
    else:
        return False   

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

    if checkPass(int(minMax[0]), int(minMax[1]), ruleLetter, password):
        contadorPass = contadorPass + 1

print(contadorPass)
