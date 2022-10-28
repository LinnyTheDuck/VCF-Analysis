# VCF-Analysis

A Variant Call File or VCF holds the genetic variations for one or more individuals. Many illnesses are linked to genetic causes that could be inherited, so from analysis of this file, one may be able to understand which genes are responsible for a particular illness. Our team was tasked to find the genetic variations that were responsible for two illnesses - Sickle Cell Anaemia and Retinitis Pigmentosa - in a family of seven where some family members would exhibit symptoms from either one or both illesses. We were given the inheritance diagram for both illnesses in the family, as well as 2 VCF files: one from a population sample of 2,000 people and one from the family of seven. Our approach consisted of narrowing down the genetic variations through filtering by chromosone, inheritance and exonic regions before making comparisons with the population and consulting current biological research and resources on the illnesses.
## Files

The two VCF files are the genes that we have narrowed the search down to.

Files prefixed with `d2` are specifically for the second disease.

The filters include:
- `chrom` - extract all variants on a certain chromosone
- `range` or `exon` -  filters all variants that fall into the exon ranges
- `pop` - filters for the population sample
- `inheritance` - filters for the family disease inheritance pattern

## Resources
ALL.merged.phase1_release_v3.20101123.snps_indels_svs.vcf.gz (564 MB)
	a vcf file with counts of known variants from 1092 individuals.
	Prepared by RTG, originally from 1000 genomes project.


diagram_jcleary.pptx
	Power-point presentation with the family and four disease associations (not for project)

merged.vcf.gz (2.0 GB)
	The variants for the simulated seven member family.

Schema for GENCODE Genes V17 - Gene Annotations from ENCODE/GENCODE Version 17.webarchive
	A web-page describing the contents of the file wgEncodeGencodeBasicV17.txt
	Originally downloaded by selecting the correct table from 
	http://genome.ucsc.edu/cgi-bin/hgTables


wgEncodeGencodeBasicV17.txt (24 MB)
	A file downloaded from http://hgdownload.soe.ucsc.edu/goldenPath/hg19/database/
	It contains (amongst many other things), the start and end of the gene and of individual
	exons as well as its "common" name.
	See the webpage above for a full description.

A useful website which can be used for searching for genes and related information in humans is:
	http://genome.ucsc.edu/cgi-bin/hgGateway

## Members of Silver Team

Stefenie Pickston 1506427

Daniel Shepherd 1514996

Cat Turnbull 1370807