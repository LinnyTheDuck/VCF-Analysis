last = ""
with open("wgEncodeGencodeBasicV17.txt") as file:
    for line in file:
        # if line.startswith("#"):
        #     continue
        cur = line.split("\t")[2]
        if (last != cur):
            print(cur)
            last = cur
