import csv

rows = [("1001","总监","1002","科学家")]

with open("./Learn\DATA\dataCSV\data.csv","a") as f:
    a_csv = csv.writer(f)
    a_csv.writerows(rows)