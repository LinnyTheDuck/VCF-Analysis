import typing as t
import sys

exon_ranges: t.List = []

if len(sys.argv) != 3:
    print("Usage: python3 find_in_range.py <start> <end>")
    exit(1)

start = int(sys.argv[1])
end = int(sys.argv[2])
count = 0
with open("../chromosome11_exon_ranges.vcf") as file:
    for line in file:
        vals = line.split("\t")
        pos = int(vals[1])
        if pos >= start and pos <= end:
            count += 1
            print(line, end="")

print("Found " + str(count) + " records withing range " + str(start) + " to " + str(end))

