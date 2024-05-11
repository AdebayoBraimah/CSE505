% Include the courses information and prerequisites
% #include "cse_courses.lp".
% #include "cse_prereqs.lp".

% Semester definition
semester(spring).
semester(fall).

% Scheduling a course in a semester
{ schedule(Course, spring) : course(Course, Credits, Career, 1, OfferedFall) } :-
    not course_taken(Course).

{ schedule(Course, fall) : course(Course, Credits, Career, OfferedSpring, 1) } :-
    not course_taken(Course).

% Credit calculation per semester
credits_sum(Sem, TotalCredits) :-
    semester(Sem),
    TotalCredits = #sum { Credits, Course : schedule(Course, Sem), course(Course, Credits, _, _, _) }.

% Enforce credit limits
:- credits_sum(Sem, TotalCredits), TotalCredits < 12.
:- credits_sum(Sem, TotalCredits), TotalCredits > 18.

% Output directives to facilitate result interpretation
#show schedule/2.
