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

a = '[06:09:32.197998][LIB][esti_wave]nf_WAVE_MW_Send_Wsm_Unsecured(343)MW send start'
b = '[06:09:32.199068][LIB][esti_wave]nf_wave_wsmp_wave_short_message_reuest(62)wsm encode start'
c = '[06:09:32.200052][LIB][esti_wave]nf_wave_wsmp_wave_short_message_reuest(225)wsm encode end'
d = '[06:09:32.201006][LIB][esti_wave]nf_wave_wsmp_wave_short_message_reuest(244)wsm send mailbox'
e = '[06:09:32.202000][LIB][esti_wave]nff_wave_wsmp_send_task(37)wsm receive mailbox'
f = '[06:09:32.204960][LIB][esti_wave]nff_wave_wsmp_send_task(40)socket send start'
g = '[06:09:32.207050][LIB][esti_wave]nff_wave_wsmp_socket_send(170)socket send end'

print(a.count(']'))

a_i = int(a[(a.find('.')+1):(a.find(']'))])
b_i = int(b[(b.find('.')+1):(b.find(']'))])
c_i = int(c[(c.find('.')+1):(c.find(']'))])
d_i = int(d[(d.find('.')+1):(d.find(']'))])
e_i = int(e[(e.find('.')+1):(e.find(']'))])
f_i = int(f[(f.find('.')+1):(f.find(']'))])
g_i = int(g[(g.find('.')+1):(g.find(']'))])



print('a_i =', a_i)
print('type(a_i) =', type(a_i))
print('b_i =', b_i)
print('type(b_i) =', type(b_i))
print('c_i =', c_i)
print('type(c_i) =', type(c_i))
print('d_i =', d_i)
print('type(d_i) =', type(d_i))
print('e_i =', e_i)
print('type(e_i) =', type(e_i))
print('f_i =', f_i)
print('type(f_i) =', type(f_i))
print('g_i =', g_i)
print('type(g_i) =', type(g_i))
