def revers(number,plan_num=0):
    if number>10:
       return revers((number//10),(plan_num+(number%10))*10)
    return plan_num+(number%10)

def is_palndrom(num):
    if num==revers(num):
        return True 
    return False 
print(is_palndrom(53335))
