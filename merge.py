list = [8, 4, 7, 3, 9, 2, 1, 5]

"""
mid = len(list)//2
left_array = list[0:mid]
print(left_array)
right_array = list[mid:len(list)]
print(right_array)
"""

def merge(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_array = arr[:mid]
        right_array = arr[mid:]

        merge(left_array)
        merge(right_array)
        #print(left_array)
        #print(right_array)
        x = 0 #Index of left array
        y = 0 #Index of right array
        z = 0 #Index of arr

        while x < len(left_array) and y < len(right_array):
            if left_array[x] < right_array[y]:
                arr[z] = left_array[x]
                x += 1

            else:
                arr[z] = right_array[y]
                y += 1

            z += 1
        #Check for any remaining elements in the left half.
        while x < len(left_array):
            arr[z] = left_array[x]
            x += 1
            z += 1

        #Check for any remaining elements in the right half.
        while y < len(right_array):
            arr[z] = right_array[y]
            y += 1
            z += 1

merge(list)
print(list)