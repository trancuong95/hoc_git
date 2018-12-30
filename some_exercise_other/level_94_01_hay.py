d = {}
chuoi = input('Nhập chuỗi cần đếm ký tư: ')
for c in chuoi:
    d[c] = d.get(c, 0) + 1

print('\n'.join('%s, %s' % (k, v) for k, v in d.items()))
