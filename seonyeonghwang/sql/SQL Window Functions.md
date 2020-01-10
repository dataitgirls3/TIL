# SQL Window Functions

Created: Nov 25, 2019 10:55 AM

**참고사이트**

[http://www.gurubee.net/lecture/2382](http://www.gurubee.net/lecture/2382)

[https://mode.com/sql-tutorial/sql-window-functions/](https://mode.com/sql-tutorial/sql-window-functions/)

# 기본 용법

WINDOW FUNCTION 함수는 다른 함수들과 비슷해보이지만 OVER를 써서 원하는 값을 어떤 조건으로 어떤 순서로 보여줄지 적어준다.

전체 데이터셋에서 범위를 좀 더 좁히고 싶다면 PARTITION BY를 사용할 수 있다.

    # 예시
    
    select
    	rank() over (order by sal desc) all_rank,
    	rank() over (partition by job order by sal desc) job_rank
    from emp;
    
    

# RANK(), DENSE_RANK() AND ROW_NUMBER()

RANK() : 1, 2, 3, 4, 4, 6

- 동일한 값에 대해서는 동일한 순위를 매기고 그 뒷 순위는 동일한 순위 개수를 포함해서(?) 늘어남

DENSE_RANK() : 1, 2, 3, 4, 4, 5

- 동일한 값에 대해서는 동일한 순위를 매기고 그 뒷순위는 전 순위 +1

ROW_NUMBER() : 1, 2, 3, 4, 5, 6

- 동일한 값이라도 고유한 순위를 부여한다

# NTILE

전체 건수를 N등분한 결과를 보여준다

데이터 개수를 확인하고 써야 한다

    SELECT NTILE(4) OVER(ORDER BY SAL DESC) QUAR_TILE
    FROM EMP;

# LAG and LEAD

    #LAG - 앞에 있는 값을 가져옴
    
    SELECT LAG(SAL) OVER(ORDER BY HIREDATE) PREV_SAL
    FROM EMP
    WHERE JOB='SALESMAN';
    
    SELECT LAG(SAL, 2, 0) OVER(ORDER BY HIREDATE) PREV_SAL
    FROM EMP
    WHERE JOB='SALESMAN';
    
    #LEAD - 뒤에 있는 값을 가져옴
    
    SELECT LEAD(HIREDATE, 1) OVER (ORDER BY HIREDATE) NEXTHIRED 
    FROM EMP;

# 같은 WINDOW를 여러번 중복해서 쓰는 경우

    #ALIAS를 생성해서 사용할 수 있음
    
    SELECT start_terminal,
           duration_seconds,
           NTILE(4) OVER ntile_window AS quartile,
           NTILE(5) OVER ntile_window AS quintile,
           NTILE(100) OVER ntile_window AS percentile
      FROM tutorial.dc_bikeshare_q1_2012
     WHERE start_time < '2012-01-08'
    WINDOW ntile_window AS
             (PARTITION BY start_terminal ORDER BY duration_seconds)
     ORDER BY start_terminal, duration_seconds