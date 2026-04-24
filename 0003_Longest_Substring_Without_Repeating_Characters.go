/*
Дана строка s. Найдите длину самой длинной строки без повторяющихся символов.
*/

func lengthOfLongestSubstring(s string) int {
    last := [128]int{}
    for i := range last {
		last[i] = -1 // -1 = символ не встречался
        }
        left, maxLen := 0, 0

for right, char := range s {
code := int(char)
if last[code] >= left { // символ уже в текущем окне
left = last[code] + 1 // сдвигаем левую границу
}
last[code] = right // обновляем последнюю позицию
if right-left+1 > maxLen {
maxLen = right - left + 1
}
}
return maxLen
}