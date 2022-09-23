while True:
    price = int(input("Enter Price Of Item:"))
    if price < 0:
        break
    print(f'You Entered {price} Amount')

    x = [1,2,3,4,-3,5,6,7,87,89]
    for i in x:
        if i < 0:
            break
        print(i)