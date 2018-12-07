def div(divident,divisor=2):
    
    qoutient =divident/divisor
    remainder = divident%divisor
    result = (qoutient,remainder)
    
    print"qoutient=",qoutient," remainder=",remainder
    
    

def div1(*n):
    divident=n[0]
    divisor=n[1]
    qoutient =divident/divisor
    remainder = divident%divisor
    result = (qoutient,remainder)
    
    print"qoutient=",qoutient,"remainder=",remainder
    
    


