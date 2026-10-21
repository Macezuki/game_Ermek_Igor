import random

words = ["пайтон", "программа", "компьютер", "клавиатура", "алгоритм",
         "переменная", "функция", "виселица", "интернет", "разработчик"]

stages = [
    """
      -----
      |   |
          |
          |
          |
          |
    =========""",
    """
      -----
      |   |
      O   |
          |
          |
          |
    =========""",
    """
      -----
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """
      -----
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """
      -----
      |   |
      O   |
     /|\\  |
          |
          |
    =========""",
    """
      -----
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========""",
    """
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========""",
]

max_mistakes = len(stages) - 1
play_again = "д"

while play_again == "д":
    word = random.choice(words)
    guessed = set()
    mistakes = 0

    print("\n=== ВИСЕЛИЦА ===")

    while True:
        print(stages[mistakes])
        display = " ".join(ch if ch in guessed else "_" for ch in word)
        print("\nСлово:", display)
        print("Ошибок:", mistakes, "из", max_mistakes)
        if guessed:
            print("Названные буквы:", ", ".join(sorted(guessed)))

        if all(ch in guessed for ch in word):
            print("\nПоздравляю, вы победили! Слово:", word)
            break

        if mistakes >= max_mistakes:
            print("\nВы проиграли. Загаданное слово:", word)
            break

        letter = input("\nВведите букву: ")

        if len(letter) != 1 or not letter.isalpha():
            print("Нужно ввести ровно одну букву.")
        elif letter in guessed:
            print("Вы уже называли эту букву.")
        else:
            guessed.add(letter)
            if letter in word:
                print("Есть такая буква!")
            else:
                mistakes += 1
                print("Такой буквы нет.")

    play_again = input("\nСыграть ещё раз? (д/н): ")

print("Спасибо за игру")
