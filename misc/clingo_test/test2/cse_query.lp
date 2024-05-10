% Load courses and their properties
% e.g., course(course_name, course_credits, career, is_offered_spring, is_offered_fall).

% Include the course data from your provided file
% #include "courses.lp".
% #include "courses.current.lp".

% NOTE:
%   - This kind of works.
%   - Try this for 1 semester.
%   - Try limiting certain courses to certain semesters. (e.g. CSE101 only in first semester)


% Query

% Define constants
#const max_semesters = 12.
#const min_credits_per_semester = 12.
#const max_credits_per_semester = 18.

% Define possible semesters
semester(1..max_semesters).

% Schedule courses across semesters
1 { schedule(Course, Sem) : semester(Sem) } 1 :- course(Course, Credits, Career, Spring, Fall).

% Prevent scheduling of courses already taken
:- course_taken(Course), schedule(Course, _).

% course_taken(cse101).
% course_taken(ams110).
% course_taken(ams151).
% course_taken(mat131).
% course_taken(mat123).
% course_taken(mat125).
% course_taken(bio201).
% course_taken(bio204).


% Semester limits: at least 12 credits and at most 18 credits per semester
:- semester(Sem), SemCredits = #count { Credits, Course : schedule(Course, Sem), course(Course, Credits, "Undergraduate", _, _) }, SemCredits < min_credits_per_semester.
:- semester(Sem), SemCredits = #count { Credits, Course : schedule(Course, Sem), course(Course, Credits, "Undergraduate", _, _) }, SemCredits > max_credits_per_semester.

% Ensure all scheduled courses comply with seasonal offerings
:- schedule(Course, Sem), course(Course, _, "Undergraduate", Spring, Fall), 
   Sem \ 2 = 1, Fall = 0.
:- schedule(Course, Sem), course(Course, _, "Undergraduate", Spring, Fall), 
   Sem \ 2 = 0, Spring = 0.

% Count total credits and major credits
total_credits(Total) :- Total = #sum { Credits, Course : schedule(Course, _), course(Course, Credits, "Undergraduate", _, _) }.
major_credits(Major) :- Major = #sum { Credits, Course : schedule(Course, _), course(Course, Credits, "Undergraduate", _, _) }.

% Graduation requirements
:- total_credits(Total), Total < 120.
:- major_credits(Major), Major < 80.

% Objective to minimize the number of semesters
#minimize { 1, Sem : schedule(_, Sem) }.

#show schedule/2.