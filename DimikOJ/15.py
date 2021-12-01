T = int(input())
for i in range(T):
    sentence  = input().strip()
    article = sorted(list(set(sentence)))
    for letter in article:
        print('{} = {}'.format(letter,sentence.count(letter)))
    if i<T-1:
        print()