#과제 5
s = input('숫자를 입력하세요 : ')
result = list(s)
print(result)

answer = 0
for i in result:
    answer = answer + int(i)

print(answer)

#1-3
result_list = []
    for i in range(1, 1000):
        if i % 2 == 0:
            result_list.append(i)
        if i % 7 == 0:
            result_list.append(i)

result_list = set(result_list)
print(sum(result_list))

#set 처음부터
s = set()

for i in range(1, 1000):
    if i % 2 == 0:
        s.add(i)

    if i % 7 == 0:
        s.add(i)
orint(sum(i))


#1-5
n = int(input())
m = int(input())

for i in range(m):
    print('*' * n)


#튜플 사용
n = int(input())
m = int(input())

tup = (n,m)
for i in range(tup[1]):
    print('*' * tup[0])

