# SQL mode Occupations

SET @id=0;
    SET @id2=0;
    SET @id3=0;
    SET @id4=0;
    
    SELECT doctor.name, professor.name, singer.name, actor.name
    FROM
    (SELECT (@id:= @id + 1) AS id, name
    FROM Occupations
    WHERE occupation = 'Doctor'
    ORDER BY name) AS doctor
    
    RIGHT JOIN
    
    (SELECT (@id2:= @id2 + 1) AS id, name
    FROM Occupations
    WHERE occupation = 'Professor'
    ORDER BY name) AS professor
    ON doctor.id = professor.id
    
    LEFT JOIN
    
    (SELECT (@id3:= @id3 + 1) AS id, name
    FROM Occupations
    WHERE occupation = 'Singer'
    ORDER BY name) AS singer
    ON professor.id = singer.id
    
    LEFT JOIN
    
    (SELECT (@id4:= @id4 + 1) AS id, name
    FROM Occupations
    WHERE occupation = 'Actor'
    ORDER BY name) AS actor
    ON professor.id = actor.id

재민님 코드 오라클

    SELECT MAX(DOCTOR), MAX(PROFESSOR), MAX(SINGER), MAX(ACTOR)
    FROM (SELECT CASE WHEN Occupation = 'Doctor' THEN Name END AS DOCTOR,
                 CASE WHEN Occupation = 'Professor' THEN Name END AS PROFESSOR,
                 CASE WHEN Occupation = 'Singer' THEN Name END AS SINGER,
                 CASE WHEN Occupation = 'Actor' THEN Name END AS ACTOR,
                 ROW_NUMBER() OVER (PARTITION BY Occupation
                                    ORDER BY Name) AS ROW_NUMBER
          FROM OCCUPATIONS)
    GROUP BY ROW_NUMBER
    ORDER BY ROW_NUMBER
    ;