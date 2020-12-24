def InBetween_Row(i,start_j,end_j):
    len_of_zero = end_j - start_j - 1

    while(len_of_zero):
        if Array[i-1][start_j + len_of_zero] and Array[i+1][start_j + len_of_zero]:
            len_of_zero -= 1
        else:
            break
    if len_of_zero == 0:
        return 1
    else:
        return 0
def InBetween_Col(j,start_j,end_j):
    len_of_zero = end_j - start_j - 1

    while(len_of_zero):
        if Array[start_j+len_of_zero][j-1] and Array[start_j+len_of_zero][j+1]:
            len_of_zero -=1
        else:
            break
    if len_of_zero == 0:
        return 1
    else:
        return 0
row = 5
col = 8

Array =  [[1,1,1,1,1,1,1,1],
          [1,0,0,0,1,0,0,1],
          [1,1,1,1,1,1,1,1],
          [1,0,1,0,0,0,1,1],
          [1,1,1,1,0,1,1,0]]
pool = 0

for i in range(row):
    for j in range(col):
        if i == 0 or j == 0 or i == row-1 or j == col-1:
            continue
        
        
        if Array[i][j] == 0 and Array[i][j+1] == 1:
            if Array[i][j+1] and Array[i][j-1] and Array[i-1][j] and Array[i-1][j+1] and Array[i-1][j-1]\
            and Array[i+1][j] and Array[i+1][j+1] and Array[i+1][j-1]:
                pool += 1

        elif Array[i][j] == 0 and Array[i][j+1] == 0:
            #print(i,j)
            start_j = j
            #print("Startj",start_j)
            for j in range(j,col):
               
                if Array[i][j] == 0 and Array[i][j+1] == 1:
                    #print(i,j,col)
                    end_j = j
                    #print(start_j,end_j)
                    
                    if Array[i][start_j-1] and Array[i][end_j+1] and Array[i-1][start_j] and Array[i-1][start_j-1]\
                       and Array[i-1][end_j] and Array[i-1][end_j+1] and Array[i+1][start_j] and Array[i+1][start_j-1]\
                       and Array[i+1][end_j] and Array[i+1][end_j+1] and InBetween_Row(i,start_j,end_j):
                        
                        pool += 1

                        
            #print(len_of_zero)
            break
for j in range(col):
    #print()
    for i in range(row):
        if j == 0 or i == 0 or i == row-1 or j == col-1:
            #print("Skipped",i,j)
            continue
        #print(Array[i][j],end = " ")
        if Array[i][j] == 0 and Array[i+1][j] == 0:
            start_j = i
            for i in range(i,row):
                if Array[i][j] == 0 and Array[i+1][j] == 1:
                    end_j = i
                    #print(j,start_j,end_j)
                    if Array[start_j][j-1] and Array[start_j][j+1] and Array[start_j-1][j] and Array[start_j-1][j+1]\
                       and Array[start_j-1][j-1] and Array[end_j+1][j] and Array[end_j][j+1] and Array[end_j][j-1]\
                       and Array[end_j+1][j-1] and Array[end_j+1][j+1] and InBetween_Col(j,start_j,end_j):
                        
                        pool += 1
        break


print("Total Pool : ",pool)
