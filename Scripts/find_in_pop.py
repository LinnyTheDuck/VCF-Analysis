family_variants = set()

with open("../d2_chr3_inh_exon1000.vcf") as file:
    for line in file:
        vals = line.split("\t")
        key = vals[0] + "-" + vals[1] # <chrom>-<pos>
        family_variants.add(key)

count = 0
with open("../large_files/ALL.merged.phase1_release_v3.20101123.snps_indels_svs.vcf") as file:
    for line in file:
        if line.startswith("#"):
            continue
        vals = line.split("\t")
        key = vals[0] + "-" + vals[1] # <chrom>-<pos>
        if key in family_variants:
            count += 1
            print(line, end="")
print("Found " + str(count) + " matching records")