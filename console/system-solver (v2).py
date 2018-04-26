#  http://paulbourke.net/miscellaneous/determinant/
import style
import os
import time
from matrixanim import matrix


def printEquations(matrice_A, matrice_B, nbrEquation, nbrUnknowns):
    for x in range(0, nbrEquation):
        print('Equation ' + x + ' : ')
        for y in range(0, nbrUnknowns):
            if(y != nbrUnknowns-1):
                print('\b' + matrice_A[x][y] + '' +nbrUnknowns[y] + ' + ')
            else:
                print('\b' + matrice_A[x][y] +''+nbrUnknowns[y] + ' = ')
        print('\b' + matrice_B[x])



def transpose(matrice, n):
    i, j = None
    temp = None

    for i in range(1, n):
        for j in range(0, i):
            temp = matrice[i][j]
            matrice[i][j] = matrice[j][i]
            matrice[j][i] = temp


def determinant(matrice, n):
    i, j, j1, j2 = None
    det = 0
    provisoire = {}

    if n < 1:
        print("Cannot be under 1")
    elif n == 1 :
        det = matrice[0][0]
    elif n == 2 :
        det = matrice[0][0] * matrice[1][1] - matrice[1][0] * matrice[0][1]
    else :
        det = 0
        for j1 in range(0, n):
            provisoire = {}
            for i in range(0, n-1):
                provisoire[i] = {}
            for i in range(1, n):
                j2 = 0
                for j in range(0, n):
                    if j == j1:
                        continue
                    provisoire[i - 1][j2] = matrice[i][j]
                    j2+=1

            det += pow(-1.0, 1.0 + j1 + 1.0) * matrice[0][j1] * determinant(provisoire, n - 1)

            for i in range (0, n-1):
                del provisoire[i]

            del provisoire

    return det


def cofactor(matrice1, n, matrice2):
    i, j, ii, jj, i1, j1 = None
    det = None
    provisoire = {}

    for i in range (0, n-1):
        provisoire[i] = {}

    for j in range (0, n):
        for i in range(0, n):
            i1 = 0
            for ii in range(0, n):
                if ii == i:
                    continue

                j1 = 0
                for jj in range(0, n):
                    if jj == j:
                        continue

                    provisoire[i1][j1] = matrice1[ii][jj]
                    j1+=1
                i1+=1

            det = determinant(provisoire, n - 1)
            matrice2[i][j] = pow(-1.0, i + j + 2.0) * det

    for i in range(0, n-1):
        del provisoire[i]
    del provisoire


def printEquations(matrice_A, matrice_B, nbrEquation, nbrUnknowns, unknowns_X):
    for x in range(0, nbrEquation):
        equation = 'Equation ' + str(x + 1) + ' : '
        for y in range(0, nbrUnknowns):
            if y != nbrUnknowns - 1:
                equation = equation + str(matrice_A[x][y]) + '' +  unknowns_X[y] + ' + '
            else:
                equation = equation + str(matrice_A[x][y]) + '' + unknowns_X[y]  + ' = '
        equation = equation + str(matrice_B[x])
        print(style.yellow(style.bold(equation)))


'''
Declarations :
'''
# Declaring the variables of the problem
matrice_B = []  # Matrix to the right
const_possible_unknowns = ['x', 'y', 'z', 'w', 'v', 'u']  # Solve equation system with 6 potentialy unknowns variables
unknowns_X = []  # Keep here the effective unknowns

# Declaring the variables containing the user inputs
nbrEquation = 0
nbrUnknowns = 0
leftFormulas = []  # Array of array Containing the left side of equation
rightAnswer = []


'''
Animation : 

matrix(700, .03)
os.system('clear')
'''

'''
User Inputs : 
'''
# Ask for the number of equations
print(style.red(style.bold('Combien y-a-t-il d\'equation dans le système ?')))
nbrEquation = int(input())
os.system('clear')

# Ask for the number of Unknowns
print(style.red(style.bold("Combien y-a-t-il de variable dans le système ?")))
nbrUnknowns = int(input())
os.system('clear')

# Matrix initialisation (because there is not such a thing as dynamic array in python ?
matrice_A = [[0 for x in range(nbrUnknowns)] for y in range(nbrEquation)]   # Matrix to the left
matrice_B = [0 for x in range(nbrEquation)] # Array (single column matrix)

# Resume number of variables and equations
print(style.green(style.bold('Il y a '+ str(nbrEquation) +' equations dans le système.')))

string_unknowns = ''
for x in range(0, nbrUnknowns):
    unknowns_X.append(const_possible_unknowns[x])
    if nbrUnknowns == 1 :
        string_unknowns = style.green(style.bold(unknowns_X[x] + " fait partie des inconnues présentes dans le système."))
        break;
    else:
        if x < nbrUnknowns -1 :
            string_unknowns = string_unknowns + style.bold(unknowns_X[x]) + ', '
        else :
            string_unknowns = string_unknowns + style.bold(unknowns_X[x]) + " font partie des inconnues présentes dans le système."

print(style.green(style.bold("Il y a " + str(len(unknowns_X)) + " variable(s) dans le système d'équation.")))
print(string_unknowns.center(40))
time.sleep(5)
os.system('clear')

# Enter user input for definition of equation
for x in range(0, nbrEquation):
    print(style.red(style.bold('Veuillez completer l\'equation ' + str(x + 1) + ':')))
    time.sleep(5)
    os.system('clear')
    for y in range(0, nbrUnknowns):
        print(style.red(style.bold('Quel est le coeficient de ' + unknowns_X[y] + ' ?')))
        matrice_A[x][y] = int(input())
        os.system('clear')
    print(style.red(style.bold('Quel est le résultat de cette équation ?')))
    matrice_B[x] = int(input())
    os.system('clear')

# Print equations
printEquations(matrice_A, matrice_B, nbrEquation, nbrUnknowns, unknowns_X)


'''
Calcul du déterminant
'''
print(style.blue(style.bold('Calcul du déterminant...')))



