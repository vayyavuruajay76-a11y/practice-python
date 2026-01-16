def steps(number):
    if number>0:
        nostep=0
        stopnum=number
        while stopnum!=1:
            if  stopnum%2==0:
                stopnum=stopnum/2
            else:
                stopnum=(stopnum*3)+1

            nostep+=1
        
        return nostep   
    else:
        raise ValueError("Only positive integers are allowed")
