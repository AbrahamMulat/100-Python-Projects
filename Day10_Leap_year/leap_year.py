def is_leap(year):
    leap = False
    
    # Write your logic here
    if year<1900 and year>(10**5):
        print("year value out of expected range!!")
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leap = True
            else:
                leap=False
        else:
            leap = True
    else:
        leap = False
                
       
    return leap


year = int(input())
is_leap(year)
