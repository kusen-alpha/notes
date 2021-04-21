# 方式一
s = "I love you!"
l = list(s)
l[2:6] = ['l', 'i', 'k', 'e']
s = ''.join(l)
print(s)

# 方式二
s = "I love you!"
b = bytearray(s.encode())
b[2:6] = [ord('l'), ord('i'), ord('k'), ord('e')]
s = b.decode()
print(s)
