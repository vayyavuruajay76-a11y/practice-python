def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if  number>0:
        fact=[]
        for i in range(1,number+1):
            if number%i==0:
                fact.append(i)

        s=sum(fact[:-1])
        if s==number:
            return "perfect"
        elif number<s:
            return "abundant"
        elif number>s:
            return "deficient"
    else:
        raise ValueError("Classification is only possible for positive integers.")
        
    
    
        
        
    

    
       
    
    
