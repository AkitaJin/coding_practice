CREATE TABLE 'student'( 
    'id' int(11),
    'name' varchar(11) DEFAULT NULL,
    'age' int(11) DEFAULT NULL,
    'sex' varchar(11) DEFAULT NULL,
    PRIMARY KEY('id')
);

CREATE TABLE 'score_relation'( 
    'id' int(11),
    'course_no' int(11) DEFAULT NULL,
    'student_no' int(11) DEFAULT NULL,
    'score' int(11)DEFAULT NULL,
    PRIMARY KEY(id));

INSERT INTO student VALUES
(7,'A',22,'asd'),
(8,'B',23,'qwe'),
(9,'C',24,'zxc'),
(10,'D',25,'ert');

INSERT INTO score_relation VALUES
(1,11,7,80),
(2,22,7,33),
(3,22,8,44),
(4,11,9,55);

-- 查询至少有一门课与学号为"7"同学所学相同课程的同学的学号与姓名，去重后，按照学号升序排列。
-- select id, name, count(course_no) cc
-- from student a join score_ relation b where a.id = b.student_no
-- WHERE 
--     course_no in (select distinct course_no from score_ relation WHERE student_no = 7)
-- having cc > 0

-- select distinct a.id, a.name 
-- from student a
-- join score_relation b on a.id = b.student_no
-- where b.course_no in
-- (select course_no from score_relation
-- where student_no=7)
-- and a.id<>7;

SELECT a.id, a.name FROM student a,
    (SELECT DISTINCT student_no FROM score_relation WHERE course_no IN
           (SELECT course_no FROM score_relation WHERE student_no = 7)) b
WHERE a.id = b.student_no;