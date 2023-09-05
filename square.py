size = int(input())

if 1 <= size <= 100:
    print("* " * size) # prentar efsta partin i kassanum

    for _ in range(size - 2):
        print("* " + "  " * (size - 2) + "*")# prentar miðjuna i kassanum

    
    if size > 1:
        print("* " * size)#prentar botnin í kassanum
else:
    print("Input value is out of the valid range.")
