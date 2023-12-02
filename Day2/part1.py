with open('bank.txt') as f:
    lines = [line.rstrip('\n') for line in f]


bank = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}
totalSum =0
for line in lines:
    game = int(line.split(":")[0].split(" ")[1])
    color_combination = line.split(":")[1].split(";")
    print(game,color_combination)
    flag = True
    for combi in color_combination:
        print()
        
        for x in combi.split(", "):
            color = x.split(" ")[-1]
            number = int(x.split(" ")[-2])
            print(color,number,bank[color])
            if number > bank[color] :
                flag = False

    print(flag)
    if flag == True:
        totalSum += game
    
    print(totalSum)