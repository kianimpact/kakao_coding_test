n = int(input())
arr1=list(map(int,input().replace('[','').replace(']','').split(',')))
arr2=list(map(int,input().replace('[','').replace(']','').split(',')))

result=[]
for i in range(n):
    result.append(bin(arr1[i] | arr2[i])[2:].replace('1', '#').replace('0', ' '))

print(result)

