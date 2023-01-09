

# '함수이름' 부분에만 각자 만든 함수 이름 넣으시면 됩니다 (2군데)
# 각자 만든 함수는 import하거나 복붙하기


import random


players = ['윤정', '준서', '홍구', '채원', '선재']
players_re = []
right_now = []
right_now_final = {}
players_amount = [2, 4, 6, 8, 10]
players_amount_re = []
player_dic = {}


def apartment(player, list):

    print('''
--------------------------------------------------------------------------------------
           ___                       _                            _   
          / _ \                     | |                          | |  
         / /_\ \ _ __    __ _  _ __ | |_  _ __ ___    ___  _ __  | |_ 
         |  _  || '_ \  / _` || '__|| __|| '_ ` _ \  / _ \| '_ \ | __|
         | | | || |_) || (_| || |   | |_ | | | | | ||  __/| | | || |_ 
         \_| |_/| .__/  \__,_||_|    \__||_| |_| |_| \___||_| |_| \__|
                | |                                                   
                |_|                                                   
--------------------------------------------------------------------------------------
    ''')
    list_list_list = []
    list_final = []
    apart_number = int(input('10부터 30사이의 숫자를 하나 골라주세요! : '))

    list_list = list + list
    num = 0
    random.shuffle(list_list)
    list_final = list_list*10

    for i in range(apart_number):
        print("🤚 ", list_final[i])

    print("아 누가 술을 마셔 🤔 {0}(이)가 술을 마셔 원 ~~ 샷 🍺".format(
        list_final[apart_number-1]))

    return list_final[apart_number-1]


print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              ___   _               _             _
             / _ \ | |             | |           | |
            / /_\ \| |  ___   ___  | |__    ___  | |   __ _   __ _  _ __ ___    ___
            |  _  || | / __| / _ \ | '_ \  / _ \ | |  / _` | / _` || '_ ` _ \  / _ \\
            | | | || || (__ | (_) || | | || (_) || | | (_| || (_| || | | | | ||  __/
            \_| |_/|_| \___| \___/ |_| |_| \___/ |_|  \__, | \__,_||_| |_| |_| \___|
                                                        __/ |
                                                        |___/

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                  🍺(╯✧▽✧)╯ 마시면서 배우는 술 ~ 게 ~ 임 (╯✧▽✧)╯🍺
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')

while (True):
    try:
        starter = input('게임을 진행할까요? (y/n) : ')
        if starter == 'y':
            break
        elif starter == 'n':
            quit()
        else:
            raise Exception(
                'input only y or n')
    except Exception as e:
        print(e)

player = input('오늘 거하게 취해볼 당신의 이름은? : ')

print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 소주 기준 당신의 주량은? ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                1. 소주 반병(2잔)
                                2. 소주 반병~한병(4잔)
                                3. 소주 한병~한병 반(6잔)
                                4. 소주 한병 반~두병(8잔)
                                5. 소주 두병 이상(10잔)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ''')


while (True):
    try:
        my_amount = int(input('당신의 치사량(주량)🍺은 얼마만큼인가요?(1~5를 선택해주세요) : '))
        player_amount = 0

        if my_amount == 1:
            player_amount = 2
        elif my_amount == 2:
            player_amount = 4
        elif my_amount == 3:
            player_amount = 6
        elif my_amount == 4:
            player_amount = 8
        elif my_amount == 5:
            player_amount = 10
        else:
            raise Exception(
                'input only integer 1~5')
        break
    except Exception as e:
        print(e)


while (True):
    try:
        play_number = int(
            input('함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기로 인해 3명까지 초대 가능합니다!) : '))
        if play_number > 3:
            raise Exception(
                'The maximum number of friends you can invite is 3.')
        else:
            break
    except Exception as e:
        print(e)

players.remove(player)
players_re = random.sample(players, play_number)  # 나빼고 나머지가 저장
players_amount_re = random.sample(players_amount, play_number)
players_amount_re.append(player_amount)

for i in range(play_number+5):
    right_now.append(0)

for i in range(play_number):
    print("오늘 함께 취할 친구는 {0}입니다! (치사량 : {1})".format(
        players_re[i], players_amount_re[i]))

players_re.append(player)

right_now_final = dict(zip(players_re, right_now))
player_dic = dict(zip(players_re, players_amount_re))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 첫번째 게임 시작


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for name in players_re:
    print('{0}(이)는 지금까지 {1}🍺!'.format(
        name, right_now_final[name]), end="")
    value = player_dic[name]-right_now_final[name]
    print(' 치사량까지 {0}'.format(value))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~🍺 오늘의 Alcohol GAME 🍺~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                    🍺 1. 아파트 게임
                                    🍺 2. 369 게임
                                    🍺 3. 초성 게임
                                    🍺 4. 지하철 게임
                                    🍺 5. 소주병뚜껑 게임
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ''')

current_player = player
choice = input(
    '{0}(이)가~ 좋아하는~ 랜덤~ 게임~! 무슨~ 게임? : '.format(current_player))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('{0} 님이 게임을 선택하셨습니다! 😄'.format(current_player))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
if choice == '1':
    drink = apartment(current_player, players_re)
elif choice == '2':

    # drink = 함수이름(current_player, players_re)
    print("2")

elif choice == '3':

    # drink = 함수이름(current_player, players_re)
    print("3")

elif choice == '4':

    # drink = 함수이름(current_player, players_re)
    print("4")

elif choice == '5':

    # drink = 함수이름(current_player, players_re)
    print("5")

right_now_final[drink] += 1


# 두번째부터 마지막 게임

while (True):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    for name in players_re:
        print('{0}(이)는 지금까지 {1}🍺!'.format(
            name, right_now_final[name]), end="")
        value = player_dic[name]-right_now_final[name]
        print(' 치사량까지 {0}'.format(value))

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    for name in players_re:
        if player_dic[name]-right_now_final[name] == 0:
            print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                _____   ___  ___  ___ _____   _____  _   _  _____ ______ 
                |  __ \ / _ \ |  \/  ||  ___| |  _  || | | ||  ___|| ___ \\
                | |  \// /_\ \| .  . || |__   | | | || | | || |__  | |_/ /
                | | __ |  _  || |\/| ||  __|  | | | || | | ||  __| |    / 
                | |_\ \| | | || |  | || |___  \ \_/ /\ \_/ /| |___ | |\ \ 
                 \____/\_| |_/\_|  |_/\____/   \___/  \___/ \____/ \_| \_|

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                                                
    ''')
            print("{0}(이)가 전사했습니다 ... 꿈나라에서는 편히 쉬시길 ... ZZZ".format(name))
            print(
                "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("🍺 다음에 술 마시면 또 불러주세요~ 안녕! 🍺")
            print(
                "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            quit()

    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~🍺 오늘의 Alcohol GAME 🍺~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                    🍺 1. 아파트 게임
                                    🍺 2. 369 게임
                                    🍺 3. 초성 게임
                                    🍺 4. 지하철 게임
                                    🍺 5. 소주병뚜껑 게임
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ''')

    status = input(
        '술게임 진행중! 다른 사람의 턴입니다. 그만하고 싶으면 "exit"을, 계속하고 싶으면 아무거나 입력해주세요! : ')
    if status == 'exit':
        quit()

    current_player = random.choice(players_re)

    choice = input('{0}(이)가~ 좋아하는~ 랜덤~ 게임~! 무슨~ 게임? : '.format(current_player))

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('{0} 님이 게임을 선택하셨습니다! 😄'.format(current_player))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    if choice == '1':
        drink = apartment(current_player, players_re)

    elif choice == '2':

        # drink = 함수이름(current_player, players_re)
        print("2")

    elif choice == '3':

        # drink = 함수이름(current_player, players_re)
        print("2")

    elif choice == '4':

        # drink = 함수이름(current_player, players_re)
        print("4")
    elif choice == '5':

        # drink = 함수이름(current_player, players_re)
        print("5")

    right_now_final[drink] += 1