int: total_courses = 10; % Example total number of courses
set of int: COURSES = 1..total_courses;
array[COURSES] of var 0..1: course_taken; % 1 if taken, 0 otherwise
array[COURSES, COURSES] of int: prerequisites; % Matrix of prerequisites

% Constraints for taking courses based on prerequisites
constraint forall(i, j in COURSES where prerequisites[i, j] == 1) (
    course_taken[j] <= course_taken[i]
);

% Constraint for minimum credits per semester
constraint sum(c in COURSES) (course_taken[c] * credits[c]) >= 12;

% Additional constraints can be added similarly
