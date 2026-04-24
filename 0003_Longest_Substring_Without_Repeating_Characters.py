'''
Дана строка s. Найдите длину самой длинной строки без повторяющихся символов.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = [-1] * 128  # last[i] = последний индекс символа с ASCII-кодом i, -1 = не встречался
        left = 0           # левая граница окна
        max_len = 0

        for right, char in enumerate(s):
            code = ord(char)  # ASCII-код текущего символа
            if last[code] >= left:  # символ уже есть в текущем окне
                left = last[code] + 1  # сдвигаем левую границу за его прошлую позицию
            last[code] = right  # обновляем последнюю позицию символа
            if right - left + 1 > max_len:  # размер текущего окна
                max_len = right - left + 1

        return max_len