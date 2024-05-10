% Load courses and their properties
% e.g., course(course_name, course_credits, career, is_offered_spring, is_offered_fall).

% Include the course data from your provided file
% #include "courses.lp".
% #include "courses.current.lp".

% NOTE:
%   - This kind of works.
%   - Try this for 1 semester.
%   - Try limiting certain courses to certain semesters. (e.g. CSE101 only in first semester)

% Course predicates
course(cse101, 3, "Undergraduate", 1, 1).
% course(cse102, 3, "Undergraduate", 0, 0).
course(cse110, 3, "Undergraduate", 1, 1).
course(cse113, 4, "Undergraduate", 0, 1).
course(cse114, 4, "Undergraduate", 1, 0).
course(cse130, 3, "Undergraduate", 1, 0).
course(cse150, 4, "Undergraduate", 1, 1).
course(cse160, 3, "Undergraduate", 1, 1).
course(cse161, 1, "Undergraduate", 1, 1).
course(cse190, 3, "Undergraduate", 1, 1).
course(cse191, 3, "Undergraduate", 0, 1).
course(cse192, 3, "Undergraduate", 0, 1).
course(cse213, 4, "Undergraduate", 1, 1).
course(cse214, 4, "Undergraduate", 1, 1).
course(cse215, 4, "Undergraduate", 1, 1).
course(cse216, 4, "Undergraduate", 1, 1).
course(cse220, 4, "Undergraduate", 0, 1).
course(cse230, 3, "Undergraduate", 1, 1).
course(cse260, 3, "Undergraduate", 1, 0).
course(cse261, 1, "Undergraduate", 1, 1).
course(cse300, 3, "Undergraduate", 1, 0).
course(cse301, 3, "Undergraduate", 1, 1).
course(cse303, 3, "Undergraduate", 1, 1).
course(cse304, 3, "Undergraduate", 1, 1).
course(cse305, 3, "Undergraduate", 1, 0).
course(cse306, 3, "Undergraduate", 0, 1).
course(cse307, 3, "Undergraduate", 1, 0).
course(cse310, 3, "Undergraduate", 0, 1).
course(cse311, 3, "Undergraduate", 0, 1).
course(cse312, 3, "Undergraduate", 0, 1).
course(cse316, 3, "Undergraduate", 1, 1).
course(cse320, 3, "Undergraduate", 1, 1).
course(cse323, 3, "Undergraduate", 0, 1).
course(cse325, 3, "Undergraduate", 0, 1).
course(cse327, 3, "Undergraduate", 1, 0).
course(cse328, 3, "Undergraduate", 1, 0).
course(cse331, 3, "Undergraduate", 0, 1).
course(cse332, 3, "Undergraduate", 1, 1).
course(cse333, 3, "Undergraduate", 0, 1).
course(cse334, 3, "Undergraduate", 1, 1).
course(cse336, 3, "Undergraduate", 0, 1).
course(cse337, 3, "Undergraduate", 0, 1).
course(cse350, 4, "Undergraduate", 1, 0).
% course(cse351, 3, "Undergraduate", 0, 0).
% course(cse352, 3, "Undergraduate", 0, 0).
course(cse353, 3, "Undergraduate", 1, 0).
course(cse354, 3, "Undergraduate", 1, 0).
course(cse355, 3, "Undergraduate", 1, 0).
course(cse356, 3, "Undergraduate", 1, 1).
course(cse357, 3, "Undergraduate", 1, 0).
course(cse360, 3, "Undergraduate", 1, 0).
course(cse361, 3, "Undergraduate", 0, 1).
course(cse362, 3, "Undergraduate", 1, 0).
course(cse363, 3, "Undergraduate", 0, 1).
course(cse364, 3, "Undergraduate", 1, 0).
course(cse366, 3, "Undergraduate", 1, 0).
course(cse370, 3, "Undergraduate", 1, 1).
course(cse371, 3, "Undergraduate", 1, 1).
course(cse373, 3, "Undergraduate", 1, 1).
course(cse376, 3, "Undergraduate", 1, 1).
course(cse377, 3, "Undergraduate", 1, 1).
course(cse378, 3, "Undergraduate", 1, 1).
course(cse380, 3, "Undergraduate", 0, 1).
course(cse381, 3, "Undergraduate", 1, 1).
course(cse385, 4, "Undergraduate", 0, 1).
course(cse390, 3, "Undergraduate", 1, 0).
course(cse391, 3, "Undergraduate", 1, 0).
% course(cse392, 3, "Undergraduate", 0, 0).
course(cse393, 3, "Undergraduate", 1, 0).
course(cse394, 3, "Undergraduate", 1, 1).
course(cse416, 3, "Undergraduate", 0, 1).
course(cse475, 3, "Undergraduate", 1 ,1).
course(cse487, 0..6, "Undergraduate", 1, 1).
course(cse488, 3, "Undergraduate", 1, 1).
course(cse495, 3, "Undergraduate", 1, 0).
course(cse496, 3, "Undergraduate", 0, 1).

% Grad classes
course(cse502, 3, "Graduate", 1, 0).
course(cse504, 3, "Graduate", 1, 0).
course(cse505, 3, "Graduate", 1, 0).
course(cse506, 3, "Graduate", 1, 1).
course(cse507, 3, "Graduate", 0, 1).
course(cse508, 3, "Graduate", 0, 1).
course(cse509, 3, "Graduate", 0, 0).
course(cse510, 3, "Graduate", 1, 1).
course(cse511, 3, "Graduate", 0, 0).
course(cse512, 3, "Graduate", 0, 0).
course(cse514, 3, "Graduate", 0, 1).
% course(cse515, 3, "Graduate", 0, 0).
% course(cse516, 1, "Graduate", 0, 0).
course(cse517, 1, "Graduate", 1, 1).
course(cse518, 3, "Graduate", 1, 1).
course(cse519, 3, "Graduate", 0, 1).
course(cse521, 3, "Graduate", 0, 1).
course(cse522, 3, "Graduate", 1, 0).
course(cse523, 3, "Graduate", 1, 0).
course(cse524, 3, "Graduate", 0, 0).
course(cse525, 3, "Graduate", 1, 1).
course(cse526, 3, "Graduate", 0, 1).
course(cse527, 3, "Graduate", 1, 0).
course(cse528, 3, "Graduate", 1, 1).
course(cse529, 3, "Graduate", 1, 0).
% course(cse530, 3, "Graduate", 0, 0).
course(cse531, 3, "Graduate", 1, 0).
course(cse532, 3, "Graduate", 1, 0).
course(cse533, 3, "Graduate", 1, 0).
course(cse534, 3, "Graduate", 1, 1).
course(cse535, 3, "Graduate", 1, 0).
course(cse536, 3, "Graduate", 0, 1).

% course(cse537, 3, "Graduate", 0, 0).
% course(cse538, 3, "Graduate", 0, 0).
% course(cse540, 3, "Graduate", 0, 0).
% course(cse541, 3, "Graduate", 0, 0).
% course(cse542, 3, "Graduate", 0, 0).
% course(cse544, 3, "Graduate", 0, 0).
% course(cse545, 3, "Graduate", 0, 0).
% course(cse546, 3, "Graduate", 0, 0).
% course(cse547, 3, "Graduate", 0, 0).
% course(cse548, 3, "Graduate", 0, 0).
% course(cse549, 3, "Graduate", 0, 0).
% course(cse550, 3, "Graduate", 0, 0).
% course(cse551, 3, "Graduate", 0, 0).
% course(cse552, 3, "Graduate", 0, 0).
% course(cse555, 3, "Graduate", 0, 0).
% course(cse564, 3, "Graduate", 0, 0).
% course(cse566, 3, "Graduate", 0, 0).
% course(cse570, 3, "Graduate", 0, 0).
% course(cse577, 3, "Graduate", 0, 0).
% course(cse581, 3, "Graduate", 0, 0).
% course(cse582, 3, "Graduate", 0, 0).
% course(cse583, 3, "Graduate", 0, 0).
% course(cse587, 3, "Graduate", 0, 0).
% course(cse590, 3, "Graduate", 0, 0).
% course(cse591, 3, "Graduate", 0, 0).
% course(cse592, 3, "Graduate", 0, 0).
% course(cse593, 1..9, "Graduate", 1, 1).
% course(cse594, 3, "Graduate", 0, 0).
% course(cse595, 3, "Graduate", 0, 0).
% course(cse596, 1, "Graduate", 0, 0).
% course(cse597, 1, "Graduate", 0, 0).
% course(cse599, 1..12, "Graduate", 0, 0).
% course(cse600, 0..1, "Graduate", 1, 1).
% course(cse602, 3, "Graduate", 0, 0).
% course(cse605, 3, "Graduate", 0, 0).
% course(cse608, 3, "Graduate", 0, 0).
% course(cse610, 3, "Graduate", 0, 0).
% course(cse613, 3, "Graduate", 0, 0).
% course(cse614, 3, "Graduate", 0, 0).
% course(cse615, 3, "Graduate", 0, 0).
% course(cse617, 3, "Graduate", 0, 0).
% course(cse620, 3, "Graduate", 0, 0).
% course(cse621, 3, "Graduate", 0, 0).
% course(cse624, 3, "Graduate", 0, 0).
% course(cse625, 3, "Graduate", 0, 0).
% course(cse626, 3, "Graduate", 0, 0).
% course(cse628, 3, "Graduate", 0, 0).
% course(cse633, 3, "Graduate", 0, 0).
% course(cse638, 3, "Graduate", 0, 0).
% course(cse639, 1, "Graduate", 0, 0).
% course(cse641, 1, "Graduate", 0, 0).
% course(cse642, 1, "Graduate", 0, 0).
% course(cse643, 1, "Graduate", 0, 0).
% course(cse644, 1, "Graduate", 0, 0).
% course(cse645, 1, "Graduate", 0, 0).
% course(cse646, 1, "Graduate", 0, 0).
% course(cse648, 1, "Graduate", 0, 0).
% course(cse649, 1, "Graduate", 0, 0).
% course(cse650, 1, "Graduate", 0, 0).
% course(cse651, 1, "Graduate", 0, 0).
% course(cse652, 1, "Graduate", 0, 0).
% course(cse653, 1, "Graduate", 0, 0).
% course(cse654, 1, "Graduate", 0, 0).
% course(cse655, 1, "Graduate", 0, 0).
% course(cse656, 1, "Graduate", 0, 0).
% course(cse657, 1, "Graduate", 0, 0).
% course(cse658, 1, "Graduate", 0, 0).
% course(cse659, 1, "Graduate", 0, 0).
% course(cse660, 1, "Graduate", 0, 0).
% course(cse661, 1, "Graduate", 0, 0).
% course(cse662, 1, "Graduate", 0, 0).
% course(cse663, 1, "Graduate", 0, 0).
% course(cse664, 1, "Graduate", 0, 0).
% course(cse665, 2, "Graduate", 0, 0).
% course(cse669, 2, "Graduate", 0, 0).
% course(cse670, 2, "Graduate", 0, 0).
% course(cse671, 2, "Graduate", 0, 0).
% course(cse672, 2, "Graduate", 0, 0).
% course(cse674, 2, "Graduate", 0, 0).
% course(cse677, 2, "Graduate", 0, 0).
% course(cse681, 2, "Graduate", 0, 0).
% course(cse684, 2, "Graduate", 0, 0).
% course(cse686, 2, "Graduate", 0, 0).
% course(cse687, 2, "Graduate", 0, 0).
% course(cse690, 3, "Graduate", 0, 0).
% course(cse691, 3, "Graduate", 0, 0).
% course(cse692, 3, "Graduate", 0, 0).
% course(cse693, 3, "Graduate", 0, 0).
% course(cse694, 1, "Graduate", 0, 0).
% course(cse695, 1, "Graduate", 0, 0).
% course(cse696, 1..3, "Graduate", 0, 0).
% course(cse697, 1, "Graduate", 0, 0).
% course(cse698, 0..3, "Graduate", 1, 1).
% course(cse699, 0..9, "Graduate", 0, 0).
% course(cse700, 0..9, "Graduate", 0, 0).
% course(cse701, 0..9, "Graduate", 0, 0).
% course(cse800, 0, "Graduate", 0, 0).

% Honors Courses
honors(cse150).
honors(cse160).
honors(cse161).
honors(cse260).
honors(cse261).
honors(cse350).
honors(cse385).
honors(cse495).
honors(cse496).

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

% Course Rules 

% % Antirequisites for CSE101
% :- course(cse101, 3, "Undergraduate", 1, 1), 
%    course(cse114, _, "Undergraduate", _, _). 

% :- course(cse101, 3, "Undergraduate", 1, 1), 
%    course(cse160, _, "Undergraduate", _, _). 

% Prerequisites for CSE102
:- course(cse102, 3, "Undergraduate", 0, 0), 
   not course(cse101, _, "Undergraduate", _, _). 

% Prerequisites for CSE113
:- course(cse113, 4, "Undergraduate", 0, 1), 
   not course(ams151, _, "Undergraduate", _, _), 
   not course(mat125, _, "Undergraduate", _, _), 
   not course(mat131, _, "Undergraduate", _, _). 

% Prerequisites for CSE114
:- course(cse114, 4, "Undergraduate", 1, 0), 
   not course(cse101, _, "Undergraduate", _, _), 
   not course(ise108, _, "Undergraduate", _, _). 

% Corequisites for CSE160
:- course(cse160, 3, "Undergraduate", 1, 1), 
   not course(cse161, _, "Undergraduate", 1, 1). 

% Corequisites for CSE161
:- course(cse161, 1, "Undergraduate", 1, 1), 
   not course(cse160, _, "Undergraduate", 1, 1). 

% Prerequisites for CSE213
:- course(cse213, 4, "Undergraduate", 1, 1), 
   not course(cse113, _, "Undergraduate", _, _). 

% Prerequisites for CSE214
:- course(cse214, 4, "Undergraduate", 1, 1), 
   not course(cse114, _, "Undergraduate", _, _). 

% Prerequisites for CSE215
:- course(cse215, 4, "Undergraduate", 1, 1), 
   not course(ams151, _, "Undergraduate", _, _), 
   not course(mat125, _, "Undergraduate", _, _), 
   not course(mat131, _, "Undergraduate", _, _). 

% Prerequisites for CSE216
:- course(cse216, 4, "Undergraduate", 1, 1), 
   not course(cse214, _, "Undergraduate", _, _). 

% Prerequisites for CSE220
:- course(cse220, 4, "Undergraduate", 0, 1), 
   not course(cse214, _, "Undergraduate", _, _). 

% % Corequisites for CSE220
% :- course(cse220, 4, "Undergraduate", 0, 1), 
%    not course(cse260, _, "Undergraduate", 0, 1). 
% :- course(cse220, 4, "Undergraduate", 0, 1), 
%    not course(cse260, _, "Undergraduate", _, _). 

% Prerequisites for CSE230
:- course(cse230, 3, "Undergraduate", 1, 1), 
   not course(cse130, _, "Undergraduate", _, _), 
   not course(cse220, _, "Undergraduate", _, _), 
   not course(ese124, _, "Undergraduate", _, _), 
   not course(esg111, _, "Undergraduate", _, _), 
   not course(bme120, _, "Undergraduate", _, _), 
   not course(mec102, _, "Undergraduate", _, _). 

% Prerequisites for CSE260
:- course(cse260, 3, "Undergraduate", 1, 0), 
   not course(cse160, _, "Undergraduate", _, _). 

% % Corequisites for CSE260
% :- course(cse260, 3, "Undergraduate", 1, 0), 
%    not course(cse261, _, "Undergraduate", 1, 0). 
:- course(cse260, 3, "Undergraduate", 1, 0), 
   not course(cse261, _, "Undergraduate", _, _). 

% % Corequisites for CSE261
% :- course(cse261, 1, "Undergraduate", 1, 1), 
%    not course(cse260, _, "Undergraduate", 1, 1). 
:- course(cse261, 1, "Undergraduate", 1, 1), 
   not course(cse260, _, "Undergraduate", _, _). 

% Prerequisites for CSE300
:- course(cse300, 3, "Undergraduate", 1, 0), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for CSE303
:- course(cse303, 3, "Undergraduate", 1, 1), 
   not course(cse160, _, "Undergraduate", _, _), 
   not course(cse214, _, "Undergraduate", _, _). 

:- course(cse303, 3, "Undergraduate", 1, 1), 
   not course(cse150, _, "Undergraduate", _, _), 
   not course(cse215, _, "Undergraduate", _, _). 

% Prerequisites for CSE304
:- course(cse304, 3, "Undergraduate", 1, 1), 
   not course(cse216, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

:- course(cse304, 3, "Undergraduate", 1, 1), 
   not course(cse220, _, "Undergraduate", _, _), 
   not course(cse303, _, "Undergraduate", _, _), 
   not course(cse350, _, "Undergraduate", _, _). 

% Prerequisites for CSE305
:- course(cse305, 3, "Undergraduate", 1, 0), 
   not course(cse216, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

% Prerequisites for CSE306
:- course(cse306, 3, "Undergraduate", 0, 1), 
   not course(cse216, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

:- course(cse306, 3, "Undergraduate", 0, 1), 
   not course(cse320, _, "Undergraduate", _, _), 
   not course(ese380, _, "Undergraduate", _, _). 

% Prerequisites for CSE307
:- course(cse307, 3, "Undergraduate", 1, 0), 
   not course(cse216, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

:- course(cse307, 3, "Undergraduate", 1, 0), 
   not course(cse220, _, "Undergraduate", _, _). 

% Prerequisites for CSE310
:- course(cse310, 3, "Undergraduate", 0, 1), 
   not course(cse214, _, "Undergraduate", _, _). 

:- course(cse310, 3, "Undergraduate", 0, 1), 
   not course(cse220, _, "Undergraduate", _, _), 
   not course(ise218, _, "Undergraduate", _, _). 

% % Corequisites for CSE310
% :- course(cse310, 3, "Undergraduate", 0, 1), 
%    not course(ams310, _, "Undergraduate", 0, 1). 
:- course(cse310, 3, "Undergraduate", 0, 1), 
   not course(ams310, _, "Undergraduate", _, _). 

% Prerequisites for CSE311
:- course(cse311, 3, "Undergraduate", 0, 1), 
   not course(cse214, _, "Undergraduate", _, _), 
   not course(cse230, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _), 
   not course(ise208, _, "Undergraduate", _, _). 

% Prerequisites for CSE316
:- course(cse316, 3, "Undergraduate", 1, 1), 
   not course(cse216, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

% Prerequisites for CSE320
:- course(cse320, 3, "Undergraduate", 1, 1), 
   not course(cse220, _, "Undergraduate", _, _). 

% Prerequisites for CSE323
:- course(cse323, 3, "Undergraduate", 0, 1), 
   not course(cse214, _, "Undergraduate", _, _), 
   not course(cse230, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _), 
   not course(ise208, _, "Undergraduate", _, _). 

% Prerequisites for CSE325
:- course(cse325, 3, "Undergraduate", 0, 1), 
   not course(cse110, _, "Undergraduate", _, _), 
   not course(cse101, _, "Undergraduate", _, _), 
   not course(cse114, _, "Undergraduate", _, _). 

% Prerequisites for CSE327
:- course(cse327, 3, "Undergraduate", 1, 0), 
   not course(cse214, _, "Undergraduate", _, _), 
   not course(cse230, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

:- course(cse327, 3, "Undergraduate", 1, 0), 
   not course(ams210, _, "Undergraduate", _, _), 
   not course(mat211, _, "Undergraduate", _, _). 

% Prerequisites for CSE328
:- course(cse328, 3, "Undergraduate", 1, 0), 
   not course(cse216, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

:- course(cse328, 3, "Undergraduate", 1, 0), 
   not course(cse220, _, "Undergraduate", _, _). 

% Prerequisites for CSE331
:- course(cse331, 3, "Undergraduate", 0, 1), 
   not course(cse220, _, "Undergraduate", _, _). 

% % Corequisites for CSE331
% :- course(cse331, 3, "Undergraduate", 0, 1), 
%    not course(cse320, _, "Undergraduate", 0, 1). 
:- course(cse331, 3, "Undergraduate", 0, 1), 
   not course(cse320, _, "Undergraduate", _, _). 

% Prerequisites for CSE332
:- course(cse332, 3, "Undergraduate", 1, 1), 
   not course(cse214, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

:- course(cse332, 3, "Undergraduate", 1, 1), 
   not course(mat211, _, "Undergraduate", _, _), 
   not course(ams210, _, "Undergraduate", _, _). 

:- course(cse332, 3, "Undergraduate", 1, 1), 
   not course(ams110, _, "Undergraduate", _, _), 
   not course(ams310, _, "Undergraduate", _, _). 

% Prerequisites for CSE333
:- course(cse333, 3, "Undergraduate", 0, 1), 
   not course(cse214, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

% Prerequisites for CSE336
:- course(cse336, 3, "Undergraduate", 0, 1), 
   not course(cse216, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

% Prerequisites for CSE337
:- course(cse337, 3, "Undergraduate", 0, 1), 
   not course(cse214, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

% Prerequisites for CSE350
:- course(cse350, 4, "Undergraduate", 1, 0), 
   not course(cse150, _, "Undergraduate", _, _), 
   not course(cse215, _, "Undergraduate", _, _). 

:- course(cse350, 4, "Undergraduate", 1, 0), 
   not course(ams210, _, "Undergraduate", _, _), 
   not course(mat211, _, "Undergraduate", _, _). 

% % Prerequisites for CSE351
% :- course(cse351, 3, "Undergraduate", 0, 0), 
%    not course(cse214, _, "Undergraduate", _, _), 
%    not course(cse260, _, "Undergraduate", _, _). 

% :- course(cse351, 3, "Undergraduate", 0, 0), 
%    not course(ams310, _, "Undergraduate", _, _). 

% % Prerequisites for CSE352
% :- course(cse352, 3, "Undergraduate", 0, 0), 
%    not course(cse216, _, "Undergraduate", _, _), 
%    not course(cse260, _, "Undergraduate", _, _). 

% Prerequisites for CSE353
:- course(cse353, 3, "Undergraduate", 1, 0), 
   not course(cse216, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

:- course(cse353, 3, "Undergraduate", 1, 0), 
   not course(ams310, _, "Undergraduate", _, _), 
   not course(ams311, _, "Undergraduate", _, _), 
   not course(ams412, _, "Undergraduate", _, _). 

% Prerequisites for CSE354
:- course(cse354, 3, "Undergraduate", 1, 0), 
   not course(cse216, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

% Prerequisites for CSE355
:- course(cse355, 3, "Undergraduate", 1, 0), 
   not course(ams301, _, "Undergraduate", _, _). 

% Prerequisites for CSE356
:- course(cse356, 3, "Undergraduate", 1, 1), 
   not course(cse316, _, "Undergraduate", _, _). 

:- course(cse356, 3, "Undergraduate", 1, 1), 
   not course(cse320, _, "Undergraduate", _, _). 

% Prerequisites for CSE357
:- course(cse357, 3, "Undergraduate", 1, 0), 
   not course(cse216, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

:- course(cse357, 3, "Undergraduate", 1, 0), 
   not course(ams310, _, "Undergraduate", _, _). 

% Prerequisites for CSE360
:- course(cse360, 3, "Undergraduate", 1, 0), 
   not course(cse220, _, "Undergraduate", _, _). 

% % Corequisites for CSE360
% :- course(cse360, 3, "Undergraduate", 1, 0), 
%    not course(cse320, _, "Undergraduate", 1, 0). 
:- course(cse360, 3, "Undergraduate", 1, 0), 
   not course(cse320, _, "Undergraduate", _, _). 

% Prerequisites for CSE361
:- course(cse361, 3, "Undergraduate", 0, 1), 
   not course(cse220, _, "Undergraduate", _, _). 

% % Corequisites for CSE361
% :- course(cse361, 3, "Undergraduate", 0, 1), 
%    not course(cse320, _, "Undergraduate", 0, 1). 
:- course(cse361, 3, "Undergraduate", 0, 1), 
   not course(cse320, _, "Undergraduate", _, _). 

% Prerequisites for CSE362
:- course(cse362, 3, "Undergraduate", 1, 0), 
   not course(cse220, _, "Undergraduate", _, _). 

% % Corequisites for CSE362
% :- course(cse362, 3, "Undergraduate", 1, 0), 
%    not course(cse320, _, "Undergraduate", 1, 0). 
:- course(cse362, 3, "Undergraduate", 1, 0), 
   not course(cse320, _, "Undergraduate", _, _). 

% Prerequisites for CSE363
:- course(cse363, 3, "Undergraduate", 0, 1), 
   not course(cse220, _, "Undergraduate", _, _). 

% % Corequisites for CSE363
% :- course(cse363, 3, "Undergraduate", 0, 1), 
%    not course(cse320, _, "Undergraduate", 0, 1). 
:- course(cse363, 3, "Undergraduate", 0, 1), 
   not course(cse320, _, "Undergraduate", _, _). 

% Prerequisites for CSE364
:- course(cse364, 3, "Undergraduate", 1, 0), 
   not course(ise334, _, "Undergraduate", _, _). 

:- course(cse364, 3, "Undergraduate", 1, 0), 
   not course(cse334, _, "Undergraduate", _, _). 

% Prerequisites for CSE366
:- course(cse366, 3, "Undergraduate", 1, 0), 
   not course(cse328, _, "Undergraduate", _, _), 
   not course(ise332, _, "Undergraduate", _, _). 

% Prerequisites for CSE370
:- course(cse370, 3, "Undergraduate", 1, 1), 
   not course(cse310, _, "Undergraduate", _, _). 

% Prerequisites for CSE371
:- course(cse371, 3, "Undergraduate", 1, 1), 
   not course(cse150, _, "Undergraduate", _, _), 
   not course(cse215, _, "Undergraduate", _, _), 
   not course(mat200, _, "Undergraduate", _, _), 
   not course(mat250, _, "Undergraduate", _, _). 

% Prerequisites for CSE373
:- course(cse373, 3, "Undergraduate", 1, 1), 
   not course(cse150, _, "Undergraduate", _, _), 
   not course(cse215, _, "Undergraduate", _, _), 
   not course(mat200, _, "Undergraduate", _, _), 
   not course(mat250, _, "Undergraduate", _, _). 

:- course(cse373, 3, "Undergraduate", 1, 1), 
   not course(mat211, _, "Undergraduate", _, _), 
   not course(ams210, _, "Undergraduate", _, _). 

:- course(cse373, 3, "Undergraduate", 1, 1), 
   not course(cse214, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

% Prerequisites for CSE376
:- course(cse376, 3, "Undergraduate", 1, 1), 
   not course(cse216, _, "Undergraduate", _, _). 

:- course(cse376, 3, "Undergraduate", 1, 1), 
   not course(cse320, _, "Undergraduate", _, _). 

% Prerequisites for CSE377
:- course(cse377, 3, "Undergraduate", 1, 1), 
   not course(ams161, _, "Undergraduate", _, _), 
   not course(mat127, _, "Undergraduate", _, _). 

:- course(cse377, 3, "Undergraduate", 1, 1), 
   not course(ams210, _, "Undergraduate", _, _), 
   not course(mat211, _, "Undergraduate", _, _). 

% Prerequisites for CSE378
:- course(cse378, 3, "Undergraduate", 1, 1), 
   not course(ams161, _, "Undergraduate", _, _), 
   not course(mat127, _, "Undergraduate", _, _). 

:- course(cse378, 3, "Undergraduate", 1, 1), 
   not course(ams210, _, "Undergraduate", _, _), 
   not course(mat211, _, "Undergraduate", _, _), 
   not course(mec262, _, "Undergraduate", _, _). 

% Prerequisites for CSE380
:- course(cse380, 3, "Undergraduate", 0, 1), 
   not course(cse216, _, "Undergraduate", _, _), 
   not course(cse220, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

% Prerequisites for CSE381
:- course(cse381, 3, "Undergraduate", 1, 1), 
   not course(cse216, _, "Undergraduate", _, _), 
   not course(cse220, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

% Prerequisites for CSE385
:- course(cse385, 4, "Undergraduate", 0, 1), 
   not course(cse150, _, "Undergraduate", _, _), 
   not course(cse215, _, "Undergraduate", _, _), 
   not course(mat200, _, "Undergraduate", _, _), 
   not course(mat250, _, "Undergraduate", _, _). 

:- course(cse385, 4, "Undergraduate", 0, 1), 
   not course(ams210, _, "Undergraduate", _, _), 
   not course(mat211, _, "Undergraduate", _, _). 

:- course(cse385, 4, "Undergraduate", 0, 1), 
   not course(cse214, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

% Prerequisites for CSE390
:- course(cse390, 3, "Undergraduate", 1, 0), 
   not course(cse214, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

% Prerequisites for CSE391
:- course(cse391, 3, "Undergraduate", 1, 0), 
   not course(cse214, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

% % Prerequisites for CSE392
% :- course(cse392, 3, "Undergraduate", 0, 0), 
%    not course(cse214, _, "Undergraduate", _, _), 
%    not course(cse260, _, "Undergraduate", _, _). 

% Prerequisites for CSE393
:- course(cse393, 3, "Undergraduate", 1, 0), 
   not course(cse214, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

% Prerequisites for CSE394
:- course(cse394, 3, "Undergraduate", 1, 1), 
   not course(cse214, _, "Undergraduate", _, _), 
   not course(cse260, _, "Undergraduate", _, _). 

% Prerequisites for CSE416
:- course(cse416, 3, "Undergraduate", 0, 1), 
   not course(cse316, _, "Undergraduate", _, _). 

% Prerequisites for CSE496
:- course(cse496, 3, "Undergraduate", 0, 1), 
   not course(cse495, _, "Undergraduate", _, _). 



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

% Graduation requirements

% Define constants
#const max_semesters = 12.
#const min_credits_per_semester = 12.
#const max_credits_per_semester = 18.

% Define possible semesters
semester(1..max_semesters).

% Schedule courses across semesters
1 { schedule(Course, Sem) : semester(Sem) } 1 :- course(Course, Credits, Career, Spring, Fall).

% Prevent scheduling of courses already taken
:- course_taken(Course), schedule(Course, _).

% course_taken(cse101).
% course_taken(ams110).
% course_taken(ams151).
% course_taken(mat131).
% course_taken(mat123).
% course_taken(mat125).
% course_taken(bio201).
% course_taken(bio204).


% Semester limits: at least 12 credits and at most 18 credits per semester
:- semester(Sem), SemCredits = #count { Credits, Course : schedule(Course, Sem), course(Course, Credits, "Undergraduate", _, _) }, SemCredits < min_credits_per_semester.
:- semester(Sem), SemCredits = #count { Credits, Course : schedule(Course, Sem), course(Course, Credits, "Undergraduate", _, _) }, SemCredits > max_credits_per_semester.

% Ensure all scheduled courses comply with seasonal offerings
:- schedule(Course, Sem), course(Course, _, "Undergraduate", Spring, Fall), 
   Sem \ 2 = 1, Fall = 0.
:- schedule(Course, Sem), course(Course, _, "Undergraduate", Spring, Fall), 
   Sem \ 2 = 0, Spring = 0.

% Count total credits and major credits
total_credits(Total) :- Total = #sum { Credits, Course : schedule(Course, _), course(Course, Credits, "Undergraduate", _, _) }.
major_credits(Major) :- Major = #sum { Credits, Course : schedule(Course, _), course(Course, Credits, "Undergraduate", _, _) }.

% Graduation requirements
:- total_credits(Total), Total < 120.
:- major_credits(Major), Major < 80.

% Objective to minimize the number of semesters
#minimize { 1, Sem : schedule(_, Sem) }.

#show schedule/2.