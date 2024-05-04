% NOTE: This works -- use this as a template
% 
% TODO: Create python function that generates these atoms

% Define possible prerequisite fulfillment
prerequisite_fulfilled(cse303, 1) :- course(cse160, 3, "Undergraduate", 1, 1, 1, 1).
prerequisite_fulfilled(cse303, 1) :- course(cse214, 3, "Undergraduate", 1, 1, 1, 1).
prerequisite_fulfilled(cse303, 2) :- course(cse150, 3, "Undergraduate", 1, 1, 1, 1).
prerequisite_fulfilled(cse303, 2) :- course(cse215, 3, "Undergraduate", 1, 1, 1, 1).

% TODO: Create python function that generates: 
%   - prequisite_fulfilled atoms
%   - corequisite_fulfilled atoms
%   - antirequisite_fulfilled atoms
%   - course_fulfilled/taken atoms

% Define that cse303 can be taken if all prerequisite conditions are fulfilled
:- course(cse303, 3, "Undergraduate", 1, 1, 1, 1), 
   not prerequisite_fulfilled(cse303, 1),
   not prerequisite_fulfilled(cse303, 2).
