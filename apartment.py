def apartment(player, list):
    import random
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