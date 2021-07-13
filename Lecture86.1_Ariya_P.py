import csv
with open('Lecture86.1_Ariya_P.csv',mode='w') as csv_file:
    fieldnames = ['Num','Name','Birth_Month','Fav_Color']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Num': '0', 'Name':'Chan', 'Birth_Month':'October', 'Fav_Color':'Orange'})
    writer.writerow({'Num': '1', 'Name':'Edd', 'Birth_Month':'September', 'Fav_Color':'Blue'})
    writer.writerow({'Num': '2', 'Name': 'Kai', 'Birth_Month': 'July', 'Fav_Color': 'Orange'})
    writer.writerow({'Num': '3', 'Name': 'Jeab', 'Birth_Month': 'April', 'Fav_Color': 'Pink'})
    writer.writerow({'Num': '4', 'Name': 'Chart', 'Birth_Month': 'July', 'Fav_Color': 'Yellow'})