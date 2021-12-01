for i in range(int(input())):
    words = input()
    letter = input()
    n = words.count(letter)
    if n>0:
        print("Occurrence of '{}' in '{}' = {}".format(letter,words,n))
    else:
        print("'{}' is not present".format(letter))