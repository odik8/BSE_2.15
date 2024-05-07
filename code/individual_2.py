#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Перед публикацией текста или документа обычно принято удалять или изменять в
# них служебную информацию. В данном упражнении вам необходимо написать
# программу, которая будет заменять все служебные слова в тексте на символы
# звездочек (по количеству символов в словах). Вы должны осуществлять
# регистрозависимый поиск служебных слов в тексте, даже если эти слова входят
# в состав других слов. Список служебных слов должен храниться в отдельном
# файле. Сохраните отредактированную версию исходного файла в новом файле.
# Имена исходного файла, файла со служебными словами и нового файла
# должны быть введены пользователем. В качестве дополнительного задания
# расширьте свою программу таким образом, чтобы она выполняла замену служебных
# слов вне зависимости от того, какой регистр символов используется в тексте.
# Например, если в списке служебных слов будет присутствовать слово exam, то
# все следующие варианты слов должны быть заменены звездочками:
# exam, Exam, ExaM и EXAM.


def replace_sensitive_words(text: str, sensitive_words: list):
    modified_text = text
    for word in sensitive_words:
        modified_text = modified_text.replace(word.lower(), "*" * len(word))
    return modified_text


def main():
    input_file_name = input("Enter filename: ")
    sensitive_words_file = input("Enter file name with sensitive_words: ")
    output_file_name = input("Enter the name for a new file: ")

    with open(input_file_name, "r") as file:
        text = file.read()

    with open(sensitive_words_file) as file:
        sensitive_words_file = file.read().splitlines()

    modified_text = replace_sensitive_words(text, sensitive_words_file)

    with open(output_file_name, "w") as file:
        file.write(modified_text)


if __name__ == "__main__":
    main()
