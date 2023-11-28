def Swap(num:list, pos1:int, pos2:int):
    num[pos1],num[pos2] = num[pos2], num[pos1]
    return num

number = [12,23,43,12,45,32,90]
print(Swap(number,2,1))
