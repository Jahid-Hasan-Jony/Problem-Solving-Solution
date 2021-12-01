while True:
    try:
        g=int(input())
        if g>0:
            print("vai ter duas!")
        if g==0:
            print("vai ter copa!")
    except EOFError:
        break