import re

#Provide address of the file correctly
handle=open("regex_sum_127577.txt")
numStrList=list()
sum = 0

for line in handle:
    line = line.rstrip()
    #uses Regular expression method to find all the numbers from the line
    numStrList = re.findall ("[0-9]+",line)
    if len(numStrList)!=0:
        for i in numStrList:
            sum=sum+int(i)
print(sum)
