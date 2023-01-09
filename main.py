

# '함수이름' 부분에만 각자 만든 함수 이름 넣으시면 됩니다 (2군데)
# 각자 만든 함수는 import하거나 복붙하기


import random
from time import sleep


players = ['윤정', '준서', '홍구', '채원', '선재']
players_re = []
right_now = []
right_now_final = {}
players_amount = [2, 4, 6, 8, 10]
players_amount_re = []
player_dic = {}
playersIndex=len(players)-1 #플레이어의 번호

def grading(tagger,temp,ans,now):#temp는 추측한 수
    print(f"{now} : {temp} ")
    if temp<ans:
        print(f"{players[tagger]} : UP! ")
        tryans=random.randrange(temp+1,51) #다음사람이 도전 할 숫자
        sleep(0.5)
        return tryans
    elif temp>ans:
        print(f"{players[tagger]} : DOWN! ")
        tryans=random.randrange(0,temp) #다음사람이 도전 할 숫자
        sleep(0.5)
        return tryans
    else:
        tryans=-1
        return tryans

def correct(now):
    if players.index(now)==playersIndex:
        print(f"{now}이/가 정답을 맞췄음으로 다음 사람인 {players[0]} 이/가 술을 마십니다@@")
        return players[0]
    else:
        print(f"{now}이/가 정답을 맞췄음으로 다음 사람인 {players[players.index(now)+1]} 이/가 술을 마십니다@@")
        return players[players.index(now)+1]

def updownGs(current_player, players):
    #인트로~~
    print(current_player)
    print(players_re)
    print('''
--------------------------------------------------------------------------------------
          _   _ ______            ______  _____  _    _  _   _ 
         | | | || ___ \   ___     |  _  \|  _  || |  | || \ | |
         | | | || |_/ /  ( _ )    | | | || | | || |  | ||  \| |
         | | | ||  __/   / _ \/\  | | | || | | || |/\| || . ` |
         | |_| || |     | (_>  <  | |/ / \ \_/ /\  /\  /| |\  |
          \___/ \_|      \___/\/  |___/   \___/  \/  \/ \_| \_/
                                                
--------------------------------------------------------------------------------------
    ''')

    print(" 까드드드득~ 까드드득~🍾🍾")
    sleep(0.5)
    print("""( •ω• ) 하나
 | ハ|""")
    sleep(0.5)
    print("""( •ω• ) 둘
 | 乂|""")
    sleep(0.5)
    print("""(|•ω•|) 셋!
 | 　|""")
    print("""♫♪♫"업 엔 다운~~ 업 엔 다운!♫♪♫""")
    #인트로~~

    choice=list(range(1,51,1)) #선택했던 숫자들 빼고!
    tagger=random.randrange(0,len(players)) #술래 인덱스
    print(f"술래는 {players[tagger]}!!!")
    print(f"게임 진행 순서 :{players}") #추가
    ans=random.randrange(1,51) #정답
    print(f"정답은 {ans}")
    tryans=0
    temp=20
    tryans=random.randrange(1,51) #도전하는 수
    playersIndex=len(players)-1 #플레이어의 번호
    
    #술래 == 플레이어
    if tagger==playersIndex:
        print(f"소주 뚜껑에 적힌 숫자는 {ans} 입니다! 잘 기억하고 대답해주세요 (* ＞з＜)")
        #화면 리셋 시킬까....?
        print("----------START----------")
        while tryans != ans:
            for now in players*2:
                if tryans==ans or temp==-2:
                    break #게임 끝
                if players.index(now)==tagger:
                    temp=0 #술래 차례
                    continue
                else:
                    print(f"{now} : {tryans}!!") #첫번째 추측
                    quest=input(">>>> up or down?(u/d)")
                    if quest=="u" and tryans<ans:
                        tryans=random.randrange(tryans+1,51) #다음사람이 도전 할 숫자
                        continue
                    elif (tryans<ans and quest!="u") or (tryans>ans and quest!="d"):
                        print("이런... 술래가 틀려버렸네요")
                        print(f"술래인 {players[tagger]} 이/가 술을 마십니다")
                        temp=-2
                        return players[tagger]

                    elif quest=="d" and tryans>ans:
                        tryans=random.randrange(0,tryans) 
                        continue
                    elif tryans==ans: #게임 끝
                        drinking=correct(now)
                        temp=-1         
                        return drinking      

            if temp !=-1 and temp!=-2:
                print("이런... 2바퀴동안 아무도 못맞췄어요ㅠㅠ")
                print("이게임 누가했어!😫😫  이게임 누가했어!😫😫")
                print(f"술래인 {players[tagger]} 이/가 술을 마십니다")
                return players[tagger]

    #술래 != 플래이어
    else:
        while tryans != ans:
            for now in players*2:
                if players.index(now)==tagger: #술래 차례
                    continue
                elif players.index(now)==playersIndex: #플레이어 차례
                    temp=int(input("숫자를 맞춰보세요!(1~50) : "))
                    tryans=grading(tagger,temp,ans,now)
                    if tryans==-1: # 플레이어가 정답 맞춘 경우
                        break
                else: #다른 사람들 차례
                    temp=tryans
                    tryans=grading(tagger,temp,ans,now)
                    if tryans==-1:
                        break
            if tryans !=-1:
                print("이런... 2바퀴동안 아무도 못맞췄어요ㅠㅠ")
                print("이게임 누가했어!😫😫  이게임 누가했어!😫😫 ")
                print(f"술래인 {players[tagger]} 이/가 술을 마십니다")
                return players[tagger]
                players[tagger][1]-=1
                break
            else : #차례가 끝나기 전에 맞춤
                drinking=correct(now)
                return drinking      



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

    # drink = game_369(current_player, players_re)
    print("2")

elif choice == '3':

    # drink = 함수이름(current_player, players_re)
    print("3")

elif choice == '4':

    # drink = 함수이름(current_player, players_re)
    print("4")

elif choice == '5':

    drink = updownGs(current_player, players_re)
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

        # drink = game_369(current_player, players_re)
        print("2")

    elif choice == '3':

        # drink = 함수이름(current_player, players_re)
        print("2")

    elif choice == '4':

        # drink = 함수이름(current_player, players_re)
        print("4")
    elif choice == '5':

        drink = updownGs(current_player, players_re)
        print("5")

    right_now_final[drink] += 1
