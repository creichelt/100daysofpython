import math

def paint_calc(h,w,c):
    cans = math.ceil((h*w)/c)
    print(f"You'll need {cans} cans of paint")

test_h = int(input("How tall is your wall? "))
test_v = int(input("How wide is your wall? "))
coverage = 5

paint_calc(test_h,test_v,coverage)
