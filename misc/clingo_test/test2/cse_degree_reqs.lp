% Load courses and their properties
% e.g., course(course_name, course_credits, career, is_offered_spring, is_offered_fall).

% Include the course data from your provided file
% #include "courses.lp".
% #include "courses.current.lp".

% NOTE:
%   - This kind of works.
%   - Try this for 1 semester.
%   - Try limiting certain courses to certain semesters. (e.g. CSE101 only in first semester)


% 1.
% Required intro courses
required_intro_course(cse220).
required_intro_course(X) :- course(X, _, _, _, _), X = cse215; X = cse150.
required_intro_course(X) :- course(X, _, _, _, _), X = cse114; X = cse214; X = cse216.

% Allow choice for one of these pairs to fulfill the requirement
1 { required_intro_course(cse215); required_intro_course(cse150) } 1.

% Choice rule for substitutions
completed_original_set :- required_intro_course(cse114), 
   required_intro_course(cse214), 
   required_intro_course(cse216).

completed_substitute_set :- required_intro_course(cse160), 
   required_intro_course(cse161), 
   required_intro_course(cse260), 
   required_intro_course(cse261).

1 { completed_original_set; completed_substitute_set } 1.

% 2.
% Required advanced courses
required_adv_course(X) :- course(X, _, _, _, _), X = cse303; X = cse350.
required_adv_course(X) :- course(X, _, _, _, _), X = cse373; X = cse385.
required_adv_course(X) :- course(X, _, _, _, _), X = cse310; X = cse316; X = cse320; X = cse416.

% Define choice rules for courses with alternatives
required_adv_course(cse310), required_adv_course(cse316), required_adv_course(cse320), required_adv_course(cse416).
1 { required_adv_course(cse303); required_adv_course(cse350) } 1.
1 { required_adv_course(cse373); required_adv_course(cse385) } 1.

% 3.
% CSE elective courses
cse_excluded_elective(X) :- course(X, _, _, _, _), X = cse475; X = cse495; X = cse496.

% Define a valid elective
valid_cse_elective(C) :- course(C, Credits, "Graduate", _, _), Credits >= 3, not cse_excluded_elective(C).

% Select exactly four valid electives
4 { cse_elective(C) : valid_cse_elective(C) } 4.

%%%%%%%%%%%%%%%%%%%%%%%%
% credit total check HERE >= 24 credits

% Define a rule to consider a course as selected if it's either a required or an elective course
selected(C) :- required_intro_course(C).
selected(C) :- required_adv_course(C).
selected(C) :- cse_elective(C).

% Calculate total credits from selected courses
% Shows marked selected courses with required_intro_course/1, required_adv_course/1, cse_elective/1 etc.
total_credits_1_thru_3(Total) :- Total = #sum { Credits, C : course(C, Credits, _, _, _), selected(C) }.

% Constraint to ensure at least 24 credits
:- total_credits_1_thru_3(Total), Total <= 24.

% % Example query to check the model
% #show selected/1.
% #show total_credits_1_thru_3/1.

%%%%%%%%%%%%%%%%%%%

% 4.
% Required math courses (1)
req_ams_mat_seq(X) :- course(X, _, _, _, _), X = ams151; X = ams161.
req_ams_mat_seq(X) :- course(X, _, _, _, _), X = mat125; X = mat126; X = mat127.
req_ams_mat_seq(X) :- course(X, _, _, _, _), X = mat131; X = mat132.

completed_ams_mat_seq_1 :- req_ams_mat_seq(ams151), req_ams_mat_seq(ams161).

completed_ams_mat_seq_2 :- req_ams_mat_seq(mat125), 
   req_ams_mat_seq(mat126), 
   req_ams_mat_seq(mat127).

completed_ams_mat_seq_3 :- req_ams_mat_seq(mat131),
    req_ams_mat_seq(mat132).

1 { completed_ams_mat_seq_1; completed_ams_mat_seq_2; completed_ams_mat_seq_3 } 1.

% 5.
% Required math courses (2)
course(mat211, _,_,_,_), course(ams210, _,_,_,_).

% 6.
%  Required AMS courses
req_ams_seq(X) :- course(X, _, _, _, _), X = ams301.
req_ams_seq(X) :- course(X, _, _, _, _), X = ams310; X = ams311.

1 { req_ams_seq(ams310); req_ams_seq(ams311) } 1.

% 7.
% Natural Science Lecture/Labs
req_nat_sci_lect_lab(X, Y) :- course(X, _, _, _, _), course(Y, _, _, _, _),
   X = bio201, Y = bio204;
   X = bio202, Y = bio204;
   X = bio203, Y = bio204;
   X = che131, Y = che133;
   X = che152, Y = che154;
   X = phy126, Y = phy133;
   X = phy131, Y = phy133;
   X = phy141, Y = phy133.

3 { req_nat_sci_lect_lab(bio201, bio204); 
    req_nat_sci_lect_lab(bio202, bio204); 
    req_nat_sci_lect_lab(bio203, bio204); 
    req_nat_sci_lect_lab(che131, che133); 
    req_nat_sci_lect_lab(che152, che154); 
    req_nat_sci_lect_lab(phy126, phy133); 
    req_nat_sci_lect_lab(phy131, phy133); 
    req_nat_sci_lect_lab(phy141, phy133) } 3.

% 8.
% Natural Science Lecture
req_nat_sci_lect(X) :- course(X, _, _, _, _), 
   X = ast203;
   X = ast205; 
   X = che132; 
   X = che321; 
   X = che322; 
   X = che331; 
   X = che332; 
   X = geo102; 
   X = geo103; 
   X = geo112; 
   X = geo113; 
   X = geo122; 
   X = phy125; 
   X = phy127; 
   X = phy132; 
   X = phy134; 
   X = phy142; 
   X = phy251; 
   X = phy252.

4 { req_nat_sci_lect(ast203);
    req_nat_sci_lect(ast205);
    req_nat_sci_lect(che132);
    req_nat_sci_lect(che321);
    req_nat_sci_lect(che322);
    req_nat_sci_lect(che331);
    req_nat_sci_lect(che332);
    req_nat_sci_lect(geo102);
    req_nat_sci_lect(geo103);
    req_nat_sci_lect(geo112);
    req_nat_sci_lect(geo113);
    req_nat_sci_lect(geo122);
    req_nat_sci_lect(phy125);
    req_nat_sci_lect(phy127);
    req_nat_sci_lect(phy132);
    req_nat_sci_lect(phy134);
    req_nat_sci_lect(phy142);
    req_nat_sci_lect(phy251);
    req_nat_sci_lect(phy252) } 4.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Credit total check HERE >= 9 credits
nat_lect_lab_selected(X,Y) :- req_nat_sci_lect_lab(X,Y).
nat_lect_selected(X) :- req_nat_sci_lect(X).

total_credits_nat_lect_lab(N) :-
    N = #sum { C,X : nat_lect_lab_selected(X, Y), course(X, C, _, _, _), course(Y, D, _, _, _) }.

total_credits_nat_lect(N) :-
    N = #sum { C,X : nat_lect_selected(X), course(X, C, _, _, _) }.

% Calculate total credits from selected courses
total_credits_7_thru_8(N) :-
    N = #sum { L : total_credits_nat_lect_lab(L) } , #sum { L : total_credits_nat_lect(L) }.

% Constraint to ensure at least 9 credits
:- total_credits_7_thru_8(Total), Total <= 9.

% % Example query to check the model
% #show nat_lect_lab_selected/2.
% #show nat_lect_selected/1.
% #show total_credits_7_thru_8/1.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% 9.
% Professional Ethics

req_prof_ethics(X) :- course(X, _, _, _, _), X = cse312.

1 { req_prof_ethics(cse312) } 1.

% 10.
% Upper Division Writing Requirement

req_upper_div_writing(X) :- course(X, _, _, _, _), X = cse300.

1 { req_upper_div_writing(cse300) } 1.