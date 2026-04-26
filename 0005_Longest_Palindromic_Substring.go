package leetcode

func longestPalindrome(s string) string {
	if len(s) <= 1 {
		return s
	}

	// Самое быстрое преобразование строки
	t := make([]byte, len(s)*2+3)
	t[0] = '^'
	t[1] = '#'
	j := 2
	for i := 0; i < len(s); i++ {
		t[j] = s[i]
		t[j+1] = '#'
		j += 2
	}
	t[j] = '$'
	t = t[:j+1]

	n := len(t)
	p := make([]int, n)
	center, right := 0, 0
	maxLen, centerIdx := 0, 0

	for i := 1; i < n-1; i++ {
		mirror := 2*center - i
		if i < right {
			p[i] = min(right-i, p[mirror])
		}

		// Расширение
		for i+p[i]+1 < n && t[i+p[i]+1] == t[i-p[i]-1] {
			p[i]++
		}

		if i+p[i] > right {
			center = i
			right = i + p[i]
		}

		if p[i] > maxLen {
			maxLen = p[i]
			centerIdx = i
		}
	}

	start := (centerIdx - maxLen) / 2
	return s[start : start+maxLen]
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
