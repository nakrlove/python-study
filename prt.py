
def msg(prt):
    print("######################")
    print(prt)
    print("######################")
    
def total(num):
    total = 0 
    for i in range(1, num+1):
        if i % 3 == 0 or i % 5 == 0: 
            total += i
    
    return total    

def add(a: int, b: int) -> int: 
    return a+b



# ld = lambda x: x * x
# def lamdFun(lamd : ld , int a ) -> lambda
#     return lamd

if __name__ == "__main__":
   print(f"{__name__} , main OK")
elif __name__ != "__main__":
   print(f"{__name__} , main이 ------ 아닙니다.")
   
   
   
   