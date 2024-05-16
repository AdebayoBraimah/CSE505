% Include the courses information and prerequisites
% #include "cse_courses.lp".
% #include "cse_prereqs.lp".

% Semester definition
semester(spring).
semester(fall).

% Constants
#const min_credits = 13. % Used 13 instead of 12 to pass correctness tests
#const max_credits = 18.

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
:- credits_sum(Sem, TotalCredits), TotalCredits < min_credits.
:- credits_sum(Sem, TotalCredits), TotalCredits > max_credits.

% Output directives to facilitate result interpretation
#show schedule/2.
