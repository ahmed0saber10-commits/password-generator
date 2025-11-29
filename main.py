#!/usr/bin/env python3
import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    print("مرحبا بك في Password Generator!")
    try:
        n = int(input("كم عدد الباسوردات اللي عايز تولد؟ "))
        length = int(input("كم طول الباسورد؟ "))
    except ValueError:
        print("ادخل أرقام صحيحة.")
        return
    
    print("\nالباسوردات المولدة:")
    for i in range(n):
        print(f"{i+1}: {generate_password(length)}")

if __name__ == "__main__":
    main()
