#1a

def SFind(letter):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter in lower:
        return upper[lower.find(letter)]
    else:
        return letter
def ToUpper(s):
    new = ''
    for letter in s:
         new += SFind(letter)
    print(new)

ToUpper('Hi there, 2 you')

#1b

def Encrypt(some_text):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new = ''
    for letter in some_text:
        if letter in lower:
            new += lower[lower.find(letter)-3]
        elif letter in upper:
            new += upper[upper.find(letter)-3]
    print(new)
Encrypt('HIthisISjasonKAO defgh')

def Decrypt(some_text):
    lower = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new = ''
    for letter in some_text:
        if letter in lower:
            new += lower[lower.find(letter)+3]
        elif letter in upper:
            new += upper[upper.find(letter)+3]
    print(new)
Decrypt('EFqefpFPgxplkHXLabcde')

#2a

def IsSameName(name1,name2):
    return ToUpper(name1) == ToUpper(name2)

#2b

def CapWord(word):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new = ''
    if word[0] in lower:
        new += upper[lower.find(word[0])]
    else:
        new += upper[lower.find(word[0])]       
    for letter in word:
        if word.find(letter) == 0:
            new += ''
        elif letter in lower:
            new += lower[lower.find(letter)]
        elif letter in upper:
            new += lower[upper.find(letter)]
    return new

CapWord('jason')

#2c

def CapName(name):
    words = name.split()
    print(CapWord(words[0]) + ' ' + CapWord(words[1]))
CapName('jason kao')

#3a

def FirstLast(names):
    names = names.split(',')
    return names[1] + " " + names[0]
FirstLast('Brooks,Peter')

#3b

def FirstLastSequence(names):
    names = names.split(';')
    for i in names:
        print(FirstLast(i))

FirstLastSequence('Brooks, Peter;Holmes, David;Pascu, Ms.')

#4a

def FileClassifier(filename):
    filename = filename.split('.')
    i = filename[-1]
    if i == 'jpg' or i =='jpeg':
        print('picture')
    elif i == 'mp3':
        print('music')
    elif i == 'nlogo':
        print('Netlogo')
    elif i == 'py':
        print('Python')

#Triple Challenge Problem

def Encrypt2(some_text,n):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new = ''
    for letter in some_text:
        if letter in lower:
            new += lower[lower.find(letter)-n]
        elif letter in upper:
            new += upper[upper.find(letter)-n]
        else:
            new += letter
    teams = ['Nets','Knicks','Jets','Giants','Mets','Yankees','Nets.','Knicks.','Giants.']
    for thing in new.split():
        if thing in teams:
            print(new)
            
def caesar_cipher(msg):
    for key in range(26):
        Encrypt2(msg,key)

caesar_cipher("Zw Z yrmv jvve wlikyvi zk zj sp jkreuzex fe kyv jyfcuvij fw Xzrekj.")


































        

