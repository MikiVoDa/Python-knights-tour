n = 8
def isSafe(x, y, tabla): #functie care arata daca calul este inca pe tabla
    if(x >= 0 and y >= 0 and x < n and y < n and tabla[x][y] == -1):
        return True
    return False

def printSolutie(n, tabla): #functie pentru afisarea tablei parcurse
    for i in range(n):
        for j in range(n):
            print(tabla[i][j], end=' ')
        print()

def solveP(n):
    tabla = [[-1 for i in range(n)] for i in range(n)] #initializarea tablei
    move_x = [2, 1, -1, -2, -2, -1, 1, 2] #miscarile calului
    move_y = [1, 2, 2, 1, -1, -2, -2, -1] #miscarile calului
    tabla[0][0] = 0 #pozitia de start
    poz = 1 #setarea pozitiei calului ca fiind vizitata
    if (solvePUtil(n, tabla, 0, 0, move_x, move_y, poz) == False): #are sau sau nu are solutie
        print("Nu exista solutie")
    else:
        printSolutie(n, tabla) #afiseaza daca este corect

def solvePUtil(n, tabla, curr_x, curr_y, move_x, move_y, poz): #functie pentru rezolvarea problemei propriu zise
    if (poz == n ** 2): #daca toate poziitiile au fost vizitate
        return True
    for i in range(8): #altfel incercam alte miscaro
        new_x = curr_x + move_x[i] #miscarea calului pe pozitie noua
        new_y = curr_y + move_y[i] #miscarea calului pe pozitie noua
        if (isSafe(new_x, new_y, tabla)): #continua solutia daca se poate
            tabla[new_x][new_y] = poz #se seteaza noua pozitie ca fiind vizitata
            if (solvePUtil(n, tabla, new_x, new_y, move_x, move_y, poz + 1)):
                return True
            tabla[new_x][new_y] = -1 #backtracking
    return False

# driver code
solveP(n)