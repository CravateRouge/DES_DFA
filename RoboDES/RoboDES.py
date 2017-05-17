'''
Created on 12 mai 2017

@author: walterwhite
'''

from robobrowser import RoboBrowser

# Browse to DES calculator
browser = RoboBrowser()
browser.open('http://www.emvlab.org/descalc/')

form = browser.get_form()

f = open('clesDES.txt', 'r')

msg = '459410AD68AB25E3'
form['input'].value = msg
form['output'].value = ''

trueEncMsg ='8ABB0A9F7009B81F' 
 
keys=[]
for line in f:
    keys.append(line.strip())

i=0
for key in keys:
    form['key'].value = key
    browser.submit_form(form,form['action'])
    i=i+1

    encMsg = browser.select('#output')[0].text
    if trueEncMsg == encMsg:
        print("solution"+key)
        break
    
    browser.back()
