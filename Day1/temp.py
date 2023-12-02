import re

bank = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
}

value =[]
with open('Day1/bank.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    
totalnum = 0
#pattern = r"\d|one|two|three|four|five|six|seven|eight|nine"
pattern = ["\d","one","two", "three", "four", "five", "six", "seven", "eight", "nine"]
for word in lines:
    res = re.findall(r"(?=("+'|'.join(pattern)+r"))", word)

    
    if res[0] in bank.keys():
        num1 = bank[res[0]]*10
    else:
        num1 = int(res[0])*10

    if res[-1] in bank.keys():
        num2 = bank[res[-1]]
    else:
        num2 = int(res[-1]) 

    num =  num1 + num2
    print(word,"\t",res,"\t",num)
    
    totalnum+=num

print(totalnum)