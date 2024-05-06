% Course predicates
course(wrt101, 3, "Undergraduate", 1, 1).
course(wrt102, 3, "Undergraduate", 1, 1).
course(wrt200, 3, "Undergraduate", 1, 1).
course(wrt201, 3, "Undergraduate", 1, 1).
course(wrt206, 3, "Undergraduate", 1, 1).
course(wrt220, 3, "Undergraduate", 1, 1).
course(wrt300, 3, "Undergraduate", 1, 1).
course(wrt301, 3, "Undergraduate", 1, 1).
course(wrt302, 3, "Undergraduate", 1, 1).
course(wrt303, 3, "Undergraduate", 1, 1).
course(wrt304, 3, "Undergraduate", 1, 1).
course(wrt305, 3, "Undergraduate", 1, 1).
course(wrt306, 3, "Undergraduate", 1, 1).
course(wrt307, 3, "Undergraduate", 1, 1).
course(wrt319, 3, "Undergraduate", 1, 1).
course(wrt321, 3, "Undergraduate", 1, 1).
course(wrt375, 3, "Undergraduate", 1, 1).
course(wrt376, 3, "Undergraduate", 1, 1).
course(wrt377, 3, "Undergraduate", 1, 1).
course(wrt380, 3, "Undergraduate", 1, 1).
course(wrt381, 3, "Undergraduate", 1, 1).
course(wrt382, 3, "Undergraduate", 1, 1).
course(wrt392, 3, "Undergraduate", 1, 1).
course(wrt444, 0, "Undergraduate", 1, 1).
course(wrt458, 0, "Undergraduate", 1, 1).
course(wrt459, 0, "Undergraduate", 1, 1).
course(wrt487, 0..6, "Undergraduate", 1, 1).
course(wrt488, 0..6, "Undergraduate", 1, 1).
course(wrt490, 3, "Undergraduate", 1, 1).
course(wrt506, 3, "Graduate", 1, 1).
course(wrt509, 3, "Graduate", 1, 1).
course(wrt592, 3, "Graduate", 1, 1).
course(wrt605, 3, "Graduate", 1, 1).
course(wrt612, 3, "Graduate", 1, 1).
course(wrt613, 3, "Graduate", 1, 1).
course(wrt614, 3, "Graduate", 1, 1).
course(wrt621, 1..3, "Graduate", 1, 1).
course(wrt687, 0..12, "Graduate", 1, 1).
course(wrt690, 0..12, "Graduate", 1, 1).
course(wrt698, 3, "Graduate", 1, 1).

% Course Rules 

% Prerequisites for WRT200
:- course(wrt200, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT201
:- course(wrt201, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT206
:- course(wrt206, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT220
:- course(wrt220, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT300
:- course(wrt300, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

:- course(wrt300, 3, "Undergraduate", 1, 1), 
   not course(com100, _, "Undergraduate", _, _). 

% Prerequisites for WRT301
:- course(wrt301, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT302
:- course(wrt302, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT303
:- course(wrt303, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT304
:- course(wrt304, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT305
:- course(wrt305, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT306
:- course(wrt306, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT307
:- course(wrt307, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT319
:- course(wrt319, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT321
:- course(wrt321, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT375
:- course(wrt375, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT376
:- course(wrt376, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT377
:- course(wrt377, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT380
:- course(wrt380, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT381
:- course(wrt381, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT382
:- course(wrt382, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT392
:- course(wrt392, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Corequisites for WRT458
:- course(wrt458, 0, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", 1, 1). 

% Prerequisites for WRT459
:- course(wrt459, 0, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT487
:- course(wrt487, 0..6, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT488
:- course(wrt488, 0..6, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for WRT490
:- course(wrt490, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

:- course(wrt490, 3, "Undergraduate", 1, 1), 
   not course(wrt300, _, "Undergraduate", _, _). 

% Prerequisites for WRT612
:- course(wrt612, 3, "Graduate", 1, 1), 
   not course(egl592, _, "Graduate", _, _), 
   not course(egl698, _, "Graduate", _, _). 

% Prerequisites for WRT613
:- course(wrt613, 3, "Graduate", 1, 1), 
   not course(egl592, _, "Graduate", _, _), 
   not course(egl698, _, "Graduate", _, _). 

