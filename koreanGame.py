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
    print('πνλ―Όμ ~μ νλ―Όμ ~μ!πΆ  ')
    if current_pl==myself:
        korean = input('λ μλ¦¬ μ΄μ±μ μλ ₯ν΄μ£ΌμΈμ ex) γ±γ΄ : ')
    else:
        korean_list = ['γ±','γ΄','γ·','γΉ','γ','γ','γ','γ','γ','γ','γ','γ','γ','γ']
        korean = random.choice(korean_list)+random.choice(korean_list)
    print(f'μ΄μ±μ {korean} !')

    # μ€ν¬λνμΌλ‘ μ΄μ± μ¬μ΄νΈμμ λ¨μ΄λ₯Ό κ°μ Έμ¨λ€
    word_list = []
    my_list = list(pl_re)
    for page in range(1, 3):
        url = f"https://wordrow.kr/%EC%B4%88%EC%84%B1/{korean}/?%EC%AA%BD={page}"
        res = requests.get(url)
        soup = bs(res.text, "html.parser")
        word_list += [word.get_text() for word in soup.select("body > div.content > section > div.larger > ul > li > a > b")[0:20]]
    random.shuffle(word_list)
    random.shuffle(my_list)

    print(f'{current_pl} : {word_list[0]} ! π')
    my_list.remove(current_pl)
    del word_list[0]

    for player in range(0,len(my_list)-1):
        print(f'{my_list[player]} : {word_list[player]} ! π')

    drink = my_list[len(my_list)-1]
    print(f'{drink} : λμ²΄ κ·Έλ° λ¨μ΄λ€μ μ΄λ»κ² μλκ±°μΌ..? π­')

    print(f'λκ° λ§μ λ€~? {drink}(μ΄)κ° λ§μ λ€! \n{drink[0]}! μ§πμ§πμ§πμ§π! \n{drink[1]}! μ§πμ§πμ§πμ§π! \nμμ΄μ΄μΈ μ·!')

    return drink