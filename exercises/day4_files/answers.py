# file = "file1.txt"
# 
# handle = open(file, "r")  
# contents = handle.readlines()
# handle.close()
# 
# f = open("upper_file1.txt", "w")
# for line in contents:
#     f.write(line.upper())
# f.close()
#     
# with open("upper_file1.txt", "a") as orange:
#     orange.write("\nI just created this upper-case file!")

with open("flu_sequences.fasta", "r") as infile:
    flu = infile.read()
    infile.seek(0)
    flulines = infile.readlines()
 
i = 0
for line in flulines:
    i += len(line) 
print i
  
# characters
# print len(flu)
# 
# lines
# lines = flu.split("\n")
# print len(lines)
# 
# loop!
# for i in range(10):
#     print lines[i]
# 
# 
# 
# with open("flu_sequences.fasta", "r") as infile:
#     flu = infile.read()
# 
# 
# 
# 
# 
# 
# 
# 











