class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # Manacher's Algorithm — O(n)
        t = "^#" + "#".join(s) + "#$"
        n = len(t)
        p = [0] * n
        center = right = 0
        max_len = 0
        center_idx = 0

        for i in range(1, n - 1):
            mirror = 2 * center - i
            if i < right:
                p[i] = min(right - i, p[mirror])

            # Расширение
            while t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1

            # Обновление центра
            if i + p[i] > right:
                center, right = i, i + p[i]

            # Лучший палиндром
            if p[i] > max_len:
                max_len = p[i]
                center_idx = i

        start = (center_idx - max_len) // 2
        return s[start : start + max_len]
