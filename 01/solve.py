'''f = open("input.txt", "r")
lines = f.readlines()'''
with open("inpute.txt") as f:
    lines = f.readlines()

group1 = []
group2 = []
for line in lines:
    group1.append(int(line.split()[0]))
    group2.append(int(line.split()[1]))

test = [3,4,2,1,3,3]
test2 = [4,3,5,3,9,3]


# Bubblesort
def bubblesort(arr):
    for i in range(0,len(arr)-1,+1): #range(start, stop, step)
        for j in range(0,len(arr)-i-1,+1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def compare(arr1, arr2):
    sum=0
    if len(arr1) != len(arr2):
        exit(1)
    for i in range(len(arr1)):
        sum += abs(arr1[i]-arr2[i])
    return sum

def similarityscore(arr1, arr2):
    sum=0
    similarityscore=0
    for i in range(len(arr1)):
        currnum = arr1[i]
        for j in range(len(arr2)):
            if currnum == arr2[j]:
                sum+=1
        similarityscore += currnum*sum
        sum=0
    return similarityscore
        
print('Ergebnis-Part 1')
bubblesort(group1)
bubblesort(group2)
print(compare(group1, group2))
print(' ')

print('Ergebnis-Part 2')
print(similarityscore(group1, group2))
