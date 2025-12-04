s = "bonjour monde"
temp = ""
res = ""

# inverse la chaine : bonjour monde ruojnob ednom
for i in range(len(s)):
    if s[i] == " ":
        res += temp + " "
        temp = ""
    else:
        temp = s[i] + temp
res += temp
print(res)

# RLE

s = "aaabbbbbbbbcccccccccaadddeeeeeee"
cpt = 0
caractere_actuel = s[0]
res = ""
for c in s:
    if c == caractere_actuel:
        cpt += 1
    else:
        res += str(cpt) + caractere_actuel
        caractere_actuel = c
        cpt = 1
res += str(cpt) + caractere_actuel

print(res)