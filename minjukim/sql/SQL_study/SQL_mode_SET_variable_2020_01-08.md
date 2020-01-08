# SQL mode mySQL SET @variable

/*
    1. gather consecutive project into a single row
    1.1 find rows where start_date = end_date -> not a clue!
    1.2 find missing start_date, and not missing durations are each projects duration.
    2. new column calculating project duration days
    3. in same duration, put the earlier start date first
    */
    
    -- 각 프로젝트가 끝난 시점
    -- 각 프로젝트의 시작 시점
    -- 이 테이블의 end_date 가 프로젝트별 end_date
    SET @id = 0;
    SET @id2 = 0;
    
    SELECT p1.start_date
    , p2.end_date
    
    FROM (
    	SELECT (@id:=@id+1) as id
    	, start_date
    	FROM Projects
    	WHERE start_date - 1
    	NOT IN (
    	SELECT start_date
    	FROM Projects)
    	ORDER BY start_date
    	) 
    
    	AS p1
    
    INNER JOIN ( 
    
    	SELECT (@id2:=@id2+1) as id
    	, end_date
    	FROM Projects
    	WHERE start_date + 1
    	NOT IN (
    	SELECT start_date
    	FROM Projects)
    	ORDER BY end_date
    	)
      AS p2
    
    
    ON p1.id = p2.id
    ORDER BY (p2.end_date - p1.start_date), p1.start_date

한슬님 코드

    SET @idx = 0;
    SET @idx2 = 0;
    
    SELECT sd.Start_date, ed.End_date
    FROM 
        (SELECT (@idx := @idx + 1) as No, Start_date 
            FROM Projects 
            WHERE Start_date NOT IN (SELECT End_date FROM Projects)
            ORDER BY Start_date
        ) as sd
        JOIN
        (SELECT (@idx2 := @idx2 + 1) as No, End_Date 
            FROM Projects 
            WHERE End_Date NOT IN (SELECT Start_Date FROM Projects)
        ORDER BY End_Date) as ed
        ON sd.No = ed.No
    ORDER BY (ed.End_date - sd.Start_date), sd.Start_Date