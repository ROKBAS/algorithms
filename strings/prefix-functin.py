# PREFIX FUNCTION
def prefix(s):
    v = [0]*len(s)
    for i in range(1,len(s)):
        k = v[i-1]
        while k > 0 and s[k] != s[i]:
            k = v[k-1]
        if s[k] == s[i]:
            k = k + 1
        v[i] = k
    return v
s = 'ANTAN'
v = prefix(s)
print(*v)

# Поиск подстроки в строке. 
# Алгоритм Кнута-Морриса-Пратта

t = 'LETS ANTAN GO SOMEBODY'

v = prefix(s+"#"+t)
print(*v)
    
