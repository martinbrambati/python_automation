def median(elements):
    lenght = len(elements)
    
    if(lenght==0):
        return 0
        
    if(lenght==1):
        return elements[0]
    
    if(lenght==2):
        return (elements[0] + elements[1]) / 2.
    
    elements.sort()
    return median(elements[1:-1])