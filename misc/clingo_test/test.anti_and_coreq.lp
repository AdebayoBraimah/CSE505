% NOTE: 
%   - This works.
%   - ',' == AND, ';' == OR
% 
%   - Command to run: clingo test.anti_and_coreq.lp test.data.2.lpgo

% NOTE: Corequisites for a course need to be written 
%      in separate rule bodies.
% 
% Rule to enforce antirequisites for CSE101
:- course(cse101, 3, "Undergraduate", 1, 1, 1, 1),
   course(cse114, _, "Undergraduate", _, _, _, _).

:- course(cse101, 3, "Undergraduate", 1, 1, 1, 1),
   course(cse160, _, "Undergraduate", _, _, _, _).

% Rule to enforce corequisites for CSE160
:- course(cse160, 3, "Undergraduate", 1, 1, 1, 1),
   not course(cse161, _, "Undergraduate", 1, 1, 1, 1).

% Rule to enforce prerequisites and corequisites for CSE220
:- course(cse220, 4, "Undergraduate", 1, 1, 1, 1),
   not course(cse214, _, "Undergraduate", _, _, _, _).

:- course(cse220, 4, "Undergraduate", 1, 1, 1, 1),
   not course(cse260, _, "Undergraduate", 1, 1, 1, 1).


% Rule to enforce prerequisites and corequisites for CSE260
:- course(cse260, 4, "Undergraduate", 1, 1, 1, 1),
   not course(cse160, _, "Undergraduate", _, _, _, _).

:- course(cse260, 4, "Undergraduate", 1, 1, 1, 1),
   not course(cse261, _, "Undergraduate", 1, 1, 1, 1).


% Rule to enforce prerequisites for CSE310
:- course(cse310, 3, "Undergraduate", 1, 1, 1, 1),
   not course(cse214, _, "Undergraduate", _, _, _, _).

:- course(cse310, 3, "Undergraduate", 1, 1, 1, 1),
   not course(cse220, _, "Undergraduate", _, _, _, _);
   not course(ise218, _, "Undergraduate", _, _, _, _).

% Rule to enforce corequisites for CSE310
:- course(cse310, 3, "Undergraduate", 1, 1, 1, 1),
   not course(ams310, _, "Undergraduate", 1, 1, 1, 1).
