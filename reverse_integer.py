def reverse(num):

    sign_flag = 1
    if(num < 0):
        sign_flag = -1
        num = num * sign_flag
    
    result = 0

    while num > 0:
        remainder = num % 10
        num = num // 10
        result =  remainder + (result * 10)
    
    if(result > -2**31 and result < (2**31)-1):
        return result * sign_flag
    else:
        return 0

# Example 1
print(reverse(9646324351))

# Example 2
print(reverse(123))

# Example 3
print(reverse(-123))