#for 문 원소로 반복하는 방법
# 시퀀스의 원소를 하나씩 변수에 넣어가면서 명령 실행
sum = 0

for num in [1,2,3,4,5]:
    print(num)

sum = 0

for i in [1,3,5]:
    sum = sum +i

print(sum)

# 명령이 len(시퀀스)번 만큼 실행
length = 0

for i in [1,3,5]:
    length = length + 1

print(length)

# 연속되는 숫자를 만ㄷ늘어 주는 시퀀스 자료형
# 시작하는 숫자(a)와 끝내는 숫자(b)를 지정하면 a~ (b-1)까지의 숫자 생성
print(range(1,9))

print(list(range(1,9)))

print(range(5))

print(list(range(5)))

num_list = [1]

for i in range(2,5):
    num_list.append(i)

print(num_list)

# 횟수로 반복하는 방법
# a번 만큼 명령을 수행
count = 0

for i in range(10):
    count = count + 1

print(count)

# range와 len, 인덱싱을 이용할 수 있음
str_list = ['a','b', 'c','d']

for idx in range(len(str_list)):
    print(idx)

for idx in range(len(str_list)):
    print(str_list[idx])

# 조건으로 반복하는 방법
# 조건이 True이면 명령을 수행
number = 5

while number > 0 :
    print(number)
    number = number-1

print('good day!!')

# 1부터 4까지 더하기
i=1
sum=0

while i < 5:
    sum =sum+i
    i=i+1

print(sum)

# 무한정 코드가 실행되어 무한루프 상태가 됨 (실행시키면 안됨)
#i=1

#while i >0:
#    print(i)
#    i=i+1

#print('종료')

# break 문
# if 문으로 조건을 걸어준 다음, break 문 실행.
# 반복문을 탈출하는 역할
number = 1

while True : 
    print('Good Day!!')

    if number >= 5 :
        break

    number = number + 1

print(number)

# continue 문
# if 문으로 조건을 걸어준 다음, continue 실행. 반복문을 건너뛰는 역할!
for number in range(1,11) :

    if number % 2 != 0 :
        continue

    print(number)
