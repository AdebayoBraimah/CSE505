% Course atoms
course(bme100, 3, "Undergraduate", 1, 1).
course(bme120, 3, "Undergraduate", 1, 1).
course(bme200, 3, "Undergraduate", 1, 1).
course(bme203, 3, "Undergraduate", 1, 1).
course(bme205, 3, "Undergraduate", 1, 1).
course(bme210, 3, "Undergraduate", 1, 1).
course(bme212, 3, "Undergraduate", 1, 1).
course(bme260, 4, "Undergraduate", 1, 1).
course(bme271, 3, "Undergraduate", 1, 1).
course(bme300, 0, "Undergraduate", 1, 1).
course(bme301, 3, "Undergraduate", 1, 1).
course(bme303, 3, "Undergraduate", 1, 1).
course(bme304, 3, "Undergraduate", 1, 1).
course(bme305, 3, "Undergraduate", 1, 1).
course(bme310, 3, "Undergraduate", 1, 1).
course(bme311, 3, "Undergraduate", 1, 1).
course(bme312, 3, "Undergraduate", 1, 1).
course(bme313, 3, "Undergraduate", 1, 1).
course(bme353, 3, "Undergraduate", 1, 1).
course(bme354, 3, "Undergraduate", 1, 1).
course(bme361, 3, "Undergraduate", 1, 1).
course(bme371, 3, "Undergraduate", 1, 1).
course(bme381, 3, "Undergraduate", 1, 1).
course(bme402, 3, "Undergraduate", 1, 1).
course(bme404, 3, "Undergraduate", 1, 1).
course(bme420, 3, "Undergraduate", 1, 1).
course(bme430, 3, "Undergraduate", 1, 1).
course(bme440, 3, "Undergraduate", 1, 1).
course(bme441, 3, "Undergraduate", 1, 1).
course(bme444, 0, "Undergraduate", 1, 1).
course(bme461, 3, "Undergraduate", 1, 1).
course(bme475, 3, "Undergraduate", 1, 1).
course(bme476, 3, "Undergraduate", 1, 1).
course(bme481, 3, "Undergraduate", 1, 1).
course(bme488, 3..6, "Undergraduate", 1, 1).
course(bme494, 1, "Undergraduate", 1, 1).
course(bme495, 3, "Undergraduate", 1, 1).
course(bme499, 0..3, "Undergraduate", 1, 1).
course(bme501, 3, "Graduate", 1, 1).
course(bme502, 3, "Graduate", 1, 1).
course(bme503, 3, "Graduate", 1, 1).
course(bme504, 3, "Graduate", 1, 1).
course(bme505, 1, "Graduate", 1, 1).
course(bme508, 3, "Graduate", 1, 1).
course(bme509, 3, "Graduate", 1, 1).
course(bme510, 3, "Graduate", 1, 1).
course(bme511, 3, "Graduate", 1, 1).
course(bme512, 3, "Graduate", 1, 1).
course(bme513, 3, "Graduate", 1, 1).
course(bme515, 3, "Graduate", 1, 1).
course(bme517, 3, "Graduate", 1, 1).
course(bme518, 3, "Graduate", 1, 1).
course(bme519, 3, "Graduate", 1, 1).
course(bme520, 1..3, "Graduate", 1, 1).
course(bme521, 1..3, "Graduate", 1, 1).
course(bme525, 3, "Graduate", 1, 1).
course(bme526, 3, "Graduate", 1, 1).
course(bme530, 3, "Graduate", 1, 1).
course(bme531, 3, "Graduate", 1, 1).
course(bme532, 3, "Graduate", 1, 1).
course(bme533, 3..4, "Graduate", 1, 1).
course(bme534, 3, "Graduate", 1, 1).
course(bme540, 3, "Graduate", 1, 1).
course(bme546, 1, "Graduate", 1, 1).
course(bme547, 1, "Graduate", 1, 1).
course(bme548, 1, "Graduate", 1, 1).
course(bme549, 1, "Graduate", 1, 1).
course(bme550, 3, "Graduate", 1, 1).
course(bme558, 3, "Graduate", 1, 1).
course(bme571, 3, "Graduate", 1, 1).
course(bme572, 3, "Graduate", 1, 1).
course(bme573, 3, "Graduate", 1, 1).
course(bme574, 3, "Graduate", 1, 1).
course(bme581, 3, "Graduate", 1, 1).
course(bme590, 0..1, "Graduate", 1, 1).
course(bme595, 1..6, "Graduate", 1, 1).
course(bme599, 1..9, "Graduate", 1, 1).
course(bme601, 3, "Graduate", 1, 1).
course(bme602, 3, "Graduate", 1, 1).
course(bme603, 3, "Graduate", 1, 1).
course(bme604, 3, "Graduate", 1, 1).
course(bme605, 3, "Graduate", 1, 1).
course(bme608, 3, "Graduate", 1, 1).
course(bme610, 3, "Graduate", 1, 1).
course(bme611, 3, "Graduate", 1, 1).
course(bme612, 3, "Graduate", 1, 1).
course(bme615, 4, "Graduate", 1, 1).
course(bme616, 4, "Graduate", 1, 1).
course(bme617, 4, "Graduate", 1, 1).
course(bme618, 4, "Graduate", 1, 1).
course(bme620, 4, "Graduate", 1, 1).
course(bme670, 0..3, "Graduate", 1, 1).
course(bme690, 1..9, "Graduate", 1, 1).
course(bme698, 1, "Graduate", 1, 1).
course(bme699, 1..9, "Graduate", 1, 1).
course(bme700, 1..9, "Graduate", 1, 1).
course(bme701, 1..9, "Graduate", 1, 1).
course(bme800, 0, "Graduate", 1, 1).

% Honors Courses
honors(bme494).
honors(bme495).

% Course Rules 

% Prerequisites for BME210
:- course(bme210, 3, "Undergraduate", 1, 1), 
   not course(bme100, _, "Undergraduate", _, _). 

% Prerequisites for BME212
:- course(bme212, 3, "Undergraduate", 1, 1), 
   not course(bme100, _, "Undergraduate", _, _). 

% Corequisites for BME212
:- course(bme212, 3, "Undergraduate", 1, 1), 
   not course(bio202, _, "Undergraduate", 1, 1). 

% Prerequisites for BME260
:- course(bme260, 4, "Undergraduate", 1, 1), 
   not course(bme100, _, "Undergraduate", _, _). 

:- course(bme260, 4, "Undergraduate", 1, 1), 
   not course(ams161, _, "Undergraduate", _, _). 

:- course(bme260, 4, "Undergraduate", 1, 1), 
   not course(phy125, _, "Undergraduate", _, _). 

% Prerequisites for BME271
:- course(bme271, 3, "Undergraduate", 1, 1), 
   not course(ams161, _, "Undergraduate", _, _), 
   not course(mat127, _, "Undergraduate", _, _). 

:- course(bme271, 3, "Undergraduate", 1, 1), 
   not course(phy127, _, "Undergraduate", _, _), 
   not course(phy132, _, "Undergraduate", _, _), 
   not course(phy142, _, "Undergraduate", _, _). 

% Prerequisites for BME300
:- course(bme300, 0, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for BME301
:- course(bme301, 3, "Undergraduate", 1, 1), 
   not course(bme120, _, "Undergraduate", _, _). 

:- course(bme301, 3, "Undergraduate", 1, 1), 
   not course(bme271, _, "Undergraduate", _, _), 
   not course(ese271, _, "Undergraduate", _, _). 

:- course(bme301, 3, "Undergraduate", 1, 1), 
   not course(bio202, _, "Undergraduate", _, _). 

% Corequisites for BME301
:- course(bme301, 3, "Undergraduate", 1, 1), 
   not course(bme212, _, "Undergraduate", 1, 1). 

% Prerequisites for BME303
:- course(bme303, 3, "Undergraduate", 1, 1), 
   not course(bme260, _, "Undergraduate", _, _), 
   not course(mec260, _, "Undergraduate", _, _). 

% Corequisites for BME303
:- course(bme303, 3, "Undergraduate", 1, 1), 
   not course(bio202, _, "Undergraduate", 1, 1). 

% Prerequisites for BME304
:- course(bme304, 3, "Undergraduate", 1, 1), 
   not course(bme100, _, "Undergraduate", _, _). 

:- course(bme304, 3, "Undergraduate", 1, 1), 
   not course(bio202, _, "Undergraduate", _, _). 

% Prerequisites for BME305
:- course(bme305, 3, "Undergraduate", 1, 1), 
   not course(ams261, _, "Undergraduate", _, _), 
   not course(mat203, _, "Undergraduate", _, _), 
   not course(mat205, _, "Undergraduate", _, _). 

:- course(bme305, 3, "Undergraduate", 1, 1), 
   not course(ams361, _, "Undergraduate", _, _), 
   not course(mat303, _, "Undergraduate", _, _), 
   not course(mat305, _, "Undergraduate", _, _). 

:- course(bme305, 3, "Undergraduate", 1, 1), 
   not course(bme260, _, "Undergraduate", _, _), 
   not course(mec260, _, "Undergraduate", _, _). 

:- course(bme305, 3, "Undergraduate", 1, 1), 
   not course(mec262, _, "Undergraduate", _, _). 

% Corequisites for BME305
:- course(bme305, 3, "Undergraduate", 1, 1), 
   not course(bio202, _, "Undergraduate", 1, 1). 

:- course(bme305, 3, "Undergraduate", 1, 1), 
   not course(bme212, _, "Undergraduate", 1, 1). 

% Prerequisites for BME310
:- course(bme310, 3, "Undergraduate", 1, 1), 
   not course(bme271, _, "Undergraduate", _, _). 

% Prerequisites for BME311
:- course(bme311, 3, "Undergraduate", 1, 1), 
   not course(bme212, _, "Undergraduate", _, _). 

% Prerequisites for BME313
:- course(bme313, 3, "Undergraduate", 1, 1), 
   not course(bme271, _, "Undergraduate", _, _), 
   not course(ese271, _, "Undergraduate", _, _). 

% Prerequisites for BME353
:- course(bme353, 3, "Undergraduate", 1, 1), 
   not course(bme100, _, "Undergraduate", _, _). 

:- course(bme353, 3, "Undergraduate", 1, 1), 
   not course(bme212, _, "Undergraduate", _, _). 

% Prerequisites for BME354
:- course(bme354, 3, "Undergraduate", 1, 1), 
   not course(bme353, _, "Undergraduate", _, _), 
   not course(esm453, _, "Undergraduate", _, _). 

% Prerequisites for BME361
:- course(bme361, 3, "Undergraduate", 1, 1), 
   not course(bme120, _, "Undergraduate", _, _). 

:- course(bme361, 3, "Undergraduate", 1, 1), 
   not course(mat125, _, "Undergraduate", _, _), 
   not course(ams151, _, "Undergraduate", _, _), 
   not course(mat131, _, "Undergraduate", _, _). 

% Prerequisites for BME371
:- course(bme371, 3, "Undergraduate", 1, 1), 
   not course(bme305, _, "Undergraduate", _, _). 

% Prerequisites for BME381
:- course(bme381, 3, "Undergraduate", 1, 1), 
   not course(che132, _, "Undergraduate", _, _). 

:- course(bme381, 3, "Undergraduate", 1, 1), 
   not course(bme100, _, "Undergraduate", _, _). 

% Corequisites for BME381
:- course(bme381, 3, "Undergraduate", 1, 1), 
   not course(bio202, _, "Undergraduate", 1, 1). 

% Prerequisites for BME402
:- course(bme402, 3, "Undergraduate", 1, 1), 
   not course(bme304, _, "Undergraduate", _, _). 

% Prerequisites for BME404
:- course(bme404, 3, "Undergraduate", 1, 1), 
   not course(bio202, _, "Undergraduate", _, _). 

:- course(bme404, 3, "Undergraduate", 1, 1), 
   not course(che132, _, "Undergraduate", _, _), 
   not course(che321, _, "Undergraduate", _, _). 

% Prerequisites for BME420
:- course(bme420, 3, "Undergraduate", 1, 1), 
   not course(bme303, _, "Undergraduate", _, _). 

% Prerequisites for BME430
:- course(bme430, 3, "Undergraduate", 1, 1), 
   not course(bio202, _, "Undergraduate", _, _). 

:- course(bme430, 3, "Undergraduate", 1, 1), 
   not course(ams261, _, "Undergraduate", _, _), 
   not course(mat203, _, "Undergraduate", _, _), 
   not course(mat205, _, "Undergraduate", _, _). 

% Prerequisites for BME440
:- course(bme440, 3, "Undergraduate", 1, 1), 
   not course(bme301, _, "Undergraduate", _, _). 

% Prerequisites for BME441
:- course(bme441, 3, "Undergraduate", 1, 1), 
   not course(bme440, _, "Undergraduate", _, _). 

% Prerequisites for BME444
:- course(bme444, 0, "Undergraduate", 1, 1), 
   not course(wrt102, _, "Undergraduate", _, _). 

% Prerequisites for BME461
:- course(bme461, 3, "Undergraduate", 1, 1), 
   not course(bme212, _, "Undergraduate", _, _). 

% Prerequisites for BME481
:- course(bme481, 3, "Undergraduate", 1, 1), 
   not course(bio202, _, "Undergraduate", _, _). 

:- course(bme481, 3, "Undergraduate", 1, 1), 
   not course(bme271, _, "Undergraduate", _, _), 
   not course(ese271, _, "Undergraduate", _, _). 

% Prerequisites for BME488
:- course(bme488, 3..6, "Undergraduate", 1, 1), 
   not course(bme212, _, "Undergraduate", _, _). 

% Prerequisites for BME495
:- course(bme495, 3, "Undergraduate", 1, 1), 
   not course(bme494, _, "Undergraduate", _, _). 

