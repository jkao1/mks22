def Esrever(L):
    output = []
    for string in L:
        new_string = ''
        i = len(string) 
        while i > 0: # not >= b/c i -= 1 goes before the function
            i -= 1
            new_string += string[i]
        output.append(new_string)
    return output

Esrever(['abcd','derF'])  # returns ['dcba', 'Fred']

import random

def RandTest(low,high,numTrials):
    output = []
    for i in range(high - low + 1):
        c = 0
        for i in range(numTrials):
            var = random.randint(low,high)
            if var == i:
                c += 1
        output.append(float(c)/ numTrials)
    return output

def Av(L):
    total = 0
    count = 0
    for i in L:
        if type(i) == type(0) or type(i) == type(0.):
            total += i
            count += 1
    return total/count

def SmallestPos(L):
    m = min(L)
    pos = 0
    while pos < len(L):
        if L[pos] == m:
            return pos
            break
        pos += 1

def SortNums(L):
    result = []
    a = L
    for i in range(len(L)):
        result.append(L[SmallestPos(a)])
        a.pop(SmallestPos(a))
    return result

nums = ['zero','one','two','three','four','five','six','seven','eight','nine',
        'ten','eleven','twelve','twen','thir','for','fif','six','seven','eigh',
        'nine','hundred']

def NumInWords(n):
    add = ''
    if n <= 12:
        return nums[n]
    elif n <= 19:
        if n == 14:
            return 'fourteen'
        return nums[n+1] + 'teen'
    elif n <= 99:
        if n % 10 != 0:
            add = '-' + nums[n % 10]
        return nums[int(n/10) + 11] + 'ty' + add
    else:
        if n % 100 != 0:
            add = ' and ' + f(n % 100)
        return nums[int(n/100)] + ' hundred' + add
    


    
    
