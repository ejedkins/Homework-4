#Elijah Jedkins PSID: 1786452
# Global variable
num_calls = 0


def partition(user_ids, l, h):
    i = (l - 1)
    par = user_ids[h]
    for j in range(l, h):
        # If current element is smaller than or equal to par
        if user_ids[j] <= par:
            i += 1
            user_ids[i], user_ids[j] = user_ids[j], user_ids[i]

    user_ids[i + 1], user_ids[h] = user_ids[h], user_ids[i + 1]
    return (i + 1)


# Write the quicksort algorithm that recursively sorts the low and high partitions. Add 1 to num_calls each time quisksort() is called
def quicksort(user_ids, l, h):
    global num_calls
    # Increment num_calls by 1
    num_calls += 1
    if len(user_ids) == 1:
        return user_ids
    elif (l < h):
        # calls partitioning funtion
        par = partition(user_ids, l, h)

        # calls quicksort function
        quicksort(user_ids, l, par - 1)
        quicksort(user_ids, par, h)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)