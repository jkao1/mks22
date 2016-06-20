def countChars(s,c):
    cnt = 0
    for char in s:
        if char == c:
            cnt += 1

    return cnt

def howManyOfAinB(alphabet,s):
    cnt = 0
    for char in alphabet:
         if char in s:
                cnt += 1
    return cnt

def countStrings(s,substring):
    cnt = 0
    pos = -1  
    for c in s:
        pos += 1
        if c == substring[0]:
            if substring in s[pos:pos + len(substring)]:
                cnt += 1
    return cnt
