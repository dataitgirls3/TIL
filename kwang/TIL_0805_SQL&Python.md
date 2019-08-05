| Date | Teacher | Category |
|:----|:----|:----|
|08.05 | Sunmi, Achal | SQL, Python |

<br>

01 SQL 
======
Join
---
	연관된 정보를 가지고 있는 테이블 두개를 합칠 때 사용한다.

### Inner Join - On

---

>눈으로 보는 JOIN: [https://sql-joins.leopard.in.ua/](https://sql-joins.leopard.in.ua/)

>예제 코드는 여기에서 실행해보세요: [https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all)

-------


#### 연습문제 1

- OrderID 10248번에는 몇 가지 종류의 상품이 들어있나요? 상품들의 총 갯수는 어떻게 되나요? Orders, OrderDetails 테이블을 이용해 알아보세요.

``` sql
SELECT count(od.OrderID), SUM(od.Quantity)
FROM Orders as o
	INNER JOIN OrderDetails AS od ON o.OrderId = od.OrderID
WHERE o.Orderid = 10248
```



#### 연습문제 2
 - OrderID 10249번에는 어떤 상품들이 들어있나요? 상품명을 출력하세요.

``` sql
SELECT ProductName
FROM Products AS p
	INNER JOIN OrderDetails As od ON p.ProductID = od.ProductID
WHERE od.OrderId = 10249
```

#### 연습문제 3
- OrderID 10249번에 들어있는 상품들의 총 가격은 얼마인가요?

``` sql
SELECT SUM(od.Quantity * p.Price)
FROM Products AS p
	INNER JOIN OrderDetails As od ON p.ProductID = od.ProductID
WHERE od.OrderId = 10249
```


</br>
</br>
-------
-------
</br>
</br>



02 Python
====

	1. 초기값 지정
	2. 코드를 반복 입력 = 누산
	3. 계산 결과 출력

*항등원??*

---

### 코딩 실습
``` python
#성적 총합 & 평균 구하기

my_scores = [30, 90, 80, 40, 50]

class_scores = [
    [30, 90, 80, 40, 50],
    [100, 100, 100, 100, 100],
    [90, 90, 30, 30, 20]
]

# 내 성적 총합 평균
my_total_score = 0
my_ave_score = 0

for a in my_scores:
    my_total_score += a

print("내 점수 총합: ", my_total_score)

# 반 전체 총합
total_score = 0
personal_score = [0, 0, 0]

for i in class_scores:
    for j in i:
        total_score += j

print("반 전체 총합: ", total_score)

# 반 전체 평균
ave_score = total_score / len(class_scores) / 5
print("반 전체 평균: ", ave_score)

```

<br>
<br>

---

## 추상화 - 함수 - **Function**

> 어떤 물체에서 본질이 되는 것을 뽑아 내는 것

``` python
def factorial(n):
	accumulator = 1
	for x in range(n)

```

``` python
def double(n):
	return n * 2
print(double(1))
```
BMI 계산하기
``` python
def bmi(weight, height):
    """Calculate BMI(Body Mass Index) with weight and height.

    Parameters:
    weight: Body weight in kilograms.
    height: Body height in meters.
    """


    return weight / (height ** 2)

print(bmi(68, 1.82))

print(bmi.__doc__)
help(bmi)
```
```python
def factorial(n):
    accumulator = 1
    for i in range(1, n + 1):
        accumulator *= i
    return accumulator

for i in range(1, 10 + 1):
    print(factorial(i))

```

score가 다음과 같은 형태로 주어졌을 때
scores = [80, 100, 70, 90, 40]
1. total 함수 만들기
2. average 함수 만들기
3. 제대로 했는지 확인하기
4. 코드를 GitHub에 올리기

``` python
scores = [80, 100, 70, 90, 40]

def total(n):
    
