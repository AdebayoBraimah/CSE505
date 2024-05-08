% Course predicates
course(esg100, 3, "Undergraduate", 1, 1).
course(esg111, 3, "Undergraduate", 1, 1).
course(esg198, 3, "Undergraduate", 1, 1).
course(esg199, 0..3, "Undergraduate", 1, 1).
course(esg201, 3, "Undergraduate", 1, 1).
course(esg281, 3, "Undergraduate", 1, 1).
course(esg300, 0, "Undergraduate", 1, 1).
course(esg302, 3, "Undergraduate", 1, 1).
course(esg312, 4, "Undergraduate", 1, 1).
course(esg316, 4, "Undergraduate", 1, 1).
course(esg332, 3, "Undergraduate", 1, 1).
course(esg333, 3, "Undergraduate", 1, 1).
course(esg375, 1, "Undergraduate", 1, 1).
course(esg420, 3, "Undergraduate", 1, 1).
course(esg440, 3, "Undergraduate", 1, 1).
course(esg441, 3, "Undergraduate", 1, 1).
course(esg487, 0..3, "Undergraduate", 1, 1).

% Course Rules 

% Prerequisites for ESG281
:- course(esg281, 3, "Undergraduate", 1, 1), 
   not course(phy132, _, "Undergraduate", _, _). 

% Prerequisites for ESG300
:- course(esg300, 0, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Corequisites for ESG300
:- course(esg300, 0, "Undergraduate", 1, 1), 
   not course(esg312, _, "Undergraduate", 1, 1). 

% Prerequisites for ESG302
:- course(esg302, 3, "Undergraduate", 1, 1), 
   not course(esg198, _, "Undergraduate", _, _), 
   not course(che131, _, "Undergraduate", _, _), 
   not course(che152, _, "Undergraduate", _, _). 

:- course(esg302, 3, "Undergraduate", 1, 1), 
   not course(ams261, _, "Undergraduate", _, _). 

% Corequisites for ESG302
:- course(esg302, 3, "Undergraduate", 1, 1), 
   not course(ams361, _, "Undergraduate", 1, 1). 

:- course(esg302, 3, "Undergraduate", 1, 1), 
   not course(che132, _, "Undergraduate", 1, 1). 

:- course(esg302, 3, "Undergraduate", 1, 1), 
   not course(che154, _, "Undergraduate", 1, 1). 

% Prerequisites for ESG312
:- course(esg312, 4, "Undergraduate", 1, 1), 
   not course(phy126, _, "Undergraduate", _, _). 

:- course(esg312, 4, "Undergraduate", 1, 1), 
   not course(phy132, _, "Undergraduate", _, _). 

% Corequisites for ESG312
:- course(esg312, 4, "Undergraduate", 1, 1), 
   not course(esg300, _, "Undergraduate", 1, 1). 

% Prerequisites for ESG316
:- course(esg316, 4, "Undergraduate", 1, 1), 
   not course(esg100, _, "Undergraduate", _, _). 

:- course(esg316, 4, "Undergraduate", 1, 1), 
   not course(ams161, _, "Undergraduate", _, _), 
   not course(mat127, _, "Undergraduate", _, _), 
   not course(mat132, _, "Undergraduate", _, _), 
   not course(mat142, _, "Undergraduate", _, _), 
   not course(mat171, _, "Undergraduate", _, _). 

% Prerequisites for ESG332
:- course(esg332, 3, "Undergraduate", 1, 1), 
   not course(che131, _, "Undergraduate", _, _). 

:- course(esg332, 3, "Undergraduate", 1, 1), 
   not course(che133, _, "Undergraduate", _, _), 
   not course(mec301, _, "Undergraduate", _, _). 

% Prerequisites for ESG333
:- course(esg333, 3, "Undergraduate", 1, 1), 
   not course(esg281, _, "Undergraduate", _, _), 
   not course(phy251, _, "Undergraduate", _, _). 

:- course(esg333, 3, "Undergraduate", 1, 1), 
   not course(esg302, _, "Undergraduate", _, _), 
   not course(cme304, _, "Undergraduate", _, _). 

% Prerequisites for ESG420
:- course(esg420, 3, "Undergraduate", 1, 1), 
   not course(phy127, _, "Undergraduate", _, _), 
   not course(phy132, _, "Undergraduate", _, _), 
   not course(phy142, _, "Undergraduate", _, _). 

:- course(esg420, 3, "Undergraduate", 1, 1), 
   not course(ams361, _, "Undergraduate", _, _), 
   not course(mat303, _, "Undergraduate", _, _), 
   not course(mat305, _, "Undergraduate", _, _). 

% Prerequisites for ESG440
:- course(esg440, 3, "Undergraduate", 1, 1), 
   not course(esg312, _, "Undergraduate", _, _). 

:- course(esg440, 3, "Undergraduate", 1, 1), 
   not course(esg316, _, "Undergraduate", _, _). 

:- course(esg440, 3, "Undergraduate", 1, 1), 
   not course(esg332, _, "Undergraduate", _, _). 

% Prerequisites for ESG441
:- course(esg441, 3, "Undergraduate", 1, 1), 
   not course(esg440, _, "Undergraduate", _, _). 

