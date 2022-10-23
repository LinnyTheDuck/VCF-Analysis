# wgEncodeGencodeBasicV17.txt
with open("wgEncodeGencodeBasicV17.txt") as file:
    for line in file:
        if line.startswith("chrUn"):
            continue

        vals = line.split()
        chromosome = vals[2]
        if chromosome.startswith("chrY"):
            chromosome = "Y"
        elif chromosome.startswith("chrX"):
            chromosome = "X"
        else:
            chromosome = chromosome[3:5]
            if len(chromosome) > 1 and chromosome[1] == "_":
                chromosome = chromosome[0]
        starts = vals[9].split(',')
        ends = vals[10].split(',')
        for i in range(len(starts)):
            if starts[i] == "":
                continue
            print(chromosome + " " + starts[i] + " " + ends[i])
