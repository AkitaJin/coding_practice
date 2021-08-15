-- drop table if exists score;
-- CREATE TABLE score (
-- 'id' int(11) NOT NULL,
-- 'class_no' varchar(11) NOT NULL
-- );

-- 请查询出课程名为courseb和coursec分数和第二高的学生成绩，返回包括3列:班级，学号和这2门的分数和。 
drop table if exists 'score';
CREATE TABLE'score'( 
    'id' int(11),//主键id
    'class_no' varchar(11) DEFAULT NULL,//班级
    'course_name' varchar(11) DEFAULT NULL,//课程名字 
    'student_no' varchar(11) DEFAULT NULL,//学号 
    'student_score' int(11) DEFAULT NULL//学生成绩 
    PRIMARY KEY('id'));

INSERT INTO class_grade VALUES
(1,'A','course_b','11', 100),
(1,'A','course_c','11', 100),
(1,'A','course_b','22', 50),
(1,'A','course_c','22', 60);

select 
    class_no, student_no, sum(student_score) ss
from score
WHERE course_name = 'course_b' or course_name = 'course_c'
GROUP by class_no, student_no
ORDER by ss DESC
limit 1 offset 1;