def find_even_index(arr):
    left_sum = right_sum = idx = 0
    for idx in range(len(arr)):
      left_sum = sum(arr[:idx])
      right_sum = sum(arr[idx+1:])
      if left_sum == right_sum:
          return idx
    return -1


print(find_even_index([1,100,50,-51,1]))