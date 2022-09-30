
def convert(s):
    
    vowels = 'aeiou'
    if s[0].lower() in vowels:
        return s + '-way'
    if s[0] == 'q':
        return s[2:len(s)] + '-' + s[0:2] + 'ay'
    found = False
    for i in range(len(s)):
        if (s[i].lower() in vowels) and (not found):
            found = True
            index = i
    
    return s[index:] + '-' + s[0:index] + 'ay'
