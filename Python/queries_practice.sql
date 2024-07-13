SELECT * FROM schools;
SELECT * FROM students;
SELECT * FROM teachers;
SELECT * FROM classes;
SELECT * FROM students_classes;

INSERT INTO schools ( name, location, created_at, updated_at ) 
VALUES ( 'Hogwarts', 'England', NOW(), NOW() );

INSERT INTO schools ( name, location, created_at, updated_at ) 
VALUES ( 'Harvard', 'Boston', NOW(), NOW() ),
( 'PCA', 'Malibu', NOW(), NOW() );

INSERT INTO students ( first_name, last_name, grade_level, age, updated_at, created_at, school_id ) 
VALUES ( 'Chase', 'Matthews', 9, 15, NOW(), NOW(), 3 ),
( 'Elle', 'Woods', 1, 22, NOW(), NOW(), 2 );

INSERT INTO students ( first_name, last_name, grade_level, age, updated_at, created_at, school_id ) 
VALUES ( 'Fred', 'Weasley', 5, 15, NOW(), NOW(), 1 ),
( 'Ginny', 'Weasley', 2, 12, NOW(), NOW(), 1 );

INSERT INTO teachers ( first_name, last_name, position, created_at, updated_at, school_id ) 
VALUES ( 'Severus', 'Snape', 'Potions Master', NOW(), NOW(), 1 ),
( 'Teddy', 'Blake', 'Math Teacher', NOW(), NOW(), 3 ),
( 'Emmett', 'Richmond', 'Law TA', NOW(), NOW(), 2 );

INSERT INTO classes ( name, description, created_at, updated_at, teacher_id ) 
VALUES ( 'Introduction to Property Law', 'blah, blah, property law', NOW(), NOW(), 6 ),
( 'Care of Magical Creatures 5', 'Care of Magical Creatures class for Year Fives.', NOW(), NOW(), 4 ),
( 'World History: 1500 to Present Day', 'World history from 1500 to present day.', NOW(), NOW(), 5 );

INSERT INTO students_classes ( student_id, class_id ) 
VALUES ( 1, 2 ), ( 5, 1 ), ( 4, 3 );

SELECT CONCAT ( first_name, ' ', last_name ) AS full_name 
FROM students;

SELECT CONCAT ( first_name, ' ', last_name ) AS full_name 
FROM students 
WHERE school_id = 1;

SELECT * FROM teachers 
JOIN schools 
ON schools.id = teachers.school_id;

SELECT * FROM classes 
JOIN teachers 
ON teachers.id = classes.teacher_id;

SELECT classes.name AS course_name, teachers.first_name AS teacher 
FROM classes JOIN teachers 
ON teachers.id = classes.teacher_id;

SELECT CONCAT ( first_name, ' ', last_name ) AS teacher, classes.name AS course 
FROM classes JOIN teachers 
ON teachers.id = classes.teacher_id;

SELECT CONCAT ( first_name, ' ', last_name ) AS student, classes.name AS class 
FROM students 
JOIN students_classes ON students.id = students_classes.student_id 
JOIN classes ON classes.id = students_classes.class_id;

SELECT students.last_name AS student, classes.name AS class, teachers.last_name AS teacher 
FROM students 
JOIN students_classes ON students.id = students_classes.student_id 
JOIN classes ON classes.id = students_classes.class_id 
JOIN teachers ON teachers.id = classes.teacher_id;

SELECT CONCAT ( students.first_name, ' ', students.last_name ) AS student, classes.name AS class, teachers.last_name AS teacher 
FROM students 
JOIN students_classes ON students.id = students_classes.student_id 
JOIN classes ON classes.id = students_classes.class_id 
JOIN teachers ON teachers.id = classes.teacher_id;

SELECT CONCAT ( students.first_name, ' ', students.last_name ) AS student, 
classes.name AS class, 
CONCAT ( teachers.first_name, ' ', teachers.last_name ) AS teacher 
FROM students 
JOIN students_classes ON students.id = students_classes.student_id 
JOIN classes ON classes.id = students_classes.class_id 
JOIN teachers ON teachers.id = classes.teacher_id;

SELECT CONCAT ( students.first_name, ' ', students.last_name ) AS student, 
classes.name AS class, 
CONCAT ( teachers.first_name, ' ', teachers.last_name ) AS teacher, 
schools.name AS school 
FROM students 
JOIN students_classes ON students.id = students_classes.student_id 
JOIN classes ON classes.id = students_classes.class_id 
JOIN teachers ON teachers.id = classes.teacher_id 
JOIN schools ON schools.id = teachers.school_id;