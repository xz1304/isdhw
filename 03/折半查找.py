from math import ceil
x=int(input("������Ҫ���ҵ����֣�"))
low=0
numgroup=[1,4,5,6,8,11,13,16,17]
high=len(numgroup)-1
i=0
mide=0
while(low<high):
    i=i+1
    mid=(low+high)/2
    mid= int(ceil(mid))
    print('���Ҵ�����',i)
    print('the mid is',mid)
    print('the mid value is',numgroup[mid])
    if x==numgroup[mid]:
        print('��Ҫ�ҵ�ֵ�Ѿ����ҵ���',numgroup[mid])
        break
    elif x>numgroup[mid]:
        low=mid
    else:
        high=mid
if low>=high:
    print('δ�ҵ���')


