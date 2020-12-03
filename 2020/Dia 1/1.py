# define the name of the file to read from
filename = "input"

def getMult(num, num2):
    if num + num2 == 2020:
        print(num * num2)
        return True
    else:
        return False

# open the file for reading
global filehandle
global filehandle2
global comparativo
global comparador

filehandle = open(filename, 'r')
comparativo = filehandle.readline()
while True:
    filehandle2 = open(filename, 'r')
    comparador = filehandle2.readline()
    while True: 
        if not comparador:
            break
        elif getMult(int(comparativo), int(comparador)):
            break
        else:
            comparador = filehandle2.readline()

    if not comparativo:
        break
    else:
        comparativo = filehandle.readline()

# close the pointer to that file
filehandle.close()
