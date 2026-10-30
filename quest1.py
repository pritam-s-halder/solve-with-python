#FizzBuzz, your way. Write fizzbuzz(n) that returns a list for 1 to n:
#"Fizz" for multiples of 3,
#"Buzz" for multiples of 5,
#"FizzBuzz" for both, otherwise the number.

def fizz(num, nums):
    for num in nums:
        if num % 3 == 0:
            print(num)
        else:
            print(num)

def buzz(num, nums):
    for num in nums:
        if num % 5 == 0:
            print(num)
        else:
            print(num)

def fizzbuzz(num, nums):
    for num in nums:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        else:
            print(num)
