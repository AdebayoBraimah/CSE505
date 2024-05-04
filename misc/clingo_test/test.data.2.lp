% NOTE: 
%   - Command to run: clingo test.anti_and_coreq.lp test.data.2.lpgo

% Test Case 1: Valid enrollment for CSE220 with prerequisites and corequisites met
course(cse214, 3, "Undergraduate", 1, 1, 1, 1).
course(cse260, 4, "Undergraduate", 1, 1, 1, 1).
course(cse220, 4, "Undergraduate", 1, 1, 1, 1).

% Test Case 2: Invalid enrollment for CSE310 - missing corequisite AMS310
course(cse214, 3, "Undergraduate", 1, 1, 1, 1).
% course(cse220, 4, "Undergraduate", 1, 1, 1, 1).
course(cse310, 3, "Undergraduate", 1, 1, 1, 1).
course(ams310, 3, "Undergraduate", 1, 1, 1, 1).
course(ise218, 4, "Undergraduate", 1, 1, 1, 1).

% Test Case 3: Valid check for antirequisites for CSE101
course(cse101, 3, "Undergraduate", 1, 1, 1, 1).

% Test Case 4: Invalid check for antirequisites for CSE101 (has taken CSE160)
course(cse160, 3, "Undergraduate", 1, 1, 1, 1).
course(cse101, 3, "Undergraduate", 1, 1, 1, 1).

% Test Case 5: Valid check for corequisites for CSE160
course(cse161, 3, "Undergraduate", 1, 1, 1, 1).

% Test Case 6: Valid check for corequisites for CSE260
course(cse261, 3, "Undergraduate", 1, 1, 1, 1).
