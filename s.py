
import string


def task1():
    text = input("Введите предложение: ").lower()
    words = []
    current_word = ""

    for char in text:
        if char.isalnum():
            current_word += char
        elif current_word:
            words.append(current_word)
            current_word = ""

    if current_word:
        words.append(current_word)

    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    if frequency:
        for word, count in frequency.items():
            print(f"{word} — {count}")
    else:
        print("Слова не найдены.")


def task2():
    text = input("Введите строку: ")
    frequency = {}

    for char in text:
        if not char.isspace():
            frequency[char] = frequency.get(char, 0) + 1

    if not frequency:
        print("Нет символов для подсчёта.")
        return

    best_char = max(frequency, key=frequency.get)
    print(f"{best_char} — {frequency[best_char]}")


def task3():
    text = " ".join(input("Введите предложение: ").split())
    text = text.lower().capitalize()

    if text and text[-1] not in ".!?":
        text += "."

    print(text)


def task4():
    words = input("Введите предложение: ").split()
    result = []

    for word in words:
        if not result or word.lower() != result[-1].lower():
            result.append(word)

    print(" ".join(result))


def task5():
    email = input("Введите email: ")

    if email.count("@") != 1:
        print("Некорректный адрес")
        return

    username, domain = email.split("@")

    if (username and domain and "." in domain
            and domain.index(".") > 0
            and domain[-1] != "."):
        print("Корректный адрес")
    else:
        print("Некорректный адрес")


def task6():
    text = input("Введите строку из латинских букв: ")
    shift = int(input("Введите сдвиг: "))
    result = ""

    for char in text:
        if "A" <= char <= "Z":
            result += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        elif "a" <= char <= "z":
            result += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        else:
            result += char

    print(result)


def task7():
    text = input("Введите текст с числами: ")
    total = 0
    number = ""

    for char in text:
        if char.isdigit():
            number += char
        elif number:
            total += int(number)
            number = ""

    if number:
        total += int(number)

    print(total)


def task8():
    text = input("Введите строку: ")
    result = []
    letter_index = 0

    for char in text:
        if char.isalpha():
            if letter_index % 2 == 0:
                result.append(char.upper())
            else:
                result.append(char.lower())
            letter_index += 1
        else:
            result.append(char)

    print("".join(result))


def task9():
    first = input("Введите первую строку: ").lower()
    second = input("Введите вторую строку: ").lower()

    chars1 = sorted(char for char in first if char.isalpha())
    chars2 = sorted(char for char in second if char.isalpha())

    if chars1 == chars2:
        print("Это анаграммы")
    else:
        print("Это не анаграммы")


def task10():
    text = input("Введите номер телефона: ")
    digits = "".join(char for char in text if char.isdigit())

    if len(digits) != 11:
        print("Ошибка: номер должен содержать 11 цифр.")
        return

    if digits[0] == "8":
        digits = "7" + digits[1:]

    if digits[0] != "7":
        print("Ошибка: номер должен начинаться с 7 или 8.")
        return

    print(f"+7 ({digits[1:4]}) {digits[4:7]}-{digits[7:9]}-{digits[9:11]}")


def task11():
    words = input("Введите несколько слов: ").split()

    if not words:
        print("Нет слов.")
        return

    prefix = words[0]

    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                print("Нет общего префикса")
                return

    print(prefix)


def task12():
    text = input("Введите текст: ")

    words = len(text.split())
    letters = sum(char.isalpha() for char in text)
    digits = sum(char.isdigit() for char in text)

    punctuation = set(string.punctuation + "—–«»…„“”‘’")
    punctuation_count = sum(char in punctuation for char in text)

    print(f"Слов: {words}; букв: {letters}; "
          f"цифр: {digits}; знаков препинания: {punctuation_count}")


def main():
    tasks = {
        "1": task1,
        "2": task2,
        "3": task3,
        "4": task4,
        "5": task5,
        "6": task6,
        "7": task7,
        "8": task8,
        "9": task9,
        "10": task10,
        "11": task11,
        "12": task12
    }

    while True:
        print("\n=== Задания по строкам в Python ===")
        print("1. Частота слов")
        print("2. Самый частый символ")
        print("3. Нормализация предложения")
        print("4. Удаление соседних повторов")
        print("5. Проверка email")
        print("6. Шифр Цезаря")
        print("7. Сумма чисел в тексте")
        print("8. Чередование регистра")
        print("9. Проверка анаграмм")
        print("10. Форматирование телефона")
        print("11. Общий префикс")
        print("12. Статистика текста")
        print("0. Выход")

        choice = input("Выберите задание: ")

        if choice == "0":
            print("Программа завершена.")
            break

        if choice in tasks:
            tasks[choice]()
        else:
            print("Нет такого задания. Выберите число от 0 до 12.")


if __name__ == "__main__":
    main()
