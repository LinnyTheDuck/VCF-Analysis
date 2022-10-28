with open("../large_files/merged.vcf") as file:
    for line in file:
        vals = line.split("\t")
        if vals[0] == "X":
            print(line, end="")
