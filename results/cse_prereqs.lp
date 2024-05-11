% Load courses and their properties
% e.g., course(course_name, course_credits, career, is_offered_spring, is_offered_fall).

% Non-CSE Courses

course(ast203, 4, "Undergraduate", 1, 1).
course(ast205, 3, "Undergraduate", 1, 1).

course(ams110, 3, "Undergraduate", 1, 1).
course(ams151, 3, "Undergraduate", 1, 1).
course(ams161, 3, "Undergraduate", 1, 1).
course(ams210, 3, "Undergraduate", 1, 1).
course(ams301, 3, "Undergraduate", 1, 1).
course(ams310, 3, "Undergraduate", 1, 1).
course(ams311, 3, "Undergraduate", 1, 1).
course(ams412, 3, "Undergraduate", 1, 1).

course(bio201, 3, "Undergraduate", 1, 1).
course(bio202, 3, "Undergraduate", 1, 1).
course(bio203, 3, "Undergraduate", 1, 1).
course(bio204, 2, "Undergraduate", 1, 1).

course(che129, 4, "Undergraduate", 1, 1).
course(che131, 4, "Undergraduate", 1, 1).
course(che132, 4, "Undergraduate", 1, 1).
course(che133, 1, "Undergraduate", 1, 1).
course(che152, 4, "Undergraduate", 1, 1).
course(che154, 2, "Undergraduate", 1, 1).
course(che321, 4, "Undergraduate", 1, 1).
course(che322, 4, "Undergraduate", 1, 1).
course(che331, 4, "Undergraduate", 1, 1).
course(che332, 4, "Undergraduate", 1, 1).

course(geo102, 3, "Undergraduate", 1, 1).
course(geo103, 3, "Undergraduate", 1, 1).
course(geo112, 1, "Undergraduate", 1, 1).
course(geo113, 1, "Undergraduate", 1, 1).
course(geo122, 4, "Undergraduate", 1, 1).

course(ise108, 3, "Undergraduate", 1, 1).
course(ise334, 3, "Undergraduate", 1, 1).

course(mat123, 3, "Undergraduate", 1, 1).
course(mat125, 3, "Undergraduate", 1, 1).
course(mat126, 3, "Undergraduate", 1, 1).
course(mat127, 3, "Undergraduate", 1, 1).
course(mat131, 4, "Undergraduate", 1, 1).
course(mat200, 3, "Undergraduate", 1, 1).
course(mat211, 3, "Undergraduate", 1, 1).
course(mat250, 4, "Undergraduate", 1, 1).

course(phy125, 3, "Undergraduate", 1, 1).
course(phy126, 3, "Undergraduate", 1, 1).
course(phy127, 3, "Undergraduate", 1, 1).
course(phy131, 3, "Undergraduate", 1, 1).
course(phy132, 3, "Undergraduate", 1, 1).
course(phy133, 1, "Undergraduate", 1, 1).
course(phy134, 1, "Undergraduate", 1, 1).
course(phy141, 3, "Undergraduate", 1, 1).
course(phy142, 3, "Undergraduate", 1, 1).
% course(phy251, 3, "Undergraduate", 1, 1).
% course(phy252, 1, "Undergraduate", 1, 1).

course(wrt101, 3, "Undergraduate", 1, 1).
course(wrt102, 3, "Undergraduate", 1, 1).

% AST Prerequisites
% Prerequisites for AST203
:- course(ast203, 4, "Undergraduate", 1, 1), 
   not course(phy125, _, "Undergraduate", _, _), 
   not course(phy131, _, "Undergraduate", _, _), 
   not course(phy141, _, "Undergraduate", _, _). 

% Prerequisites for AST205
:- course(ast205, 3, "Undergraduate", 1, 1), 
   not course(phy125, _, "Undergraduate", _, _), 
   not course(phy131, _, "Undergraduate", _, _), 
   not course(phy141, _, "Undergraduate", _, _).

% AMS Prerequisites
% Prerequisites for AMS110
:- course(ams110, 3, "Undergraduate", 1, 1), 
   not course(ams151, _, "Undergraduate", _, _), 
   not course(mat125, _, "Undergraduate", _, _).

% Prerequisites for AMS151
:- course(ams151, 3, "Undergraduate", 1, 1), 
   not course(mat123, _, "Undergraduate", _, _). 

% Prerequisites for AMS310
:- course(ams310, 3, "Undergraduate", 1, 1), 
   not course(ams161, _, "Undergraduate", _, _), 
   not course(mat132, _, "Undergraduate", _, _), 
   not course(mat127, _, "Undergraduate", _, _), 
   not course(mat142, _, "Undergraduate", _, _).

% Prerequisites for AMS161
:- course(ams161, 3, "Undergraduate", 1, 1), 
   not course(ams151, _, "Undergraduate", _, _), 
   not course(mat131, _, "Undergraduate", _, _). 

% Prerequisites for AMS210
:- course(ams210, 3, "Undergraduate", 1, 1), 
   not course(ams151, _, "Undergraduate", _, _), 
   not course(mat131, _, "Undergraduate", _, _).

% Prerequisites for AMS301
:- course(ams301, 3, "Undergraduate", 1, 1), 
   not course(ams210, _, "Undergraduate", _, _), 
   not course(mat211, _, "Undergraduate", _, _), 
   not course(ams361, _, "Undergraduate", _, _), 
   not course(mat303, _, "Undergraduate", _, _). 

% Prerequisites for AMS310
:- course(ams310, 3, "Undergraduate", 1, 1), 
   not course(ams161, _, "Undergraduate", _, _), 
   not course(mat132, _, "Undergraduate", _, _), 
   not course(mat127, _, "Undergraduate", _, _), 
   not course(mat142, _, "Undergraduate", _, _). 

% Prerequisites for AMS311
:- course(ams311, 3, "Undergraduate", 1, 1), 
   not course(ams301, _, "Undergraduate", _, _).

% Prerequisites for AMS412
:- course(ams412, 3, "Undergraduate", 1, 1), 
   not course(ams311, _, "Undergraduate", _, _).

% BIO Prerequisites
% Prerequisites for BIO202
:- course(bio202, 3, "Undergraduate", 1, 1), 
   not course(che129, _, "Undergraduate", _, _), 
   not course(che131, _, "Undergraduate", _, _). 

% Prerequisites for BIO203
:- course(bio203, 3, "Undergraduate", 1, 1), 
   not course(che129, _, "Undergraduate", _, _), 
   not course(che131, _, "Undergraduate", _, _).

% Prequisites for BIO204
:- course(bio204, 2, "Undergraduate", 1, 1), 
   not course(che152, _, "Undergraduate", _, _).

% CHE Prerequisites
% Prerequisites for CHE129
:- course(che129, 4, "Undergraduate", 1, 1), 
   not course(mat123, _, "Undergraduate", _, _). 

% Prerequisites for CHE131
:- course(che131, 4, "Undergraduate", 1, 1), 
   not course(mat125, _, "Undergraduate", _, _).

% Corequisites for CHE133
:- course(che133, 1, "Undergraduate", 1, 1), 
   not course(che129, _, "Undergraduate", _, _).

% Prerequisites for CHE152
:- course(che152, 4, "Undergraduate", 1, 1), 
   not course(mat131, _, "Undergraduate", _, _), 
   not course(mat125, _, "Undergraduate", _, _), 
   not course(ams151, _, "Undergraduate", _, _). 

% Corequisites for CHE154
:- course(che154, 2, "Undergraduate", 1, 1), 
   not course(che152, _, "Undergraduate", _, _).

% Prerequisites for CHE331
:- course(che331, 4, "Undergraduate", 1, 1), 
   not course(che152, _, "Undergraduate", _, _).

% GEO Prerequisites
%  Prequisites for GEO112
:- course(geo112, 1, "Undergraduate", 1, 1), 
   not course(geo102, _, "Undergraduate", _,_). 

% Prequisites for GEO113
:- course(geo113, 1, "Undergraduate", 1, 1), 
   not course(geo103, _, "Undergraduate", _,_). 

% MAT Prerequisites
% Prerequisites for MAT125
:- course(mat125, 3, "Undergraduate", 1, 1), 
   not course(mat123, _, "Undergraduate", _, _).

% Prerequisites for MAT127
:- course(mat127, 3, "Undergraduate", 1, 1), 
   not course(mat126, _, "Undergraduate", _, _).

% Prerequisites for MAT131
:- course(mat131, 4, "Undergraduate", 1, 1), 
   not course(mat123, _, "Undergraduate", _, _). 

% Prerequisites for MAT211
:- course(mat211, 3, "Undergraduate", 1, 1), 
   not course(ams151, _, "Undergraduate", _, _), 
   not course(mat131, _, "Undergraduate", _, _), 
   not course(mat126, _, "Undergraduate", _, _). 

% Prerequisites for MAT250
:- course(mat250, 4, "Undergraduate", 1, 1), 
   not course(mat131, _, "Undergraduate", _, _). 

% PHY Prerequisites
% Prerequisites for PHY125
:- course(phy125, 3, "Undergraduate", 1, 1), 
   not course(mat123, _, "Undergraduate", _, _). 

% Prerequisites for PHY126
:- course(phy126, 3, "Undergraduate", 1, 1), 
   not course(phy125, _, "Undergraduate", _, _). 

% Prequisites for PHY126
:- course(phy126, 3, "Undergraduate", 1, 1), 
   not course(mat126, _, "Undergraduate", _, _). 

:- course(phy126, 3, "Undergraduate", 1, 1), 
   not course(ams161, _, "Undergraduate", _, _).

% Prerequisites for PHY127
:- course(phy127, 3, "Undergraduate", 1, 1), 
   not course(phy125, _, "Undergraduate", _, _). 

% Prerequisites for PHY131
:- course(phy131, 3, "Undergraduate", 1, 1), 
   not course(mat123, _, "Undergraduate", _, _). 

% Prequisites for PHY131
:- course(phy131, 3, "Undergraduate", 1, 1), 
   not course(mat125, _, "Undergraduate", _, _). 

:- course(phy131, 3, "Undergraduate", 1, 1), 
   not course(mat131, _, "Undergraduate", _, _). 

:- course(phy131, 3, "Undergraduate", 1, 1), 
   not course(ams151, _, "Undergraduate", _, _).

% Prerequisites for PHY132
:- course(phy132, 3, "Undergraduate", 1, 1), 
   not course(phy131, _, "Undergraduate", _, _), 
   not course(phy141, _, "Undergraduate", _, _). 

% Prequisites for PHY133
:- course(phy133, 1, "Undergraduate", 1, 1), 
   not course(phy125, _, "Undergraduate", _, _). 

:- course(phy133, 1, "Undergraduate", 1, 1), 
   not course(phy126, _, "Undergraduate", _, _). 

:- course(phy133, 1, "Undergraduate", 1, 1), 
   not course(phy131, _, "Undergraduate", _, _).  

% Prerequisites for PHY134
:- course(phy134, 1, "Undergraduate", 1, 1), 
   not course(phy133, _, "Undergraduate", _, _). 

% Corequisites for PHY141
:- course(phy141, 3, "Undergraduate", 1, 1), 
   not course(mat131, _, "Undergraduate", _, _). 

:- course(phy141, 3, "Undergraduate", 1, 1), 
   not course(ams151, _, "Undergraduate", _, _).

% Prerequisites for PHY142
:- course(phy142, 3, "Undergraduate", 1, 1), 
   not course(phy141, _, "Undergraduate", _, _). 

% :- course(phy251, 3, "Undergraduate", 1, 1), 
%    not course(mat307, _, "Undergraduate", 1, 1). 

% ISE Prerequisites

% WRT Prerequisites
% Prerequisites for WRT102
:- course(wrt102, 3, "Undergraduate", 1, 1), 
   not course(wrt101, _, "Undergraduate", _, _). 
