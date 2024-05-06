% Load course data
#include "cse_courses.lp".

% Define semesters (assuming the program may last up to 10 semesters for flexibility)
semester(1..10).

% Each course can only be scheduled once if it has not been taken.
{ schedule(Course, S) : semester(S) } = 1 :- course(Course, _, _, _, _), not course_taken(Course).

% Limit credits per semester between 12 and 18
:- semester(S), #sum { Credits, Course : course(Course, Credits, _, _, _), schedule(Course, S) } < 12.
:- semester(S), #sum { Credits, Course : course(Course, Credits, _, _, _), schedule(Course, S) } > 18.

% Assume prerequisite relation is defined as prerequisite(Course, PreCourse)
:- schedule(Course, S1), schedule(PreCourse, S2), prerequisite(Course, PreCourse), S1 <= S2.

% Undergraduates need at least 80 CSE credits
:- career("Undergraduate"), #sum { Credits, Course : course(Course, Credits, "Undergraduate", _, _), schedule(Course, _) } < 80.

% Total credits needed for graduation
:- career("Undergraduate"), #sum { Credits, Course : course(Course, Credits, _, _, _), schedule(Course, _) } < 120.

% Minimize the number of semesters
#minimize { S : semester(S), schedule(_, S) }.

#show schedule/2.
