# list.append(d)
# 자료 d를 리스트 마지막 원소 뒤에 추가
# 오직 한개의 자료만 넣을 수 있음

a = []
b = ['a','b','c']

a.append(10)
b.append('d')

print(a,b)

# list.insert(i,d)
# 지정한 인덱스 위치 i에 자료 d를 추가
# 오직 한 개의 자료만 넣을 수 있음
c = [1,2,4,5]

c.insert(2,3)

print(c)

# list.remove(d)
# 처음 나오는 자료 d를 제거
my_list = [3,1,2,3]

my_list.remove(3)

print(my_list)

# list.sort(d)
# 리스트 내의 자료들을 순서대로 정렬
# 숫자형은 오름차순, 문자열은 사전순(a부터 z까지)
e = [6,2,4,1]
f = ['carrot','apple','banana']

e.sort()
f.sort()

print(e,f)

# list.pop(i)
# 인덱스 i의 원소를 제거 후, 그 원소를 반환 
# 괄호를 비우면 마지막 원소를 제거 및 반환

my_list = [2,3,5,7,11]

print(my_list)
print(my_list.pop(0))
print(my_list.pop())
print(my_list)

# 반복문만 이용한 사례
# 0~99까지 숫자를 저장한 리스트 생성
num_list = [num for num in range(100) if num%2 == 0]
print(num_list)


new_list = [num*10 for num in range(10)]
print(new_list)

# 반복문과 조건문(if)를 이용한 사례
new_list2 = [str(num) for num in range(10) if num%2 == 0]
print(new_list2)

# 특정 텍스트만 추출하여 저장하는 방법
region_list = ['수원(경기)', '군산(전북)','포항(경북)','경주(경북)', '익산(전북)','강릉(강원)']

gyeonggi_list = []

for region in region_list :
    if '경기' in region :
        gyeonggi_list.append(region)


print(gyeonggi_list)


region_list = ['수원(경기)', '군산(전북)','포항(경북)','경주(경북)', '익산(전북)','강릉(강원)']

gyeonggi_list = [region for region in region_list
 if '경기' in region]

print(gyeonggi_list)



# 반복문과 조건문을 이용한 사례
# 물건의 가격에 따라 할인율 적용

original_prices = [800, 1200, 950, 1100]
discounted_prices = []

for price in original_prices:
    if price >= 1000:
        discounted_prices.append(int(price*0.9))
    else:
        discounted_prices.append(price)

print(original_prices)

print(discounted_prices)


original_prices = [1000,1400,1150,1300]

discounted_prices = [
    int(price*0.9) if price >= 1000 else price
for price in original_prices
]

print(original_prices)

print(discounted_prices)


# 리스트를 정렬하는 방법
# python에서 리스트를 정렬하는 방법은 sort 메소드를 사용
# sort 메소드는 원본 리스트를 정렬
# sort 메소드를 사용한 명령어를 저장하면 None이 저장됨
my_list = [5,2,3,1,4]
my_list.sort()

print(my_list)


my_list = [5,2,3,1,4]
sort_list = my_list.sort()

print(my_list)

print(sort_list)

# python에서 리스트를 정렬하는 또 다른 방법은 sorted 함수를 사용
# sorted 함수는 복사본 리스트를 정렬
# sorted 함수를 사용한 명령어를 저장하면 정렬된 리스트가 저장 됨
my_list = [5,2,3,1,4]
sort_list = sorted(my_list)

print(my_list)

print(sort_list)

# 시퀀스 자료형
# 순서가 있는 자료형, 문자열/리스트 등이 이에 속함
# 원소 간의 순서가 존재하기 때문에 인덱싱, 슬라이싱이 가능
# 인덱싱, 슬라이싱을 할 때 음수를 넣거나 자리를 비우는 것이 가능

a = "Hello"
b = ['e','l','i','c','e']

print(a[1])

print(b[2:4])

print(a[-1])

print(b[:4])

print(b[2:])

# in 연산자로 시퀀스 안에 원소가 잇는지 확인 가능
a = "Hello"
b = ['e','l','i','c','e']

print('e' in a)

print('E' in b)


# len 연산자로 시퀀스 자료형의 길이 확인 가능
a = "Hello World"
b = ['e','l','i','c','e']

print(len(a))

print(len(b))

# + 연산자를 이용하면 같은 종류의 시퀀스 자료를 이어 붙일 수 있음
c = 'Good' + 'Day'
print(c)

d = ['H','e'] + ['l','l','o']
print(d)

# 연산자와 숫자를 이용하면 시퀀스 자료를 반복할 수 있음
e = 'Go!!'*5
print(e)

f = [13,17,19*3]
print(f)

g = [13,17,19] * 3
print(g)

# seq.count(d) 시퀀스 내부의 자료 d의 개수를 반환
my_seq = [2,2,2,4,4]
print(my_seq.count(2))

my_str = 'elice and alice'
print(my_str.count('e'))