#  http://paulbourke.net/miscellaneous/determinant/
import style
import os
import time
import numpy as np
import PyGnuplot as gp
from matrixanim import matrix

'''
1 Functions :
'''
def printEquations(matrice_A, matrice_B, nbrEquation, nbrUnknowns, unknowns_X):
    for x in range(0, nbrEquation):
        equation = 'Equation ' + str(x + 1) + ' : '
        for y in range(0, nbrUnknowns):
            if y != nbrUnknowns - 1:
                equation = equation + str(matrice_A[x][y]) + '' +  unknowns_X[y] + ' + '
                #print(style.bold('\b' + style.yellow(str(matrice_A[x][y])) + '' + style.blue(unknowns_X[y]) + style.cyan(' + ') + '\b'))
            else:
                equation = equation + str(matrice_A[x][y]) + '' + unknowns_X[y]  + ' = '
                #print(style.bold('\b\b' + style.yellow(str(matrice_A[x][y])) + '' + style.blue(unknowns_X[y]) + style.cyan(' = ') + '\b' ))
        #print(style.yellow(style.bold('\b\b' + str(matrice_B[x])))+ '\b')
        equation = equation + str(matrice_B[x])
        print(style.yellow(style.bold(equation)))


'''
2 Declarations :
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
3 Animation of introduction : 

matrix(700, .03)
os.system('clear')
'''


'''
4 User Inputs : 
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


'''
5 Print equations : 
'''
printEquations(matrice_A, matrice_B, nbrEquation, nbrUnknowns, unknowns_X)


'''
6 Solve it : 
'''
# Convert list to numpy arrays
matrice_A = np.array(matrice_A)
matrice_B = np.array(matrice_B)

# Solution numpy... The Lazy Way :)))
soluce = np.linalg.solve(matrice_A, matrice_B)   # <== C'EST ICI QUE CA SE PASSE ! Mouahaha...
print(soluce)


'''
7 Print Graphs : 
'''
# Print equations
gp.c('')
gp.c('set xlabel \'x\'')

gp.c('plot ylabel')

gp.c('plot ')

