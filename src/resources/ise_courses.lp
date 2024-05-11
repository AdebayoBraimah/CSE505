% Course atoms
course(ise102, 3, "Undergraduate", 1, 1).
course(ise108, 3, "Undergraduate", 1, 1).
course(ise208, 3, "Undergraduate", 1, 1).
course(ise218, 3, "Undergraduate", 1, 1).
course(ise300, 3, "Undergraduate", 1, 1).
course(ise301, 3, "Undergraduate", 1, 1).
course(ise305, 3, "Undergraduate", 1, 1).
course(ise311, 3, "Undergraduate", 1, 1).
course(ise312, 3, "Undergraduate", 1, 1).
course(ise316, 3, "Undergraduate", 1, 1).
course(ise317, 3, "Undergraduate", 1, 1).
course(ise320, 3, "Undergraduate", 1, 1).
course(ise321, 3, "Undergraduate", 1, 1).
course(ise323, 3, "Undergraduate", 1, 1).
course(ise325, 3, "Undergraduate", 1, 1).
course(ise331, 3, "Undergraduate", 1, 1).
course(ise332, 3, "Undergraduate", 1, 1).
course(ise333, 3, "Undergraduate", 1, 1).
course(ise334, 3, "Undergraduate", 1, 1).
course(ise337, 3, "Undergraduate", 1, 1).
course(ise339, 3, "Undergraduate", 1, 1).
course(ise340, 3, "Undergraduate", 1, 1).
course(ise364, 3, "Undergraduate", 1, 1).
course(ise369, 3, "Undergraduate", 1, 1).
course(ise377, 3, "Undergraduate", 1, 1).
course(ise378, 3, "Undergraduate", 1, 1).
course(ise390, 3, "Undergraduate", 1, 1).
course(ise391, 3, "Undergraduate", 1, 1).
course(ise392, 3, "Undergraduate", 1, 1).
course(ise393, 3, "Undergraduate", 1, 1).
course(ise475, 3, "Undergraduate", 1, 1).
course(ise487, 0..6, "Undergraduate", 1, 1).
course(ise488, 3, "Undergraduate", 1, 1).
course(ise503, 3, "Graduate", 1, 1).
course(ise506, 3, "Graduate", 1, 1).
course(ise507, 3, "Graduate", 1, 1).

% Course Rules 

% Prerequisites for ISE102
:- course(ise102, 3, "Undergraduate", 1, 1), 
   not course(cse101, _, "Undergraduate", _, _). 

% Prerequisites for ISE208
:- course(ise208, 3, "Undergraduate", 1, 1), 
   not course(ise108, _, "Undergraduate", _, _). 

% Prerequisites for ISE218
:- course(ise218, 3, "Undergraduate", 1, 1), 
   not course(mat123, _, "Undergraduate", _, _). 

% Prerequisites for ISE300
:- course(ise300, 3, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for ISE305
:- course(ise305, 3, "Undergraduate", 1, 1), 
   not course(ise208, _, "Undergraduate", _, _), 
   not course(cse114, _, "Undergraduate", _, _), 
   not course(cse230, _, "Undergraduate", _, _). 

% Prerequisites for ISE311
:- course(ise311, 3, "Undergraduate", 1, 1), 
   not course(cse214, _, "Undergraduate", _, _), 
   not course(cse230, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _), 
   not course(ise208, _, "Undergraduate", _, _). 

% Prerequisites for ISE316
:- course(ise316, 3, "Undergraduate", 1, 1), 
   not course(cse114, _, "Undergraduate", _, _), 
   not course(ise208, _, "Undergraduate", _, _). 

:- course(ise316, 3, "Undergraduate", 1, 1), 
   not course(mat123, _, "Undergraduate", _, _). 

% Prerequisites for ISE317
:- course(ise317, 3, "Undergraduate", 1, 1), 
   not course(ise316, _, "Undergraduate", _, _), 
   not course(cse310, _, "Undergraduate", _, _). 

% Prerequisites for ISE321
:- course(ise321, 3, "Undergraduate", 1, 1), 
   not course(ise316, _, "Undergraduate", _, _), 
   not course(cse310, _, "Undergraduate", _, _). 

% Prerequisites for ISE323
:- course(ise323, 3, "Undergraduate", 1, 1), 
   not course(cse214, _, "Undergraduate", _, _), 
   not course(cse230, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _), 
   not course(ise208, _, "Undergraduate", _, _). 

% Prerequisites for ISE325
:- course(ise325, 3, "Undergraduate", 1, 1), 
   not course(cse110, _, "Undergraduate", _, _), 
   not course(cse101, _, "Undergraduate", _, _), 
   not course(cse114, _, "Undergraduate", _, _). 

% Prerequisites for ISE331
:- course(ise331, 3, "Undergraduate", 1, 1), 
   not course(ise218, _, "Undergraduate", _, _), 
   not course(cse220, _, "Undergraduate", _, _). 

% Corequisites for ISE331
:- course(ise331, 3, "Undergraduate", 1, 1), 
   not course(ise316, _, "Undergraduate", 1, 1). 

:- course(ise331, 3, "Undergraduate", 1, 1), 
   not course(cse310, _, "Undergraduate", 1, 1). 

% Prerequisites for ISE332
:- course(ise332, 3, "Undergraduate", 1, 1), 
   not course(cse214, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

:- course(ise332, 3, "Undergraduate", 1, 1), 
   not course(mat211, _, "Undergraduate", _, _), 
   not course(ams210, _, "Undergraduate", _, _). 

:- course(ise332, 3, "Undergraduate", 1, 1), 
   not course(ams110, _, "Undergraduate", _, _), 
   not course(ams310, _, "Undergraduate", _, _). 

% Prerequisites for ISE333
:- course(ise333, 3, "Undergraduate", 1, 1), 
   not course(cse214, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

% Prerequisites for ISE337
:- course(ise337, 3, "Undergraduate", 1, 1), 
   not course(cse214, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

% Prerequisites for ISE364
:- course(ise364, 3, "Undergraduate", 1, 1), 
   not course(ise334, _, "Undergraduate", _, _). 

% Prerequisites for ISE369
:- course(ise369, 3, "Undergraduate", 1, 1), 
   not course(cse101, _, "Undergraduate", _, _), 
   not course(cse114, _, "Undergraduate", _, _), 
   not course(iae101, _, "Undergraduate", _, _). 

:- course(ise369, 3, "Undergraduate", 1, 1), 
   not course(ams102, _, "Undergraduate", _, _), 
   not course(ams110, _, "Undergraduate", _, _), 
   not course(ams310, _, "Undergraduate", _, _), 
   not course(pol201, _, "Undergraduate", _, _), 
   not course(pol102, _, "Undergraduate", _, _). 

% Prerequisites for ISE377
:- course(ise377, 3, "Undergraduate", 1, 1), 
   not course(ams161, _, "Undergraduate", _, _), 
   not course(mat127, _, "Undergraduate", _, _). 

:- course(ise377, 3, "Undergraduate", 1, 1), 
   not course(ams210, _, "Undergraduate", _, _), 
   not course(mat211, _, "Undergraduate", _, _). 

% Prerequisites for ISE378
:- course(ise378, 3, "Undergraduate", 1, 1), 
   not course(ams161, _, "Undergraduate", _, _), 
   not course(mat127, _, "Undergraduate", _, _). 

:- course(ise378, 3, "Undergraduate", 1, 1), 
   not course(ams210, _, "Undergraduate", _, _), 
   not course(mat211, _, "Undergraduate", _, _), 
   not course(mec262, _, "Undergraduate", _, _). 

% Prerequisites for ISE390
:- course(ise390, 3, "Undergraduate", 1, 1), 
   not course(cse214, _, "Undergraduate", _, _). 

% Prerequisites for ISE391
:- course(ise391, 3, "Undergraduate", 1, 1), 
   not course(cse214, _, "Undergraduate", _, _). 

% Prerequisites for ISE393
:- course(ise393, 3, "Undergraduate", 1, 1), 
   not course(cse214, _, "Undergraduate", _, _). 

