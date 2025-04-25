import random

def guess_the_number():
    # Загадываем случайное число от 1 до 100
    secret_number = random.randint(1, 100)
    attempts = 0  # Счётчик попыток
    
    print("🎮 Игра 'Угадай число от 1 до 100'!")
    
    while True:
        # Запрашиваем ввод пользователя
        guess = input("Введите вашу догадку: ")
        
        try:
            guess = int(guess)  # Преобразуем ввод в число
        except ValueError:
            print("🚫 Ошибка! Введите целое число.")
            continue
        
        attempts += 1  # Увеличиваем счётчик попыток
        
        # Проверяем догадку
        if guess < secret_number:
            print(f"⬆️ Загаданное число БОЛЬШЕ {guess}!")
        elif guess > secret_number:
            print(f"⬇️ Загаданное число МЕНЬШЕ {guess}!")
        else:
            print(f"🎉 Поздравляем! Вы угадали число {secret_number} за {attempts} попыток!")
            break

if __name__ == "__main__":
    guess_the_number()