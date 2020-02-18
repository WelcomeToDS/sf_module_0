import numpy as np
def game_core_v2(number):
    count = 0
    _min = 1
    _max = 100
    predict = 50
    while number != predict:
        count += 1
        if number > predict:
            _min = predict + 1
        elif number < predict:
            _max = predict - 1
        predict = (_min + _max) // 2
    return(count)
def score_game(game_core):
    '''«апускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1) # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"¬аш алгоритм угадывает число в среднем за {score} попыток")
# запускаем
score_game(game_core_v2)

