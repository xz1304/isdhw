from math import ceil
x=int(input("请输入要查找的数字："))
low=0
numgroup=[1,4,5,6,8,11,13,16,17]
high=len(numgroup)-1
i=0
mide=0
while(low<high):
    i=i+1
    mid=(low+high)/2
    mid= int(ceil(mid))
    print('查找次数。',i)
    print('the mid is',mid)
    print('the mid value is',numgroup[mid])
    if x==numgroup[mid]:
        print('你要找的值已经查找到：',numgroup[mid])
        break
    elif x>numgroup[mid]:
        low=mid
    else:
        high=mid
if low>=high:
    print('未找到。')


