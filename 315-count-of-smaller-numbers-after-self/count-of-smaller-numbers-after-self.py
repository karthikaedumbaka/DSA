class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        indexed_nums = list(enumerate(nums))  # Store (original_index, value)

        def merge_sort(start, end):
            if end - start <= 1:
                return indexed_nums[start:end]
            
            mid = (start + end) // 2
            left = merge_sort(start, mid)
            right = merge_sort(mid, end)
            
            merged = []
            i = j = 0
            right_count = 0

            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    # Count how many smaller elements have been passed in 'right'
                    result[left[i][0]] += right_count
                    merged.append(left[i])
                    i += 1
                else:
                    # Right has a smaller element
                    right_count += 1
                    merged.append(right[j])
                    j += 1

            # Append remaining left items and count right_count for them
            while i < len(left):
                result[left[i][0]] += right_count
                merged.append(left[i])
                i += 1

            # Append remaining right items
            while j < len(right):
                merged.append(right[j])
                j += 1

            # Very important: update the portion of indexed_nums being merged
            indexed_nums[start:end] = merged
            return merged

        merge_sort(0, n)
        return result