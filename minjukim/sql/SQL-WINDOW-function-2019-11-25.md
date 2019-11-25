# SQL WINDOW function 2019-11-25

[SQL Window Functions | Advanced SQL - Mode Analytics](https://mode.com/sql-tutorial/sql-window-functions)

`WINDOW` 데이터를 섹션으로 나눠서 보는 함수

MySQL 에는 `WINDOW` function 이 없다

cf. window function 을 지원하는 DB

- postgresql
- Hive : 대용량 분산처리 DB
- Presto
- Amazon Redshift : AWS 와 연결, 비싸다
- ORACLE : 금융처럼 돈 많고 커스텀이 필요한 곳에서 쓴다
- Tableau 에도 SQL 이 붙어있다

**`WINDOW` 함수 안에서 쓰는 함수**

`SUM`, `COUNT`, `AVG`

`ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`

`ROW_NUMBER()` 공동 순위가 없다

`RANK()` 공동 4위 다음에 6위

`DENSE_RANK()` 공동 4위 다음에 5위

`NTILE(#)` : 숫자 개로 나눠준다

데이터 갯수가 (#)보다 적다면 데이터 갯수까지로만 나눠진다

`LAG`, `LEAD`

`LAG(컬럼명, #)` #개 앞의 데이터 출력

e.g. 직전 배송완료시간과의 간격

`LEAD(컬럼명, #)` #개 뒤의 데이터 출력

    SQL 은 피어 체크가 중요하다
    
    오류코드가 제대로 안 나오기 때문에