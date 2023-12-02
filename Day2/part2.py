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
    in_game_red, in_game_green, in_game_blue = 0,0,0
    for combi in color_combination:
        print()
        
        for x in combi.split(", "):
            color = x.split(" ")[-1]
            number = int(x.split(" ")[-2])
            print(color,number)
            if color == "red":
                if number > in_game_red:
                    in_game_red = number
            elif color == "green":
                if number > in_game_green:
                    in_game_green = number
            elif color == "blue":
                if number > in_game_blue:
                    in_game_blue = number
            
    print(in_game_red, in_game_green, in_game_blue)
    multiplied_value = in_game_red* in_game_green* in_game_blue
    totalSum += multiplied_value

print(totalSum)

