import math
f = open("input", "r")
lines = f.read().split(' ')
nums = list(map(int, lines))

def _min(a):
    m=min(a)
    return m

def _max(a):
    m=max(a)
    return m

def _sum(a):
    m=sum(a)
    return m

def _mult(a):
    m=math.prod(a)
    return m

print ("В файле: ", *nums, sep=" ")
print ("Минимальное: ", _min(nums))
print ("Максимальное: ",_max(nums))
print ("Сумма: ",_sum(nums))
print ("Произведение: ",_mult(nums))
