#updated 02/16/17
from datetime import datetime


# NIRS date/time is 2 mins and 10 seconds slower than Philips. Have to correct for it.
# Pulse ox date/time is 1 mins and 32 seconds faster than Philips. Have to correct for it.
ROP003 = {
    'EyeDrop1' : datetime(2015, 5, 20, 8, 58),
    'EyeDrop2' : datetime(2015, 5, 20, 9, 3),
    'EyeDrop3' : datetime(2015, 5, 20, 9, 8),
    'ExamStart' : datetime(2015, 5, 20, 11, 0),
    'ExamEnd' : datetime(2015, 5, 20, 11, 2)
}

ROP005 = {
    'EyeDrop1' : datetime(2015, 6, 3, 6, 30),
    'EyeDrop2' : datetime(2015, 6, 3, 6, 35),
    'EyeDrop3' : datetime(2015, 6, 3, 6, 42),
    'ExamStart' : datetime(2015, 6, 3, 8, 42),
    'ExamEnd' : datetime(2015, 6, 3, 8, 46)
}

ROP006 = {
    'EyeDrop1' : datetime(2015, 6, 17, 7, 10),
    'EyeDrop2' : datetime(2015, 6, 17, 7, 15),
    'EyeDrop3' : datetime(2015, 6, 17, 7, 20),
    'ExamStart' : datetime(2015, 6, 17, 8, 36),
    'ExamEnd' : datetime(2015, 6, 17, 8, 39)
}

ROP007 = {
    'EyeDrop1' : datetime(2015, 7, 1, 8, 30),
    'EyeDrop2' : datetime(2015, 7, 1, 8, 37),
    'EyeDrop3' : datetime(2015, 7, 1, 8, 42),
    'ExamStart' : datetime(2015, 7, 1, 9, 49),
    'ExamEnd' : datetime(2015, 7, 1, 9, 53)
}

ROP008 = {
    'EyeDrop1' : datetime(2015, 8, 19, 6, 30),
    'EyeDrop2' : datetime(2015, 8, 19, 6, 36),
    'EyeDrop3' : datetime(2015, 8, 19, 6, 41),
    'ExamStart' : datetime(2015, 8, 19, 8, 1),
    'ExamEnd' : datetime(2015, 8, 19, 8, 5)
}

ROP009 = {
    'EyeDrop1' : datetime(2015, 8, 26, 9, 4),
    'EyeDrop2' : datetime(2015, 8, 26, 9, 9),
    'EyeDrop3' : datetime(2015, 8, 26, 9, 14),
    'ExamStart' : datetime(2015, 8, 26, 9, 56),
    'ExamEnd' : datetime(2015, 8, 26, 9, 59)
}

ROP010 = {
    'EyeDrop1' : datetime(2015, 9, 14, 10, 36),
    'EyeDrop2' : datetime(2015, 9, 14, 10, 43),
    'EyeDrop3' : datetime(2015, 9, 14, 10, 53),
    'ExamStart' : datetime(2015, 9, 14, 11, 25),
    'ExamEnd' : datetime(2015, 9, 14, 11, 29)
}

ROP011 = { #Dr. Fan Extra Long One
    'EyeDrop1' : datetime(2015, 9, 23, 14, 12),
    'EyeDrop2' : datetime(2015, 9, 23, 14, 19),
    'EyeDrop3' : datetime(2015, 9, 23, 14, 28),
    'ExamStart' : datetime(2015, 9, 23, 15, 8),
    'ExamEnd' : datetime(2015, 9, 23, 15, 24)
}

ROP012 = {
    'EyeDrop1' : datetime(2015, 10, 7, 6, 7),
    'EyeDrop2' : datetime(2015, 10, 7, 6, 13),
    'EyeDrop3' : datetime(2015, 10, 7, 6, 17),
    'ExamStart' : datetime(2015, 10, 7, 7, 32),
    'ExamEnd' : datetime(2015, 10, 7, 7, 37)
}

ROP013 = {
    'EyeDrop1' : datetime(2015, 10, 14, 8, 30),
    'EyeDrop2' : datetime(2015, 10, 14, 8, 35),
    'EyeDrop3' : datetime(2015, 10, 14, 8, 40),
    'ExamStart' : datetime(2015, 10, 14, 9, 36),
    'ExamEnd' : datetime(2015, 10, 14, 9, 40)
}

ROP014 = {
    'EyeDrop1' : datetime(2015, 10, 28, 7, 35),
    'EyeDrop2' : datetime(2015, 10, 28, 7, 40),
    'EyeDrop3' : datetime(2015, 10, 28, 7, 45),
    'ExamStart' : datetime(2015, 10, 28, 8, 54),
    'ExamEnd' : datetime(2015, 10, 28, 8, 57)
}

ROP015 = {
    'EyeDrop1' : datetime(2015, 11, 4, 8, 0),
    'EyeDrop2' : datetime(2015, 11, 4, 8, 5),
    'EyeDrop3' : datetime(2015, 11, 4, 8, 10),
    'ExamStart' : datetime(2015, 11, 4, 8, 52),
    'ExamEnd' : datetime(2015, 11, 4, 8, 56)
}

ROP017 = {
    'EyeDrop1' : datetime(2016, 1, 13, 8, 25),
    'EyeDrop2' : datetime(2016, 1, 13, 8, 30),
    'EyeDrop3' : datetime(2016, 1, 13, 8, 35),
    'ExamStart' : datetime(2016, 1, 13, 10, 8),
    'ExamEnd' : datetime(2016, 1, 13, 10, 12)
}


ROP018 = {
    'EyeDrop1' : datetime(2016, 1, 20, 7, 35),
    'EyeDrop2' : datetime(2016, 1, 20, 7, 40),
    'EyeDrop3' : datetime(2016, 1, 20, 7, 45),
    'ExamStart' : datetime(2016, 1, 20, 8, 59),
    'ExamEnd' : datetime(2016, 1, 20, 9, 3)
}

ROP019 = {
    'EyeDrop1' : datetime(2016, 1, 27, 7, 49),
    'EyeDrop2' : datetime(2016, 1, 27, 7, 54),
    'EyeDrop3' : datetime(2016, 1, 27, 8, 0),
    'ExamStart' : datetime(2016, 1, 27, 8, 42),
    'ExamEnd' : datetime(2016, 1, 27, 8, 46)
}

ROP020 = {
    'EyeDrop1' : datetime(2016, 2, 10, 8, 30),
    'EyeDrop2' : datetime(2016, 2, 10, 8, 37),
    'EyeDrop3' : datetime(2016, 2, 10, 8, 45),
    'ExamStart' : datetime(2016, 2, 10, 10, 12),
    'ExamEnd' : datetime(2016, 2, 10, 10, 16)
}

ROP021 = {
    'EyeDrop1' : datetime(2016, 2, 17, 6, 54),
    'EyeDrop2' : datetime(2016, 2, 17, 6, 59),
    'EyeDrop3' : datetime(2016, 2, 17, 7, 4),
    'ExamStart' : datetime(2016, 2, 17, 8, 39),
    'ExamEnd' : datetime(2016, 2, 17, 8, 42)
}

ROP022 = {
    'EyeDrop1' : datetime(2016, 4, 20, 9, 15),
    'EyeDrop2' : datetime(2016, 4, 20, 9, 20),
    'EyeDrop3' : datetime(2016, 4, 20, 9, 25),
    'ExamStart' : datetime(2016, 4, 20, 11, 1),
    'ExamEnd' : datetime(2016, 4, 20, 11, 5)
}

ROP023 = {
    'EyeDrop1' : datetime(2016, 4, 27, 8, 19),
    'EyeDrop2' : datetime(2016, 4, 27, 8, 24),
    'EyeDrop3' : datetime(2016, 4, 27, 8, 29),
    'ExamStart' : datetime(2016, 4, 27, 9, 36),
    'ExamEnd' : datetime(2016, 4, 27, 9, 40)
}

ROP025 = {
    'EyeDrop1' : datetime(2016, 7, 13, 8, 16),
    'EyeDrop2' : datetime(2016, 7, 13, 8, 21),
    'EyeDrop3' : datetime(2016, 7, 13, 8, 26),
    'ExamStart' : datetime(2016, 7, 13, 10, 38),
    'ExamEnd' : datetime(2016, 7, 13, 10, 42)
}

ROP026 = {
    'EyeDrop1' : datetime(2016, 10, 10, 6, 19),
    'EyeDrop2' : datetime(2016, 10, 10, 6, 24),
    'EyeDrop3' : datetime(2016, 10, 10, 6, 29),
    'ExamStart' : datetime(2016, 10, 10, 7, 42),
    'ExamEnd' : datetime(2016, 10, 10, 7, 46)
}

ROP027 = {
    'EyeDrop1' : datetime(2016, 10, 17, 8, 42),
    'EyeDrop2' : datetime(2016, 10, 17, 8, 50),
    'EyeDrop3' : datetime(2016, 10, 17, 8, 55),
    'ExamStart' : datetime(2016, 10, 17, 9, 50),
    'ExamEnd' : datetime(2016, 10, 17, 9, 54)
}

#Same Time Now

ROP028 = {
    'EyeDrop1' : datetime(2017, 1, 11, 8, 31),
    'EyeDrop2' : datetime(2017, 1, 11, 8, 36),
    'EyeDrop3' : datetime(2017, 1, 11, 8, 41),
    'ExamStart' : datetime(2017, 1, 11, 9, 33),
    'ExamEnd' : datetime(2017, 1, 11, 9, 37)
}

ROP029 = { #for ROP029, have to subtract 5 minutes from every point)
    'EyeDrop1' : datetime(2017, 2, 1, 7, 42),
    'EyeDrop2' : datetime(2017, 2, 1, 7, 47),
    'EyeDrop3' : datetime(2017, 2, 1, 7, 52),
    'ExamStart' : datetime(2017, 2, 1, 8, 55),
    'ExamEnd' : datetime(2017, 2, 1, 8, 59)
}

ROP030 = {
    'EyeDrop1' : datetime(2017, 2, 8, 8, 35),
    'EyeDrop2' : datetime(2017, 2, 8, 8, 40),
    'EyeDrop3' : datetime(2017, 2, 8, 8, 45),
    'ExamStart' : datetime(2017, 2, 8, 12, 36),
    'ExamEnd' : datetime(2017, 2, 8, 12, 40)
}

ROP031 = {
    'EyeDrop1' : datetime(2017, 2, 15, 8, 19),
    'EyeDrop2' : datetime(2017, 2, 15, 8, 25),
    'EyeDrop3' : datetime(2017, 2, 15, 8, 34),
    'ExamStart' : datetime(2017, 2, 15, 8, 43),
    'ExamEnd' : datetime(2017, 2, 15, 8, 47)
}

ROP032 = {
    'EyeDrop1' : datetime(2017, 3, 1, 7, 31),
    'EyeDrop2' : datetime(2017, 3, 1, 7, 36),
    'EyeDrop3' : datetime(2017, 3, 1, 7, 41),
    'ExamStart' : datetime(2017, 3, 1, 8, 12),
    'ExamEnd' : datetime(2017, 3, 1, 8, 16)
}

ROP033 = {
    'EyeDrop1' : datetime(2017, 3, 8, 14, 15),
    'EyeDrop2' : datetime(2017, 3, 8, 14, 20),
    'EyeDrop3' : datetime(2017, 3, 8, 14, 25),
    'ExamStart' : datetime(2017, 3, 8, 14, 56),
    'ExamEnd' : datetime(2017, 3, 8, 15, 0)
}

ROP034 = {
    'EyeDrop1' : datetime(2017, 3, 22, 13, 30),
    'EyeDrop2' : datetime(2017, 3, 22, 13, 35),
    'EyeDrop3' : datetime(2017, 3, 22, 13, 40),
    'ExamStart' : datetime(2017, 3, 22, 14, 50),
    'ExamEnd' : datetime(2017, 3, 22, 14, 54)
}

ROP035 = {
	'EyeDrop1' : datetime(2017, 4, 12, 8, 41),
	'EyeDrop2' : datetime(2017, 4, 12, 8, 46),
	'EyeDrop3' : datetime(2017, 4, 12, 8, 51),
	'ExamStart' : datetime(2017, 4, 12, 9, 32),
	'ExamEnd' : datetime(2017, 4, 12, 9, 36)
}

ROP036 = {
	'EyeDrop1' : datetime(2017, 9, 20, 6, 10),
	'EyeDrop2' : datetime(2017, 9, 20, 6, 18),
	'EyeDrop3' : datetime(2017, 9, 20, 6, 24),
	'ExamStart' : datetime(2017, 9, 20, 6, 53),
	'ExamEnd' : datetime(2017, 9, 20, 6, 57)
}

ROP037 = {
	'EyeDrop1' : datetime(2017, 9, 20, 6, 3),
	'EyeDrop2' : datetime(2017, 9, 20, 6, 8),
	'EyeDrop3' : datetime(2017, 9, 20, 6, 13),
	'ExamStart' : datetime(2017, 9, 20, 6, 58),
	'ExamEnd' : datetime(2017, 9, 20, 7, 2)
}

ROP038 = {
	'EyeDrop1' : datetime(2017, 9, 27, 5, 29),
	'EyeDrop2' : datetime(2017, 9, 27, 5, 35),
	'EyeDrop3' : datetime(2017, 9, 27, 5, 40),
	'ExamStart' : datetime(2017, 9, 27, 6, 19),
	'ExamEnd' : datetime(2017, 9, 27, 6, 23)
}

ROP039 = {
	'EyeDrop1' : datetime(2017, 9, 27, 5, 38),
	'EyeDrop2' : datetime(2017, 9, 27, 5, 44),
	'EyeDrop3' : datetime(2017, 9, 27, 5, 50),
	'ExamStart' : datetime(2017, 9, 27, 6, 35),
	'ExamEnd' : datetime(2017, 9, 27, 6, 39)
}

ROP040 = {
	'EyeDrop1' : datetime(2017, 10, 18, 7, 45),
	'EyeDrop2' : datetime(2017, 10, 18, 7, 50),
	'EyeDrop3' : datetime(2017, 10, 18, 7, 55),
	'ExamStart' : datetime(2017, 10, 18, 8, 35),
	'ExamEnd' : datetime(2017, 10, 18, 8, 39)
}

ROP041 = {
	'EyeDrop1' : datetime(2017, 10, 25, 7, 40),
	'EyeDrop2' : datetime(2017, 10, 25, 7, 45),
	'EyeDrop3' : datetime(2017, 10, 25, 7, 50),
	'ExamStart' : datetime(2017, 10, 25, 9, 6),
	'ExamEnd' : datetime(2017, 10, 25, 9, 9)
}

ROP042 = {
	'EyeDrop1' : datetime(2017, 11, 1, 8, 19),
	'EyeDrop2' : datetime(2017, 11, 1, 8, 32),
	'EyeDrop3' : datetime(2017, 11, 1, 8, 43),
	'ExamStart' : datetime(2017, 11, 1, 9, 36),
	'ExamEnd' : datetime(2017, 11, 1, 9, 40)
}

ROP043 = {
	'EyeDrop1' : datetime(2017, 11, 1, 8, 29),
	'EyeDrop2' : datetime(2017, 11, 1, 8, 40),
	'EyeDrop3' : datetime(2017, 11, 1, 8, 48),
	'ExamStart' : datetime(2017, 11, 1, 9, 56),
	'ExamEnd' : datetime(2017, 11, 1, 10)
}

ROP044 = {
	'EyeDrop1' : datetime(2017, 11, 8, 8, 40),
	'EyeDrop2' : datetime(2017, 11, 8, 8, 45),
	'EyeDrop3' : datetime(2017, 11, 8, 8, 50),
	'ExamStart' : datetime(2017, 11, 8, 9, 51),
	'ExamEnd' : datetime(2017, 11, 8, 9, 55)
}

ROP045 = {
	'EyeDrop1' : datetime(2017, 11, 8, 8, 35),
	'EyeDrop2' : datetime(2017, 11, 8, 8, 42),
	'EyeDrop3' : datetime(2017, 11, 8, 8, 49),
	'ExamStart' : datetime(2017, 11, 8, 9, 39),
	'ExamEnd' : datetime(2017, 11, 8, 9, 43)
}


