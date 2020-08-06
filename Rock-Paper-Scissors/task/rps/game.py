from random import choice


def move():
    user = input()
    print(check(user))


def check(player):
    win = {'rock': ['scissors', 'sponge', 'wolf', 'tree', 'snake', 'human', 'fire'],
           'gun': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'rock'],
           'lightning': ['tree', 'human', 'snake', 'scissors', 'gun', 'rock', 'fire'],
           'devil': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
           'dragon': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
           'water': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
           'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
           'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
           'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
           'wolf': ['lightning',  'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
           'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
           'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
           'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
           'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
           'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors']}
    computer = choice(characters)
    if player == '!exit':
        with open('rating.txt', 'w') as f_file:
            for _i in data_dict:
                f_file.writelines(f'{_i} {data_dict[_i]}\n')
        print('Bye!')
        exit()
    else:
        if player == '!rating':
            return f"Your rating: {data_dict[name]}"
        else:
            if player not in characters:
                return "invalid input"
            else:
                if player == computer:
                    data_dict[name] = data_dict[name] + 50
                    return f"There is a draw ({computer})"
                if computer in win[player]:
                    data_dict[name] = data_dict[name] + 100
                    return f"Well done. Computer chose {computer} and failed"
                else:
                    return f"Sorry, but computer chose {computer}"


name = input("Enter your name: ")
print(f"Hello, {name}")
with open('rating.txt', 'r+') as file:
    data = file.read()
    data_dict = {}
    for i in data.splitlines():
        data_dict[i.split()[0]] = int(i.split()[1])
    if name not in data_dict:
        data_dict[name] = 0
option = input()
print("Okay, let's start")
if option == '':
    characters = ['rock', 'paper', 'scissors']
else:
    option = option.split(',')
    characters = []
    for opt in option:
        characters.append(opt.strip().lower())

while True:
    move()
