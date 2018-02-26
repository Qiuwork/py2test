#_*_ coding:utf-8 _*_
# Author: Qiu
# def a1(a,b,c=''):
#     p = {'a':a,'b':b}
#     if c:
#         p['c'] = c
#     return p
# while True:
#     a = raw_input('a: ')
#     b = raw_input('b: ')
#     c = raw_input('c: ')
#     y = a1(a, b, c)
#     print y
#     q = raw_input('q: ')
#     if q == 'q':
#         print '退出'
#         break
# def show_magicians(magician_list):
#     for magician in magician_list:
#         print(magician.title())
# def make_great(magician_list):
#     for i in range(len(magician_list)):
#         magician_list[i] = 'the '+ magician_list[i]
#     return magician_list
# m_list = ['qq','ww','cc']
# n_list = make_great(m_list[:])
# show_magicians(m_list)
# show_magicians(n_list)

#yield https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/
# from inspect import isgeneratorfunction
#
# def f1(x):
#     for i in xrange(x):
#         yield call(i)
#         # call(i)
#         print 'i=',i
#     print 'do'
# def call(x):
#     print x*'ci', x
#
# for a in f1(5):
#     print 'a=',a
#
# print isgeneratorfunction(f1)