for i in range(int(input())):
    n = [m for m in [*map(input().lower().count, "aeiou")]]
    print("Number of vowels = {}".format(sum(n)))