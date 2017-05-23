def rule1(C):
    for i in range(0,5) :
        if (C[i][0] +C[i][1] +C[i][2] +C[i][3] +C[i][4]) == 5:
            return True;
    return False;

def rule2(C) :
    for i in range(0,5) :
        if (C[0][i] +C[1][i] +C[2][i] +C[3][i] +C[4][i]) == 5:
            return True;
    return False;

def rule3(C) :
    count =0
    for i in range(0,5) :
        if C[i][i] == 1:
            count = count +1
    if count == 5:
        return True;

    count = 0
    for i in range(0,5) :
        if C[i][4-i] == 1:
            count = count +1
    if count == 5 :
        return True;
    
    return False;


def rule4(C):
    if (C[0][0] +C[0][4] +C[4][0] +C[4][4]) == 4 :
        return True;
    
    return False;    



row = 5
col = 5

BINGO = []
C = []
T = int(input())

for t in range(0,T):
    BINGO = []
    C = []
    for i in range(0, row):
        row_input = input().split()
        row_input = [int(j) for j in row_input]
        BINGO.append(row_input)
        
        if i == 2:
            C.append([0,0,1,0,0])
        else :
            C.append([0]*5)
            
    input_numbers = input().split()
    input_numbers = [int(j) for j in input_numbers]

    count_of_input = 0
    for number in input_numbers:

        count_of_input = count_of_input + 1

        for i in range(0,5):
            for j in range(0,5):
                if number == BINGO[i][j]:
                    C[i][j] = 1
                    
        if rule1(C) == True:
            print(count_of_input)
            break

        if rule2(C) == True:
            print(count_of_input)
            break


        if rule3(C) == True:
            print(count_of_input)
            break

        if rule4(C) == True :
            print(count_of_input)
            break

