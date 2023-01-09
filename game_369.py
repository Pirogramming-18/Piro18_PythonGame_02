import time; import random

def game_369(current_player, players_re, myself):

    print('''
    --------------------------------------------------------------------------------------

                _____   ____   _____   _____                         
                |____ | / ___| |  _  | |  __ \                        
                    / // /___  | |_| | | |  \/  __ _  _ __ ___    ___ 
                    \ \| ___ \ \____ | | | __  / _` || '_ ` _ \  / _ |
                .___/ /| \_/ | .___/ / | |_\ \| (_| || | | | | ||  __|
                \____/ \_____/ \____/   \____/ \__,_||_| |_| |_| \___|
                                                        
    --------------------------------------------------------------------------------------
    ''')
    start_person_369 = random.choice(players_re)
    print('{}(이)가 좋아하는 랜덤~게임! 369 369! 369 369~'.format(current_player))
    print('먼저 랜덤으로 시작할 사람을 정할거에요!')
    print('본인의 차례가 되었을 때, input창에 본인이 말해야할 숫자를 적거나')
    print('3,6,9가 숫자 안에 들어있다면 그 개수만큼 박수를 쳐주세요! ex) 33 : (공백없이) "짝짝" 입력 ')
    print()
    print('먼저 시작할 사람은 ... ',end=' ')
    time.sleep(1)
    print(start_person_369, '입니다!')

    x = players_re.index(start_person_369)
    for _ in range(len(players_re)):
        print(players_re[x], end=' ')
        x = (x+1) % len(players_re)
    print('이 순서대로 진행할거에요!')
    x = players_re.index(start_person_369)
    num = 1
    print('3초 뒤에 시작할게요!')
    time.sleep(3)
    print('게 임 시 작 !')
    print('369 369! 369 369~')

    while True:
        
        choice = ans_or_wrong_369(num)
        correct_ans = choice[0]
        wrong_ans = choice[-1]
        if start_person_369 == current_player:
            final_choice = input('어떻게 대답할래요?')
        else:
            final_choice = random.choice(choice)
        print('{} : {} !!'.format(start_person_369,final_choice))

        if final_choice == correct_ans:
            x = (x+1) % len(players_re)
            start_person_369 = players_re[x]
            num += 1
            continue
        else:
            print('어이쿠!', start_person_369,'님, 틀렸어요! 정답은',correct_ans,'에요!')
            break
    print("아 누가 술을 마셔 🤔 {0}(이)가 술을 마셔 원 ~~ 샷 🍺".format(start_person_369))

    return start_person_369



    

def ans_or_wrong_369(num):
    answer_list = []
    answer = 0
    y = list(map(int,str(num)))
    for i in y:
        if i == 3 or i == 6 or i == 9:
            answer += 1
    if answer == 0:
        for __ in range(4):
            answer_list.append(str(num))
        answer_list.append('짝'*random.randint(1,3))
    else:
        for __ in range(4):
            answer_list.append('짝'*answer)
        answer_list.append(str(num))
    return answer_list

    
    