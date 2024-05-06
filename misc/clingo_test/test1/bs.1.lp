% Load course data
#include "cse_courses.lp".

% Define semesters dynamically, considering an arbitrary upper limit
#const max_semesters = 12.
semester(1..max_semesters).

% Assign courses to semesters based on whether they are offered in the spring or fall
1 { take(C, N, Cr, Car, S, F, Sem) : semester(Sem) } 1 :-
    course(C, N, Cr, Car, S, F), F=1.
1 { take(C, N, Cr, Car, S, F, Sem) : semester(Sem) } 1 :-
    course(C, N, Cr, Car, S, F), S=1.

% Constraint to not schedule courses already taken
:- course_taken(Name), take(Name, _, _, _, _, _, _).

% Prerequisite constraints (revised for safety)
:- take(C2, _, _, Car, _, _, Sem2), 
   prereq(C1, C2),
   course(C1, _, Car, _, _),
   not take(C1, _, _, Car, _, _, Sem1),
   semester(Sem1),
   Sem1 < Sem2.

% Anti-requisite constraints
:- take(C1, _, _, Car, _, _, Sem), 
   take(C2, _, _, Car, _, _, Sem),
   antireq(C1, C2).

% Co-requisite constraints
:- take(C1, _, _, Car, _, _, Sem), 
   not take(C2, _, _, Car, _, _, Sem),
   coreq(C1, C2).

% Compute total credits accumulated
total_credits(TotalCredits) :- 
    TotalCredits = #sum { Cr : take(_, _, Cr, _, _, _, _) }.

% Compute total major credits accumulated for undergraduate courses
major_credits(MajorCredits) :- 
    MajorCredits = #sum { Cr : take(_, _, Cr, "Undergraduate", _, _, _) }.

% Check for minimum and maximum credits per semester
credits_per_semester(Sem, Credits) :-
    Credits = #sum { Cr : take(_, _, Cr, _, _, _, Sem) },
    semester(Sem).
:- semester(S), credits_per_semester(S, C), C < 12.
:- semester(S), credits_per_semester(S, C), C > 18.

% Minimize semesters used
#minimize { 1@1,Sem : semester(Sem), take(_, _, _, _, _, _, Sem) }.
