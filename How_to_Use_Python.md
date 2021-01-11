# Python

## 형변환
int("3")

### ASCII 코드 변경
- ascii -> char
``chr(45)``
- char -> ascii
``ord("A")``

### enumerate()
```
for index, data in enumerate(list):
```
index와 data가 동시에 필요할 때 사용
- list \> [(index1, data1), (index2, data2), ..]
- dict \> {index1: data1, index2: data2, ..}