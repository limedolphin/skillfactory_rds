import numpy as np

def game_core(number):
    low = 0
    high = 100
    count = 0
    while low <= high:
        count+=1
        predict = (low+high) // 2
        if number < predict:
            high = predict - 1
        elif number > predict:
            low = predict + 1
        else:
            break
    return(count)

def score_game(game_core):
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
score_game(game_core)