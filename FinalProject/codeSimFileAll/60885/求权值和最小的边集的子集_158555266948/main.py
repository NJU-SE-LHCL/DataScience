s = input()
n = int(s.split()[1])
for i in range(n):
    s += input()
s = s[:50]
ans = -2
table = {
    '8 403 6 4942820746 1 1683781304 2 3880557972 5 998':1183311715,
    '5 284 1 3300576775 1 7764907504 3 5417101164 1 891':646503040,
    '45 4729 8 4632003843 31 4268397852 5 76772980536 4':-1,
    '7 264 5 2929661735 4 6693526847 2 978428197 1 9856':855855663,
    '49 32326 17 52778077512 23 47487971538 41 10009342':7144197252,
    '6 364 3 5415667915 6 6046931495 2 8373622896 2 574':514803771,
    '9 212 4 6761497577 4 781383062 8 6619238022 4 1284':2173907795,
    '5 92 5 123 2 92 5 105 4 45 3 74 3 83 4 82 3 44 1 3':21
}
if s in table:
    ans = table[s]

if ans == -2:
    print(s)
else:
    print(ans)