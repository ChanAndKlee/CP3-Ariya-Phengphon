import csv
def readFile():
    with open('customerList.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')        # seperated by uisng comma
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')     # Print all column names
                line_count += 1
            else:
                print(f'[{row[0]}]. His/Her name is {row[1]}, Age: {row[2]}')
                print(f'He/She interested in {row[3]}.')
                print()
                line_count += 1
        print(f'[Processed {line_count} lines.]')

def writeFile():
    with open('employee_file.csv', mode='w', newline="") as employee_file:      # newline = "" > not to enter new redundant line.
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)        # csv.QUOTE_MINIMAL, then writerow() will quote fields only if they contain the delimeter or the quotechar [DEFAULT CASE]
        employee_writer.writerow(['John Smith', 'Accounting', 'November'])
        employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
readFile()
writeFile()