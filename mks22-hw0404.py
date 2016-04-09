# Problem 5:
def replaceAll(astring,lookfor,replaceWith):
    pos = -1  
    for c in astring:
        pos += 1
        if lookfor == astring[pos:pos + len(lookfor)]:
             astring = astring[:pos] + replaceWith + astring[pos+len(lookfor):]
    return astring
# Test results:
# 1. Pass
# 2. Does not pass.
# 3. Pass

# Problem 6:
def is_prime(n):
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3,int(n**0.5) + 1,2):
        if n % i == 0:
            return False
    return True

def primesUnder(n):
    if n <= 2:
        return "There are no primes less than " + str(n) + "."
    primes = []
    for i in range(2,n):
        if is_prime(i):
            primes.append(i)
    if len(primes) == 1:
        return "The prime less than " + str(n) + " is 2."
    pt1 = "The primes less than " + str(n) + " are " 
    pt2 = ''
    for elem in primes:
        if elem == primes[-1]:
            pt2 += str(elem) + '.'
            continue
        pt2 += str(elem) + ' and ' 
    return pt1 + pt2
# Test results:
# 1. Pass
# 2. Pass
# 3. Pass
# 4. Pass

# Problem 7:
def countWords(s):
    return len(s.split())
# Test results:
# 1. Pass
# 2. Pass
# 3. Pass
# 4. Pass
# 5. Pass
