#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Написать программу, которая считывает текст из файла, находит самое
# длинное слово и определяет, сколько раз оно встретилось в тексте.


if __name__ == "__main__":

    with open("file.txt") as f:

        words = f.read().split()
        max_word = str(max(words, key=len))
        count_of_max_word = words.count(max_word)
        print(f"Max word: {max_word}, Count of max word: {count_of_max_word}")
