def para_rect(len,wid):
    return 2*(len+wid)

def area_circle(r):
    return 2*(3.14*r*r)

def unique_list(numbers):
    unique = []

    for num in numbers:
        if num not in unique:
            unique.append(num)

    return unique



if __name__=="__main__":

    print("testing",para_rect(2,3))