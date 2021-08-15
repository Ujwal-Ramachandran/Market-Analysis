a = [1,2,3]
for i in range(1,7) :
    a.append(a[i]-a[i-1])
print(a[7])