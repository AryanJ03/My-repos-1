import sqlite3

connection = sqlite3.connect("uni_table.db")

crsr = connection.cursor()

sql_command = '''CREATE TABLE universities(
  id SERIAL PRIMARY KEY,
  Name VARCHAR NOT NULL,
  Overall_Score INTEGER NOT NULL,
  Student_Satisfaction INTEGER NOT NULL,
  Entry_Standards INTEGER NOT NULL,
  Research_Quality INTEGER NOT NULL
);
'''

crsr.execute(sql_command)

sql_command = '''INSERT INTO universities VALUES(1, "Cambridge", 1000, 4.09, 224, 3.33);'''
crsr.execute(sql_command)

sql_command = '''INSERT INTO universities VALUES
(2, "Oxford", 989, 4.1, 215, 3.34),
(3, "St.Andrews", 944, 4.26, 207, 3.13),
(4, "London School Of Economics", 934, 3.67, 189, 3.35),
(5, "Imperial College London", 933, 4.02, 205, 3.36),
(6, "Durham", 915, 4.01, 194, 3.14),
(7, "Lancaster", 914, 4.14, 156, 3.15),
(8, "Loughbrough", 905, 4.18, 157, 2.95),
(9, "Bath", 882, 4.05, 183, 3.17),
(10, "University College London", 880, 3.87, 187, 3.22),
(11, "Exeter", 868, 4.08, 171, 3.08),
(12, "Warwick", 868, 4.05, 171, 3.22),
(13, "Birmingham", 841, 4.01, 163, 3.07),
(14, "Leeds", 838, 4.09, 164, 3.13),
(15, "Manchester", 827, 3.98, 168, 3.16),
(16, "Edinburgh", 826, 3.84, 189, 3.18),
(17, "Bristol", 826, 3.95, 177, 3.18),
(18, "Glasgow", 823, 4.06, 196, 3.10),
(19,"Nottingham", 814, 4.02, 162, 3.09),
(20, "Southampton", 804, 4.03, 161, 3.15),
(21, "East Anglia UEA", 802, 4.01, 147, 3.11),
(22, "Newcastle", 800, 4.03, 160, 3.09),
(23, "Royal Holloway_University of London", 798, 4.02, 141, 3.09),
(24, "Surrey", 798, 4.04, 156, 2.98),
(25, "Kings college London", 795, 3.84, 171, 3.23),
(26,"Cardiff", 786, 3.99, 158, 3.27),
(27,"Harper Adams", 785, 4.09, 134, 2.66),
(28,"liverpool", 776, 4.08, 145, 3.06),
(29,"Aberdeen", 774, 4.08, 183, 2.97),
(30,"York", 773, 4.09, 157, 3.17),
(31,"Dundee", 772, 4.16, 168, 3.03),
(32,"Sussex", 768, 3.91, 148, 3.01),
(33,"Sheiffeld", 767, 4.04, 157, 3.17),
(34,"Aston", 763, 4.02, 131, 3.05),
(35,"Swansea", 756, 4.08, 130, 3.09),
(36,"Heriot-Watt", 756, 3.94, 162, 3.06),
(37,"Queen's Belfast", 755, 3.97, 150, 2.99),
(38,"Nottingham Trent", 753, 4.14, 134, 2.59),
(39,"Strathclyde", 747, 3.95, 198, 3.04),
(40,"Reading", 746, 3.85, 132, 3.03);
'''
crsr.execute(sql_command)


sql_command = '''SELECT * FROM universities;'''
crsr.execute(sql_command)
connection.commit()



connection.close()