nums = 371
num = nums
ans = 0

while num > 0:
    digit = num % 10
    num //= 10
    ans += digit ** 3

if ans == nums:
    print(f"{nums} is an Armstrong number.")
else:
    print(f"{nums} is not an Armstrong number.")

    