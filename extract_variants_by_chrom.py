with open("merged10mb.vcf") as file:
    for line in file:
        vals = line.split("\t")
        # if vals[0] == "11":
        print(vals[0])
