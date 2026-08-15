# data.py
import random
import string

def generate_login():
    """Генерирует случайный email (логин)."""
    prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(['ya.ru', 'mail.ru', 'gmail.com', 'example.com'])
    return f"{prefix}@{domain}"

def generate_password(length=8):
    """Генерирует случайный пароль заданной длины (по умолчанию 8)."""
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choices(characters, k=length))

def generate_short_password():
    """Генерирует пароль длиной менее 6 символов (для проверки ошибки)."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))