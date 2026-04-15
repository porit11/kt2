import random
import os

def load_words(filename="words.txt"):
    words = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    word = parts[0].upper()
                    hint = parts[1] if len(parts) > 1 else "Без описания"
                    words.append((word, hint))
    except FileNotFoundError:
        print("Файл words.txt не найден!")
        exit()
    return words

def load_gallows_stage(step):
    try:
        with open(f"gallows_{step}.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"[Ошибка: файл gallows_{step}.txt не найден]"

def display_galloon(step):
    print(load_gallows_stage(step))

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print(display.strip())

def play_game():
    words = load_words()
    if not words:
        print("Нет слов для игры!")
        return
    
    word, hint = random.choice(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 7
    guessed_word = False
    
    print("\n=== ВИСЕЛИЦА НА ПОЛЕ ЧУДЕС ===\n")
    print(f"Подсказка: {hint}\n")
    
    while incorrect_guesses < max_incorrect and not guessed_word:
        display_galloon(incorrect_guesses + 1)
        print("\nСлово:")
        display_word(word, guessed_letters)
        print(f"\nОшибок: {incorrect_guesses}/{max_incorrect}")
        print(f"Угаданные буквы: {', '.join(sorted(guessed_letters)) if guessed_letters else 'пока нет'}")
        
        guess = input("\nНазовите букву или слово целиком: ").upper().strip()
        
        if not guess:
            continue
        
        if len(guess) > 1:
            if guess == word:
                guessed_word = True
                break
            else:
                print("❌ Неправильно!")
                incorrect_guesses += 1
                continue
        
        if guess in guessed_letters:
            print("Вы уже называли эту букву!")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("✅ Верно!")
            if all(letter in guessed_letters for letter in word):
                guessed_word = True
        else:
            print("❌ Нет такой буквы!")
            incorrect_guesses += 1
    
    display_galloon(incorrect_guesses + 1 if not guessed_word else max_incorrect)
    print("\nСлово:", " ".join(word))
    
    if guessed_word:
        print("\n🎉 ПОЗДРАВЛЯЮ! Вы спасли человечка! 🎉")
    else:
        print("\n💀 Игра окончена. Виселица построена. 💀")
    
    print(f"\nЗагаданное слово: {word} - {hint}")

if __name__ == "__main__":
    play_game()
