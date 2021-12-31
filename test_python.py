import math
import os
import random
import re
import sys

def findValidDiscountCoupons(discounts):
    # Write your code here    
    # initialize result list
    result = []
    
    # for each discount in the discount list
    for discount in discounts:
        # initialize a stack ds
        stack = []
        discount_length = len(discounts)
        
        # for each character in the discount string
        for char in discount:
            # remove the character from the stack if it is the latest in the stack else add the character to the stack
            if len(stack) != 0 and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)  
        # the discount is valid only if there are no more item left in the stack
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)
    return result
    
def isValid(discount_coupon):
    print('input: ',discount_coupon)
    if (len(discount_coupon) == 0):
        print('length = 0')
        return 1
    else:
        if (len(discount_coupon) == 1):
            print('length = 1')
            return 0
        else:
            if (discount_coupon[0] == discount_coupon[len(discount_coupon)-1]):
                return isValid(discount_coupon[1:len(discount_coupon)-1])
            else:
                for i in range (2, len(discount_coupon)-1):
                    isValidResult = isValid(discount_coupon[0:i])
                    isValidResult = isValidResult * isValid(discount_coupon[i:])
                    print('isValidResult = ',isValidResult)
                    if (isValidResult == 1):
                        return 1
        return 0

discount_coupons = ['aabb', 'aabcbbccdeffedcbaa']
discount_coupon = 'abnncddcbaaxxa'

# print(findValidDiscountCoupons(discount_coupons))
print('=== START ====')
result = isValid(discount_coupon)
print('result : ',result)

