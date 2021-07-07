#Elijah Jedkins PSID: 1786452
# Created a selection_sort_descend_trace() function that sorts the numbers list into descending order
def selection_sort_descend_trace(nums):
        for i in range(len(nums) - 1):
            des = i
            for j in range(i + 1, len(nums)):
                if (nums[j] > nums[des]):
                    # If the j value is greater than the des value, des will become equal to j
                    des = j
            nums[i], nums[des] = nums[des], nums[i]
            for x in nums:
                print(x, end=' ')
            print()
        return nums

if __name__ == "__main__":
        # Reads the list of integers into numbers, then call selection_sort_descend_trace() to sort the numbers
        numbers = [int(x) for x in input().split()]
        selection_sort_descend_trace(numbers)
