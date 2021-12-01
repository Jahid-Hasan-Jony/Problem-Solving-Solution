def convert_to_roman(n):
    integers = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    roman_numerals = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(integers)):
        count = int(n / integers[i])
        result.append(roman_numerals[i] * count)
        n -= integers[i] * count
    return ''.join(result) 
num = int(input())
print(convert_to_roman(num))
   