import requests
import random
from bs4 import BeautifulSoup as bs

def koreanGame(current_pl, pl_re, myself):

    print('''
    ---------------------------------------------------------------------------
    _   __                                   _____                         
    | | / /                                  |  __ \                        
    | |/ /   ___   _ __   ___   __ _  _ __   | |  \/  __ _  _ __ ___    ___ 
    |    \  / _ \ | '__| / _ \ / _` || '_ \  | | __  / _` || '_ ` _ \  / _ 
    | |\  \| (_) || |   |  __/| (_| || | | | | |_\ \| (_| || | | | | ||  __/
    \_| \_/ \___/ |_|    \___| \__,_||_| |_|  \____/ \__,_||_| |_| |_| \___|
                                                                            
    ---------------------------------------------------------------------------
                                                                            ''')
    print('📖훈민정~음 훈민정~음!🎶  ')
    if current_pl==myself:
        korean = input('두 자리 초성을 입력해주세요 ex) ㄱㄴ : ')
    else:
        korean_list = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
        korean = random.choice[korean_list]+random.choice[korean_list]

    # 스크래핑으로 초성 사이트에서 단어를 가져온다
    word_list = []
    my_list = list(pl_re)
    for page in range(1, 3):
        url = f"https://wordrow.kr/%EC%B4%88%EC%84%B1/{korean}/?%EC%AA%BD={page}"
        res = requests.get(url)
        soup = bs(res.text, "html.parser")
        word_list += [word.get_text() for word in soup.select("body > div.content > section > div.larger > ul > li > a > b")[0:20]]
    random.shuffle(word_list)
    random.shuffle(my_list)

    print(f'{current_pl} : {word_list[0]} ! 👍')
    my_list.remove(current_pl)
    del word_list[0]

    for player in range(0,len(my_list)-1):
        print(f'{my_list[player]} : {word_list[player]} ! 👍')

    drink = my_list[len(my_list)-1]
    print(f'{drink} : 대체 그런 단어들은 어떻게 아는거야..? 😭')

    print(f'누가 마신다~? {drink}(이)가 마신다! \n{drink[0]}! 짝👏짝👏짝👏짝👏! \n{drink[1]}! 짝👏짝👏짝👏짝👏! \n워어어언 샷!')

    return drink