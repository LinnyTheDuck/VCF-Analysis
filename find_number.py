import typing as t
import sys

exon_ranges: t.List = []


with open("exon_ranges_with_chromosomes.txt") as file:
    for line in file:
        vals = line.split(" ")
        chrom = vals[0]
        start = int(vals[1])
        end = int(vals[2])
        if chrom == "11":
            exon_ranges.append([start, end])

print(sys.argv[1])
to_find = int(sys.argv[1])

for [start, end] in exon_ranges:
    if to_find >= start and to_find <= end:
        print("Found! Range: " + str(start) + " " + str(end))
        exit()

print("Not found: " + str(to_find))
