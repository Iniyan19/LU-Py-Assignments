list = [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
list.sort()
k=list.count(0);
print(list[k:]+list[:k])
