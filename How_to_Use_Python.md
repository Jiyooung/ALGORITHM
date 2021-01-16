# Python

## 변수

### 전역변수
```python
x = 10

def func():
    y = 5
    global z = 7

    print(x, y, z)  # 10, 5, 7

print(x, y, z)      # 10, 에러, 7  > 에러
```


## 형변환
int("3")
str(3)

### ASCII 코드 변경
- ascii -> char<br>
```python 
chr(45)
```
- char -> ascii<br>
```python
ord("A")
```

### enumerate()
```python
for index, data in enumerate(list):
```
index와 data가 동시에 필요할 때 사용
- list \> [(index1, data1), (index2, data2), ..]
- dict \> {index1: data1, index2: data2, ..}

## 연산자

### 산술 연산자
|Operator|Description|Example|
|---|---|---|
|+|더하기|a + b = 30|
|-|빼기|a - b = -10|
|*|곱하기|a * b = 200|
|/|나누기|b / a = 2.0|
|%|나머지|b % a = 0|
|**|제곱|a ** c = 1000|
|//|몫|a // c = 3|

### 삼항 연산자
```python
a if 조건식 else b 
```
조건식이 참이면 a, 거짓이면 b


## for문

### for문 하나 한 줄로 작성하기
```python
for i in list1 :
    list2.append(i + 1)

# 한 줄에 작성
list2 = [i + 1 for i in list1]
```

### 이중 for문 한줄로 작성하기
```python
list1 = [1, 2, 3]
list2 = [1, 1, 1]
list3 = []

for i in list1 :
    for j in list2 :
        if i == 1 :
            list3.append(i + j)
        else:
            list3.append(0)

# 한 줄에 작성
list3 = [i + j if i == 1 else 0 for i in list1 for j in list2]

# else문 없다면
list3 = [i + j for i in list1 for j in list2 if i == 1]
```
바깥 for문 먼저 쓰기

## int

### 반올림, 내림
```python
import numpy as np
np.around(a)    # 0.5 기준으로 올림/내림
np.round_(a, N) # N 소수점 자리까지 반올림 
np.rint(a)      # 가장 가까운 정수로 반올림

np.ceil(a)      # 올림
np.trucn(a)     # 버림

np.fix(a)       # 0 반향으로 가장 가까운 정수로 올림/내림
```

## string

### string > int
```python
s = "123"
n = int(s)
```

## list

### list 원소추가
```python
a.append(1)     # 원소 마지막에 1 추가
a.insert(2, 5)  # index 2의 위치에 값 5 추가, 뒤에 값들은 밀림
c = a + b       # list 합치기
a.extend([1,2,3])   # 기존 a의 뒤에 해당 리스트 추가하기

```
### list 원소삭제
```python
del a[1]    # list a의 index 1 삭제
a.remove(3) # list a에서 값 3을 찾아 가장 먼저 발견된 3을 제거
            # 3 값이 없으면 ValueError 발생
del a[a.index(3)] # remove(3)과 동일한 효과
```

### 특정 값이 있는지 체크하기
```python
if item in list:        # item이 list에 있으면 ~
if item not in list:    # item이 list에 없으면 ~
```

### 특정 값으로 초기화
```python
l = [0 for i in range(n)]   # n크기만큼 0으로 초기화한 리스트 생성
matrix = [[0 for col in range(c)] for row in range(r)]  # r * c 인 2차원 배열 생성
```

### list 정렬하기

#### <list>.sort()
```python
l.sort([reverse=<True|False>][, key=<function>])
``` 
**원본 리스트가 변경**됨, 반환값은 None
새로운 리스트를 생성하지 않기 때문에 sorted()보다 빠름

- 2차원 배열 정렬
```python
l.sort(key=lambda x:x[0])   # x[0] : 첫 번째 인자로 sort
                            # x[1]...등 다른 인자로 sort 가능
i.sort(key=lambda x: (x[0], -x[1])) # 첫 번째 인자값이 동일하면 두번째 값을 비교하여 내림차순으로 정렬, -붙이면 내림차순
```

#### sorted(<list>)
```python
sorted(iterable[, key=<function>][, reverse=<True|False>])
a = sorted(d.items(), key=lambda x:x[0]) # d.items() > [(key, value)] 형태로 반환
``` 
원본 리스트 영향X, **정렬된 새로운 리스트 반환**
모든 iterable(list, tuple, dict, 문자열 등등)에 동작 가능


## 오류 발생
### 들여쓰기 오류
`IndentationError: unindent does not match any outer indentation level`
들여쓰기에 tab과 space를 섞어서 사용됨!<br>
처음에 tab를 사용했으면 계속 tab으로 들여쓰기를 해야 함<br>


<!-- 
```python

``` -->

