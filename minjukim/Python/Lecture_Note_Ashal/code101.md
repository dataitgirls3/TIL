# 파이썬 Python 2019-07-26
## 프로그램 Program (컴퓨터 프로그램)
### Pro + gram
### : 앞 + 쓰다, 적다
### : 앞으로 할 것을 적은 것

예측한 순서대로 되고 있다

### :행동 단위로 구성된다
> 1. 체크인
> 2. 강의
> 3. 점심
> 4. 실습
> 5. 회고

## 명령 Command
### : 컴퓨터는 애매한 건 못 알아먹음
### : 명확하게 전달해야하기 때문에 **인공 언어**를 사용한다.
## 프로그래밍 언어
### : 우리는 파이썬 Python 배운다
### : 많이 쓰이기 때문에

## 프로그램의 예시
> print('Hello, world')
- 명령어 + 실행문
- 한 줄도 프로그램
- 아무것도 없으면 비어있는 프로그램

## 문법을 정확하게 지켜서

## 코딩 공부
### : 많이 써보기

#
## 표현식 Expression
### : 파이썬에서 가장 단순한 단위
> 입력값 > 1

> 실행 결과 > 1

> 입력값 > 1 + 2

> 실행 결과 > 3

> 입력값 > Hi

> 실행 결과> 'Hi'

## 명령문 
### : 실행해준다
> 입력값 > print('Hi')

> 실행 결과 > Hi

## 할당문 Assignment Statement
> name = 'Anne'

> a = 1 + 2

## 연산자
### : 우선순위가 있다
> ### '+ : 더하기
> ### = : 변수 할당
> ### / : 나누기
> ### // : 몫

## Data Type
> 1 → int
### int : integer 정수형
### : 정확하지만 소수점은 나타낼 수 없다

> 1.2 → float
### float: 부동소수점
### : 약간의 오차가 있다
### : 컴퓨터는 2진수로 계산하기 때문

## 에러 Error
### : 에러 많이 봐두기
### : 나중에 문제 해결할 때 도움된다

> ### 'ㅇㅇ' 
> ### "ㅇㅇ"
### : 둘 다 결과는 'ㅇㅇ' 로 나옴

## 큰 따옴표를 표현해주고 싶을 때
> ### "\"Hello, world\""
> ### "\\"Hello, world\\""

## Escape 문자열
> ### \\: 닫히지 않는다고 알려주기
> ### \n : 다음 줄로 넘기기
> ### \t : 탭 넘기기

문자열 안에서 \역슬래시를 쓰고 싶을 때는 \\\ 두 번 쓰면 된다

> ### "Hi" * 2 → 'HiHi'
### 문자열 곱셈: 곱해준 숫자만큼 문자열 반복

## Modular 연산
> ### // : 몫
> ### % : 나머지

부등호
> ### 1 < 2 < 3
### : 연달아서 쓸 수 있다

## 연산자 계산 순서
### : and or 보다는 < > 부등호가 먼저 실행된다

# python 02 예제 중에서
> ### some_scores = scores
: some_scores 는 scores 와 같은 리스트이다
> ### some_scores = scores[:]
: scores 의 모든 값을 복사해서 some_scores 에 붙여넣는다

> ### scores = [10, 20, 30, 40, 50, 60]
> ### print(scores[::-1])
> [60, 50, 40, 30, 20, 10]
###

> ### scores[::2]
> ### [10, 30, 50]

> ### scores[2:4:-1]
> ### []
: 방향이 더 중요 마지막 -1
> ### scores[4:2:-1]
> ### [50, 40]

> ### scores[2:4:1]
> ### scores[2:4]
> ### [30, 40]

> ### scores[2:4:-1]
> ### []