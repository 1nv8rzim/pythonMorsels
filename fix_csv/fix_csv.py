from sys import argv
import csv

with open(argv[1], 'r') as csv_old:
    csv_reader = csv.reader(csv_old, delimiter='|')
    with open(argv[2], 'w') as csv_new:
        csv_writer = csv.writer(csv_new)
        for line in csv_reader:
            csv_writer.writerow(line)
