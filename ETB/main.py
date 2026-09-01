# fizzbuzz

def fizzbuzz(n, a = 3, b = 5):
    for i in range(1, n+1):
        if i % a  == 0 and i % b == 0:
            print("Fizzbuzz")
        elif i % a == 0:
            print("Fizz")
        elif i % b == 0:
            print("Buzz")
        else: 
            print(i)

fizzbuzz(20)

# find maximum in array

arr = [3,7, 2,9, 4]

max = arr[0]

for num in arr:
    if num > max:
        max = num

print(max)

# find minimum in array

min = arr[0]


# find second largest 

arr = [10,5,20,8,15]

largest = float('-inf')
second_largest = float('-inf')
for num in arr:
    if num > largest:
        second_largest = largest
        largest = num 
    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)

# reverse an array

arr = [1,2,3,4,5]

left = 0 
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)

# checking if array is sorted 

arr = [1,2,3,4,5]

is_sorted = True

for i in range(len(arr) - 1):
    if (arr[i] > arr[i+1]):
        is_sorted = False
        break
print(is_sorted )