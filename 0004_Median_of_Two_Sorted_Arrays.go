package leetcode

import "math"

/*
Даны два отсортированных массива
nums1 и nums2 размером m и n соответственно.
Необходимо вернуть медиану этих двух отсортированных массивов.
*/

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	// Всегда бинарим по меньшему массиву
	if len(nums1) > len(nums2) {
		nums1, nums2 = nums2, nums1
	}

	m, n := len(nums1), len(nums2)
	lo, hi := 0, m

	for lo <= hi {
		i := (lo + hi) / 2 // partition в nums1
		j := (m+n+1)/2 - i // partition в nums2

		maxLeft1 := math.MinInt64
		if i > 0 {
			maxLeft1 = nums1[i-1]
		}
		minRight1 := math.MaxInt64
		if i < m {
			minRight1 = nums1[i]
		}

		maxLeft2 := math.MinInt64
		if j > 0 {
			maxLeft2 = nums2[j-1]
		}
		minRight2 := math.MaxInt64
		if j < n {
			minRight2 = nums2[j]
		}

		if maxLeft1 <= minRight2 && maxLeft2 <= minRight1 {
			// Нашли правильный partition
			if (m+n)%2 == 1 {
				return float64(max(maxLeft1, maxLeft2))
			}
			return float64(max(maxLeft1, maxLeft2)+min(minRight1, minRight2)) / 2.0
		} else if maxLeft1 > minRight2 {
			hi = i - 1
		} else {
			lo = i + 1
		}
	}

	return 0.0
}
