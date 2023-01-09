import random
from time import sleep


def grading(tagger, temp, ans, now, players):  # temp는 추측한 수
    print(f"{now} : {temp} ")
    if temp < ans:
        print(f"{players[tagger]} : UP! ")
        tryans = random.randrange(temp+1, 51)  # 다음사람이 도전 할 숫자
        sleep(0.5)
        return tryans
    elif temp > ans:
        print(f"{players[tagger]} : DOWN! ")
        tryans = random.randrange(0, temp)  # 다음사람이 도전 할 숫자
        sleep(0.5)
        return tryans
    else:
        tryans = -1
        return tryans


def correct(now, players):
    if players.index(now) == playersIndex:
        print(f"{now}이/가 정답을 맞췄음으로 다음 사람인 {players[0]} 이/가 술을 마십니다@@")
        return players[0]
    else:
        print(
            f"{now}이/가 정답을 맞췄음으로 다음 사람인 {players[players.index(now)+1]} 이/가 술을 마십니다@@")
        return players[players.index(now)+1]


def updownGs(current_player, players):
    # 인트로~~
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
    # 인트로~~

    choice = list(range(1, 51, 1))  # 선택했던 숫자들 빼고!
    tagger = random.randrange(0, len(players))  # 술래 인덱스
    print(f"술래는 {players[tagger]}!!!")
    print(f"게임 진행 순서 :{players}")  # 추가
    ans = random.randrange(1, 51)  # 정답
    print(f"정답은 {ans}")
    tryans = 0
    temp = 20
    tryans = random.randrange(1, 51)  # 도전하는 수
    playersIndex = len(players)-1  # 플레이어의 번호

    # 술래 == 플레이어
    if tagger == playersIndex:
        print(f"소주 뚜껑에 적힌 숫자는 {ans} 입니다! 잘 기억하고 대답해주세요 (* ＞з＜)")
        # 화면 리셋 시킬까....?
        print("----------START----------")
        while tryans != ans:
            for now in players*2:
                if tryans == ans or temp == -2:
                    break  # 게임 끝
                if players.index(now) == tagger:
                    temp = 0  # 술래 차례
                    continue
                else:
                    print(f"{now} : {tryans}!!")  # 첫번째 추측
                    quest = input(">>>> up or down?(u/d)")
                    if quest == "u" and tryans < ans:
                        tryans = random.randrange(
                            tryans+1, 51)  # 다음사람이 도전 할 숫자
                        continue
                    elif (tryans < ans and quest != "u") or (tryans > ans and quest != "d"):
                        print("이런... 술래가 틀려버렸네요")
                        print(f"술래인 {players[tagger]} 이/가 술을 마십니다")
                        temp = -2
                        return players[tagger]

                    elif quest == "d" and tryans > ans:
                        tryans = random.randrange(0, tryans)
                        continue
                    elif tryans == ans:  # 게임 끝
                        drinking = correct(now, players)
                        temp = -1
                        return drinking

            if temp != -1 and temp != -2:
                print("이런... 2바퀴동안 아무도 못맞췄어요ㅠㅠ")
                print("이게임 누가했어!😫😫  이게임 누가했어!😫😫")
                print(f"술래인 {players[tagger]} 이/가 술을 마십니다")
                return players[tagger]

    # 술래 != 플래이어
    else:
        while tryans != ans:
            for now in players*2:
                if players.index(now) == tagger:  # 술래 차례
                    continue
                elif players.index(now) == playersIndex:  # 플레이어 차례
                    temp = int(input("숫자를 맞춰보세요!(1~50) : "))
                    tryans = grading(tagger, temp, ans, now, players)
                    if tryans == -1:  # 플레이어가 정답 맞춘 경우
                        break
                else:  # 다른 사람들 차례
                    temp = tryans
                    tryans = grading(tagger, temp, ans, now, players)
                    if tryans == -1:
                        break
            if tryans != -1:
                print("이런... 2바퀴동안 아무도 못맞췄어요ㅠㅠ")
                print("이게임 누가했어!😫😫  이게임 누가했어!😫😫 ")
                print(f"술래인 {players[tagger]} 이/가 술을 마십니다")
                return players[tagger]
                players[tagger][1] -= 1
                break
            else:  # 차례가 끝나기 전에 맞춤
                drinking = correct(now, players, playersIndex)
                return drinking
