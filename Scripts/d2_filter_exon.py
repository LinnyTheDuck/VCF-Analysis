import string
import typing as t
from intervaltree import Interval, IntervalTree

# exon_ranges: t.List = []
# starts: t.List = []
# exon_ranges: t.Dict = {}
exon_ranges = IntervalTree()
chromy = "3"

with open("../exon_ranges.txt") as file:
    for line in file:
        vals = line.split(" ")
        chrom = vals[0]
        start = int(vals[1]) - 1000 # wiggle room for potential misread in exon region
        end = int(vals[2]) + 1000
        if chrom == chromy:
            exon_ranges[start:end] = (start, end)


with open("../d2_chr3_inheritance.vcf") as file:
    for line in file:
        vals = line.split("\t")
        pos = int(vals[1])
        if vals[0] == chromy:
            if exon_ranges.overlaps_point(pos):
                print(line, end="")