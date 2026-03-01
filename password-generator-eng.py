import random
import string

def generate_password(length=12, strong=True):
    """
    Password generator
    strong=True  -> Guarantees letters, numbers and special characters
    strong=False -> Random symbols
    """
    if not strong:
        # Simply mode
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))
    else:
        # Strong mode
        one_letter = random.choice(string.ascii_letters)
        one_digit = random.choice(string.digits)
        one_punct = random.choice(string.punctuation)
        
        all_chars = string.ascii_letters + string.digits + string.punctuation
        rest = ''.join(random.choice(all_chars) for _ in range(length - 3))
        
        password_list = list(one_letter + one_digit + one_punct + rest)
        random.shuffle(password_list)
        return ''.join(password_list)

# Interface
print("🔐 PASSWORD GENERATOR 🔐")
print("-" * 30)

length = input("String length (recomends 12-16): ")
if length == "":
    length = 12
    print("✅ Auto-Length 12")
else:
    length = int(length)

# -----------------------------------------------------

print("\nSelect mode:")
print("1 - Simply password (Random sybmobls (without special characters))")
print("2 - Strong password (Guarantees letters+numbers+special characters)")
mode = input("Selected (1 or 2): ")

strong_mode = (mode == "2")

print("\n🎲 Generated variabled...\n")

for i in range(5):
    password = generate_password(length, strong_mode)
    # Check strength password
    strength = "🔴 Simply Password"
    if len(password) >= 12:
        if any(c in string.punctuation for c in password):
            if any(c in string.digits for c in password):
                strength = "🟢 Very Hard Password"
            else:
                strength = "🟡 Middle Password"
    
    print(f"{i+1}. {password}  {strength}")
