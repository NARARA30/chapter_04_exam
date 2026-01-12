a = []
b = ['a','b','c']

a.append(10)
b.append('d')

print(a,b)


c = [1,2,4,5]

c.insert(2,3)

print(c)


my_list = [3,1,2,3]

my_list.remove(3)

print(my_list)


e = [6,2,4,1]
f = ['carrot','apple','banana']

e.sort()
f.sort()

print(e,f)


my_list = [2,3,5,7,11]

print(my_list)
print(my_list.pop(0))
print(my_list.pop())
print(my_list)


num_list = [num for num in range(100) if num%2 == 0]
print(num_list)

new_list = [num*10 for num in range(10)]
print(new_list)

new_list2 = [str(num) for num in range(10) if num%2 == 0]
print(new_list2)


region_list = ['수원(경기)', '군산(전북)','포항(경북)','경주(경북)', '익산(전북)','강릉(강원)']

gyeonggi_list = []

for region in region_list :
    if '경기' in region :
        gyeonggi_list.append(region)


print(gyeonggi_list)
