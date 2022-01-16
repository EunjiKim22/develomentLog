'''
print("Hello, World!")

a = 1
b = 4.1
print(a,b)  # int, float 두개를 많이 쓴다.

print(a+b)
print(a*b)  # 사칙연산 가능
print(a//b) # 몫이 나옴
print(a%b) # 나머지
print(a**b) # 제곱

c = "Eunji's age is 22."
d = " 나는 생각한다.\n 고로 존재한다." #이스케이프 문자 \n을 넣으면 줄바꿈
e = "python"
print(c)
print(d)
print(e*100)
'''
#위에 꺼 응용
'''
print("="*50)
print("My program")
print("="*50)
'''
# 인덱싱
'''
a = "Life is too short, You need Python"
print(a[2])
print(a[:5]) # 공백도 포함해서 같이 나옴 "Life " 이렇게
print(len(a))
'''
#  인덱싱 예시
'''
a = "20201012Rainy"
date  = a[:8]
weather = a[8:]
print(date, weather)

year = a[:4]
day = a[4:8]

print(year, day, weather)
'''
# "pithon" 이라는 문자열을 "python"으로 바꿀려면
'''
a ="pithon"
print(a)
a = a[:1] + "y" + a[2:]
print(a)
'''
# 문자열 포매팅 %s 문자열 %c 문자 1개 %d 정수 %f 부동소수(float) %o 8진수 %x 16진수 %% 문자% 자체
'''
a = "I eat %d apples." % 3
print(a)
b = "I eat %s apples." % "five"
print(b)
number = 5
c = "I eat %d apples." % number
print(c)
day = "three"
d = "I ate %d apples. so I was sick for %s days." % (number, day)
print(d)
e = "I have %s apples." % 3
f = "I have %s apples." % 3.24
print(e, f) # 숫자를 자동으로 스트링으로 바꾸기 때문에 그냥 사용해도 괜찮음
'''
# 문자열 포맷팅 +
# a = "Error is %d%." % 98 # -> 이러면 에러남 %d 와 같은 애들이 문자열에 있으면 %% 이렇게 사용해야한다.
#b = "Error is %d%%" % 98 
#print(b)
# 포맷 코드와 숫자 함께 사용하기
# 추가했다ㅏㅏㅏㅏㅏ