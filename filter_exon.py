import string
import typing as t
from intervaltree import Interval, IntervalTree

exon_ranges: t.List = []
# starts: t.List = []
# exon_ranges: t.Dict = {}
# exon_ranges = IntervalTree()


with open("exon_ranges.txt") as file:
    for line in file:
        vals = line.split(" ")
        chrom = vals[0]
        start = int(vals[1])
        end = int(vals[2])
        if chrom == "11":
            # exon_ranges[start:end] = (start, end)
            exon_ranges.append([start, end])


with open("chromosome11.vcf") as file:
    for line in file:
        vals = line.split("\t")
        pos = int(vals[1])
        # if exon_ranges.overlaps_point(pos):
        #     print(line)
        for [start, end] in exon_ranges:
            if pos >= start and pos <= end:
                print(line, end="")
                break

# def in_range(line: string):
