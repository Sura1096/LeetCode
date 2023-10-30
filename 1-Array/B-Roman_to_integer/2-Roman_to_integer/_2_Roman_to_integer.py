#num = 'MCMXCIV'  # M = 1000, CM = 900, XC = 90 and IV = 4
#rom = 'LVIII'  # L = 50, V= 5, III = 3

#def roman_to_integer(roman_digits):
    #dct = {}
    #for char in roman_digits:
    #    dct[char] = dct.get(char, 0) + 1


    #if dct['I'] > 3:
    #    return 'Too much "I"'
    #elif dct['X'] > 3:
    #    return 'Too much "X"'
    #elif dct['C'] > 3:
    #    return 'Too much "C"'
    #elif dct['M'] > 3:
    #    return 'Too much "M"'

    #elif dct['V'] > 1:
    #    return 'Too much "V"'
    #elif dct['L'] > 1:
    #    return 'Too much "L"'
    #elif dct['D'] > 1:
    #    return 'Too much "D"'

    #number = 0
    #ind = 0
    #I, V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000
    
    #for char in roman_digits:
    #    if char == 'V' and roman_digits[ind+1] == 'I':
    #        number += V + I

    #    elif char == 'I' and roman_digits[ind+1] == 'V':
    #        number += V - I

    #    elif char == 'I' and roman_digits[ind+1] == 'X':
    #        number += X - I

    #    elif char == 'X' and roman_digits[ind+1] == 'I':
    #        number += X + I

    #    elif char == 'X' and roman_digits[ind+1] == 'C':
    #        number += C - X

    #    elif char == 'C' and roman_digits[ind+1] == 'X':
    #        number += C + X

    #    ind += 1

    #return number
    

roman_digits = 'LXXVI'  
#print(roman_to_integer(roman_digits))


number = []
ind = 1
for char in roman_digits:
    if char == 'I' and roman_digits.count('I') <= 3:
        if ind <= len(roman_digits)-1:
            if roman_digits[ind] == 'V':
                number.append(5)
                number.append(-1)
            elif roman_digits[ind] == 'X':
                number.append(10)
                number.append(-1)
            else:
                number.append(1)

    elif char == 'V' and roman_digits.count('V') == 1:
        if ind <= len(roman_digits)-1:
            if roman_digits[ind] == 'I':
                number.append(5)
                number.append(1)
            elif roman_digits[ind-2] != 'I':
                number.append(5)
            else:
                number.append(5)

    elif char == 'X' and roman_digits.count('X') <= 3:
        if ind <= len(roman_digits)-1:
            if roman_digits[ind] == 'L':
                number.append(50)
                number.append(-10)
            elif roman_digits[ind] == 'C':
                number.append(100)
                number.append(-10)
            elif roman_digits[ind] == 'V':
                number.append(10)
                number.append(5)
            elif roman_digits[ind-2] == 'L':
                continue
            else:
                number.append(10)

    elif char == 'L' and roman_digits.count('L') == 1: 
        if ind <= len(roman_digits)-1:
            if roman_digits[ind] == 'X':
                number.append(50)
                number.append(10)
            else:
                number.append(50)

    elif char == 'C' and roman_digits.count('C') <= 3:
        if ind <= len(roman_digits)-1:
            if roman_digits[ind] == 'D':
                number.append(500)
                number.append(-100)
            elif roman_digits[ind] == 'M':
                number.append(1000)
                number.append(-100)
            elif roman_digits[ind] == 'L':
                number.append(100)
                number.append(50)
            elif roman_digits[ind-2] != 'X':
               number.append(100)
            else:
                number.append(100)


    elif char == 'D' and roman_digits.count('D') == 1:
        if ind <= len(roman_digits)-1:
            if roman_digits[ind] == 'C':
                number.append(500)
                number.append(100)
            else:
                number.append(500)

    elif char == 'M' and roman_digits.count('M') <= 3:
        if ind <= len(roman_digits)-1:
            if roman_digits[ind] == 'D':
                number.append(1000)
                number.append(500)
            elif roman_digits[ind] == 'C':
                number.append(1000)
                number.append(100)
            elif roman_digits[ind] == 'L':
                number.append(1000)
                number.append(50)
            elif roman_digits[ind] == 'X':
                number.append(1000)
                number.append(10)
            elif roman_digits[ind] == 'I':
                number.append(1000)
                number.append(1)
            elif roman_digits[ind-2] != 'C':
                number.append(1000)

    ind += 1

if len(number) != len(roman_digits):
    print(f'Number "{roman_digits}" does not exist')
else:
    print(sum(number))