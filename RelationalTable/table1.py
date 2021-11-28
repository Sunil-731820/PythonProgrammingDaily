from prettytable import PrettyTable
mytable = PrettyTable(["Name ","Class","Roll Number"])
mytable.add_row(["Sunil","12","1"])
print(mytable)
mytable.add_column("Locations",["Lucknow"])
print(mytable)
mytable.add_row(["Harish","11","2","Delhi"])
print(mytable)