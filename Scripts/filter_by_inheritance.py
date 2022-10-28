with open("../chromosome11_exon_ranges.vcf") as file:
    for line in file:
        vals = line.split("\t")

        # FATHER:9	MOTHER:10	DAUGHTER1:11	DAUGHTER2:12	DAUGHTER3:13	SON1:14	SON2:15

        father_left = vals[9][0]
        father_right = vals[9][2]

        mother_left = vals[10][0]
        mother_right = vals[10][2]

        d1_left = vals[11][0]
        d1_right = vals[11][2]

        d2_left = vals[12][0]
        d2_right = vals[12][2]

        d3_left = vals[13][0]
        d3_right = vals[13][2]

        s1_left = vals[14][0]
        s1_right = vals[14][2]

        s2_left = vals[15][0]
        s2_right = vals[15][2]

        father = (father_left != "0" or father_right != "0") # does this need to be exclusive or?
        mother = (mother_left != "0" or mother_right != "0")

        d1 = (d1_left != "0" or d1_right != "0")
        d2 = (d2_left != "0" and d2_right != "0")
        d3 = (d3_left == "0" and d3_right == "0")
        s1 = (s1_left != "0" or s1_right != "0")
        s2 = (s2_left != "0" and s2_right != "0")

        if(father and mother and d1 and d2 and d3 and s1 and s2):
            print(line, end="")        
