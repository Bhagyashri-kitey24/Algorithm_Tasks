for x in range(1,100):
    i = ""  #define i
    if x % 15 == 0: 
        i= "fizz buzz"
    if x % 3 == 0:
        i ="Fizz"
    if x%5==0:
        i+="Fizz"   
    print(x if not i else i)
    
print("-----------------------------------")    


        
    
