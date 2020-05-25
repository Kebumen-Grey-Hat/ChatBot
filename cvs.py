import csv



contak = []

with open('belajar.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    print(csv_reader)
    for row in csv_reader:
        contak.append(row)


labels = contak.pop(0)


print(f'{labels[0]} \t {labels[1]} \t\t {labels[2]}')
print("-"*34)
for data in contak:
    print(f'{data[0]} \t {data[1]} \t {data[2]}')
