import calendar 
"""
c=calendar.month(2012,2)
print (c)
"""
"""
Napisz program, ktory wyswietla pelny kalendarz roku podanego przez uzytkownika
"""
"""
year = int (input("Please entare a year \n"))
for miesiac in range(1,13):
	c=calendar.month(year, miesiac)
	print(c)
====================================================================================
	uzywtkowinik wpisuje jeden rok i drugi rok i program ma wypisac kalendarze dla 
	wszystkich lat w tym przedziale
"""	
year1 = int (input("Please, enter a 1st year"))
year2 = int (input("Please, enter a 2nd year"))

for rok in range(year1, year2+1):
	for miesiac in range(1,13):
		c=calendar.month(rok, miesiac)
		print(c)