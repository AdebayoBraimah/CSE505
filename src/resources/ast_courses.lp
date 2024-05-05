% Course predicates
course(ast100, 1, "Undergraduate", 1, 1, 1, 1).
course(ast101, 3, "Undergraduate", 1, 1, 1, 1).
course(ast105, 3, "Undergraduate", 1, 1, 1, 1).
course(ast112, 1, "Undergraduate", 1, 1, 1, 1).
course(ast200, 1, "Undergraduate", 1, 1, 1, 1).
course(ast203, 4, "Undergraduate", 1, 1, 1, 1).
course(ast205, 3, "Undergraduate", 1, 1, 1, 1).
course(ast248, 3, "Undergraduate", 1, 1, 1, 1).
course(ast287, 0..3, "Undergraduate", 1, 1, 1, 1).
course(ast301, 3, "Undergraduate", 1, 1, 1, 1).
course(ast341, 3, "Undergraduate", 1, 1, 1, 1).
course(ast345, 0..1, "Undergraduate", 1, 1, 1, 1).
course(ast346, 3, "Undergraduate", 1, 1, 1, 1).
course(ast347, 3, "Undergraduate", 1, 1, 1, 1).
course(ast389, 3, "Undergraduate", 1, 1, 1, 1).
course(ast390, 3, "Undergraduate", 1, 1, 1, 1).
course(ast443, 4, "Undergraduate", 1, 1, 1, 1).
course(ast444, 0, "Undergraduate", 1, 1, 1, 1).
course(ast447, 1..3, "Undergraduate", 1, 1, 1, 1).
course(ast458, 0, "Undergraduate", 1, 1, 1, 1).
course(ast459, 0, "Undergraduate", 1, 1, 1, 1).
course(ast475, 3, "Undergraduate", 1, 1, 1, 1).
course(ast487, 0..6, "Undergraduate", 1, 1, 1, 1).

% Repeatable Courses
repeatable(ast390, _, 6).
repeatable(ast447, 2, _).

% Course Rules 

% Corequisites for AST112
:- course(ast112, 1, "Undergraduate", 1, 1, 1, 1), 
   not course(ast101, _, "Undergraduate", 1, 1, 1, 1). 

% Prerequisites for AST203
:- course(ast203, 4, "Undergraduate", 1, 1, 1, 1), 
   not course(phy125, _, "Undergraduate", _, _, _, _), 
   not course(phy131, _, "Undergraduate", _, _, _, _), 
   not course(phy141, _, "Undergraduate", _, _, _, _). 

% Prerequisites for AST205
:- course(ast205, 3, "Undergraduate", 1, 1, 1, 1), 
   not course(phy125, _, "Undergraduate", _, _, _, _), 
   not course(phy131, _, "Undergraduate", _, _, _, _), 
   not course(phy141, _, "Undergraduate", _, _, _, _). 

% Prerequisites for AST301
:- course(ast301, 3, "Undergraduate", 1, 1, 1, 1), 
   not course(mat125, _, "Undergraduate", _, _, _, _), 
   not course(ams151, _, "Undergraduate", _, _, _, _). 

:- course(ast301, 3, "Undergraduate", 1, 1, 1, 1), 
   not course(phy121, _, "Undergraduate", _, _, _, _), 
   not course(phy125, _, "Undergraduate", _, _, _, _), 
   not course(phy131, _, "Undergraduate", _, _, _, _), 
   not course(phy141, _, "Undergraduate", _, _, _, _). 

% Prerequisites for AST341
:- course(ast341, 3, "Undergraduate", 1, 1, 1, 1), 
   not course(ast203, _, "Undergraduate", _, _, _, _). 

:- course(ast341, 3, "Undergraduate", 1, 1, 1, 1), 
   not course(phy251, _, "Undergraduate", _, _, _, _). 

:- course(ast341, 3, "Undergraduate", 1, 1, 1, 1), 
   not course(phy277, _, "Undergraduate", _, _, _, _). 

:- course(ast341, 3, "Undergraduate", 1, 1, 1, 1), 
   not course(mat203, _, "Undergraduate", _, _, _, _), 
   not course(ams261, _, "Undergraduate", _, _, _, _). 

% Prerequisites for AST346
:- course(ast346, 3, "Undergraduate", 1, 1, 1, 1), 
   not course(ast203, _, "Undergraduate", _, _, _, _). 

:- course(ast346, 3, "Undergraduate", 1, 1, 1, 1), 
   not course(phy251, _, "Undergraduate", _, _, _, _). 

:- course(ast346, 3, "Undergraduate", 1, 1, 1, 1), 
   not course(mat203, _, "Undergraduate", _, _, _, _), 
   not course(ams261, _, "Undergraduate", _, _, _, _). 

% Prerequisites for AST347
:- course(ast347, 3, "Undergraduate", 1, 1, 1, 1), 
   not course(ast203, _, "Undergraduate", _, _, _, _). 

:- course(ast347, 3, "Undergraduate", 1, 1, 1, 1), 
   not course(phy251, _, "Undergraduate", _, _, _, _). 

:- course(ast347, 3, "Undergraduate", 1, 1, 1, 1), 
   not course(mat203, _, "Undergraduate", _, _, _, _), 
   not course(ams261, _, "Undergraduate", _, _, _, _). 

% Prerequisites for AST389
:- course(ast389, 3, "Undergraduate", 1, 1, 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _, _, _). 

% Prerequisites for AST390
:- course(ast390, 3, "Undergraduate", 1, 1, 1, 1), 
   not course(ast203, _, "Undergraduate", _, _, _, _), 
   not course(phy277, _, "Undergraduate", _, _, _, _), 
   not course(mat203, _, "Undergraduate", _, _, _, _), 
   not course(ams261, _, "Undergraduate", _, _, _, _). 

% Prerequisites for AST443
:- course(ast443, 4, "Undergraduate", 1, 1, 1, 1), 
   not course(ast203, _, "Undergraduate", _, _, _, _). 

:- course(ast443, 4, "Undergraduate", 1, 1, 1, 1), 
   not course(phy277, _, "Undergraduate", _, _, _, _). 

:- course(ast443, 4, "Undergraduate", 1, 1, 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _, _, _). 

% Prerequisites for AST444
:- course(ast444, 0, "Undergraduate", 1, 1, 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _, _, _). 

% Corequisites for AST458
:- course(ast458, 0, "Undergraduate", 1, 1, 1, 1), 
   not course(wrt102, _, "Undergraduate", 1, 1, 1, 1). 

% Prerequisites for AST459
:- course(ast459, 0, "Undergraduate", 1, 1, 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _, _, _). 

