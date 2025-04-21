import random
import string

def generate_password(length=12):
    """Генерирует случайный пароль."""
    characters = string.ascii_letters + string.digits + "!@#$%^&*№"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_to_file(password):
    """Сохраняет пароль в файл."""
    with open("password.txt","a") as file:
        file.write(f"Пароль: {password}\n")

def main():
    print("🔐 Генератор паролей")
    length = int(input("Введите длину пароля: "))
    password = generate_password(length)
    print(f"Ваш пароль: {password}")
    save_to_file(password)
    print("Пароль сохранен в password.txt")

if __name__ == "__main__":
    main()