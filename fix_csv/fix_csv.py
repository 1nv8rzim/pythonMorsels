import csv
import sys


old, new = sys.argv[1:]

with open(old, newline='') as old_csv:
    reader = csv.reader(old_csv, delimiter='|')
    with open(new, mode='wt', newline='') as new_csv:
        csv.writer(new_csv).writerows(reader)
