import calendar 
"""
c=calendar.month(2012,2)
print (c)
"""
"""
Napisz program, ktory wyswietla pelny kalendarz roku podanego przez uzytkownika
"""

year = int (input("Please entare a year \n"))
for miesiac in range(1,13):
	c=calendar.month(year, miesiac)
	print(c)