import random
import string

def generate_password(length=12, strong=True):
    """
    Генератор паролей
    strong=True  -> гарантирует буквы, цифры и спецсимволы
    strong=False -> просто случайные символы
    """
    if not strong:
        # Простой режим
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))
    else:
        # Надёжный режим
        one_letter = random.choice(string.ascii_letters)
        one_digit = random.choice(string.digits)
        one_punct = random.choice(string.punctuation)
        
        all_chars = string.ascii_letters + string.digits + string.punctuation
        rest = ''.join(random.choice(all_chars) for _ in range(length - 3))
        
        password_list = list(one_letter + one_digit + one_punct + rest)
        random.shuffle(password_list)
        return ''.join(password_list)

# Красивый интерфейс
print("🔐 ГЕНЕРАТОР ПАРОЛЕЙ 🔐")
print("-" * 30)

length = input("Длина пароля (рекомендуется 12-16): ")
if length == "":
    length = 12
    print("✅ Использую длину 12")
else:
    length = int(length)

# -----------------------------------------------------

print("\nВыберите режим:")
print("1 - Простой (просто случайные буквы+цифры)")
print("2 - Надёжный (гарантированно буква+цифра+символ)")
mode = input("Ваш выбор (1 или 2): ")

strong_mode = (mode == "2")

print("\n🎲 Генерирую варианты...\n")

for i in range(5):
    password = generate_password(length, strong_mode)
    # Добавим оценку надёжности
    strength = "🔴 Слабый"
    if len(password) >= 12:
        if any(c in string.punctuation for c in password):
            if any(c in string.digits for c in password):
                strength = "🟢 Очень надёжный"
            else:
                strength = "🟡 Средний"
    
    print(f"{i+1}. {password}  {strength}")
