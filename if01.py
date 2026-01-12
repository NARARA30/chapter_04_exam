#참 또는 거짓을 나따내는 자료형
print(True)
print(False)

#숫자나 문자의 값을 비교하는 연산자
print(3 < 5)
print(7 == 5)
print(2 >= 10)
print(5! =10)

# 각 논리가 모두 True여야 True
print(3==3 and 4<=5 and 6>2)

# 논리들 중 하나라도 True가 존재하면 True
print(3==4 or 4<=5 or 6<2)

#논리값을 뒤집음(True - False)
print(not 3==4)

#if 문
i=1

if i == 1:
    print(i)

else:
    print(i+1)

score = 78

if score>=90:
    print("a")
elif score>=75:
    print('b')
else:
    print('c')
    