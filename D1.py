# a = round(0.995, 2)
# print(a)

# 0.1+0.2


# Exercise 2
# import decimal

# print(round(3.1415, 2))
# print(round(9.995, 2))

# print(decimal.Decimal(9.995))


# Exercise 3
# t = 'He is a string. Who are you?'
# print(t.capitalize())
# print(t.split())
# print(t.find('i'))
# print(t.find('in'))
# print(t.find('Python'))
# print(t[0:4])
# print(t.replace(' ', '_'))
# w = 'http://www.google.com'
# print(w.strip('http://'))

# i=10
# while i<9:
#     print(i)
#     i-=1

# ##循环语言(Example: loops)
# for i in range(2, 10, 3):
#     print("i =", i)
#     l = i ** 2
#     print('l =', l)

# print('\nnow, while\n')

# i = 2
# while i < 10:
#     print("i =", i)
#     l = i ** 2
#     print('l =', l)
#     i += 3

# a = 0
# suma = 0
# while a <= 100:
#     suma += a
#     a += 1
# print('sum = ', suma)

# for i in range(1, 3):
#     for j in range(1, i+1):
#         print(j, '*', i, '=', i * j)

# a = 0
# for i in range(1001):
#     a += i
# print('sum =', a)

# a = 0
# i = 1
# while i <= 1000:
#     a += i
#     i += 1
# print('sum =', a)

# i = 0
# a = 0
# for i in range(0, 1001, 2):
#     a += i
# print('sum =', a)


# i = 0
# a = 0
# while i <= 1000:
#     if (i%2)==0:
#         a += i
#     i += 1
# print('sum =', a)

a = '[08:39:26.220950][LIB][esti_key]nf_WAVE_MW_Send_Wsm_Unsecured(343)SEND_WAVE_START'
print(a[0:1])
print(a.find('.'))
print(a.find(']'))
print(a[a.find(']')])
print(a[(a.find('.')+1):(a.find(']'))])
print(a.count(']'))