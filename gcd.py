def gcd(a,b):
    if(a==1 or b==1):
        return 1
    else:
        a=a%b
        # print()
        if(b%a==0):
            global c
            c=a
            return c
        else:
            # print(a,b)
            a,b=b,a
            gcd(a,b)
c=1
gcd(48,18)
print(c)









# import math
#
# a=math.gcd(14,21)
# print(a)