N = int(input())
count = 0
Decimals = list(map(int,input().split()))
#print(Decimals)
Bin_Arr = []
for dec in range(len(Decimals)):
    Bin_Arr.append(bin(Decimals[dec])[2:])

#print(Bin_Arr)
max_len = max(Bin_Arr,key=len)
calc_len  = len(max_len)
#print("l is",l)
#print(max_len)
for i in range(len(Bin_Arr)):
    Bin_Arr[i]=Bin_Arr[i].zfill(calc_len)
#print(Bin_Arr)

for i in range(len(Bin_Arr)):
    for j in range(len(Bin_Arr)):
        if i==j:continue
        if j is len(Bin_Arr) - 1:break
        #print(Bin_Arr[i],Bin_Arr[j])
        if Bin_Arr[i].count('0') + Bin_Arr[j].count('0') == Bin_Arr[i].count('1') + Bin_Arr[j].count('1'):
           count += 1
    i = i+1
if len(Bin_Arr) != 2:
    
    all_ele = ""
    all_ele = all_ele.join(Bin_Arr)
    #print(all_ele)

    if all_ele.count('0') == all_ele.count('1'):
        count +=1

if N>1:
    count_bin = bin(count)[2:]
    count_len = count_bin.zfill(calc_len)
    print(count_len)
else:
    print('0'*calc_len)
