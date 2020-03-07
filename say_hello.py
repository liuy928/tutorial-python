# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 16:55:36 2019

@author: liuy928
"""

print('hello world')
print('what is your name?')
myName = input()
print('it is good to meet you,' + myName)
print('the length of youe name is: ')
print(len(myName))
print('what is you age?')
myAge = input()
print('you will be ' + str(int(myAge) + 1) + 'in a yer')

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break;
    catNames.append(name)
print(catNames)

for i in catNames:
    print(i)