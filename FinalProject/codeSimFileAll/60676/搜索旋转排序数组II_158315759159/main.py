def find_rotate_index(arr):
    left = 0
    right = len(arr) - 1
    if arr[left] < arr[right]:
        return 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            return mid + 1
        else:
            if arr[left] <= arr[mid]:
                left = mid + 1
            else:
                right = mid - 1


def find_target_index(arr, num):
    if len(arr) == 0:
        return False
    if len(arr) == 1:
        return True if arr[0] == num else False
    left = 0
    right = len(arr) - 1
    r_i = find_rotate_index(arr)
    if arr[r_i] == num:
        return True
    if r_i != 0:
        if num > arr[-1]:
            right = r_i - 1
        else:
            left = r_i
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return True
        elif num < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False


if __name__ == '__main__':
    array = eval(input())
    print(find_target_index(array, int(input())))