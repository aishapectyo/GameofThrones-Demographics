#!/usr/bin/env python

import sys
import os
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import csv
from collections import defaultdict

#----Functions----#
def median(ages):
	sorts = sorted(ages)
	length = len(sorts)
	if not length % 2:
		return (sorts[length / 2] + sorts[length / 2 - 1]) / 2.0
	return sorts[length / 2]


#----Read Data----#
names = []
age = []
status = []
gender = []
with open('gotData.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		names.append(row[0])
		age.append(row[1])
		status.append(row[2])
		gender.append(row[3])


#----Analyze Data----#
file_len = len(names)
females_alive = 0
males_alive  = 0
females_dead = 0
males_dead = 0

for i in xrange(file_len):
	if gender[i] == '1' and status[i] == '1':
		males_dead = males_dead + 1
	if gender[i] == '1' and status[i] == '0':
		males_alive = males_alive + 1
	if gender[i] == '0' and status[i] == '1':
		females_dead = females_dead + 1
	if gender[i] == '0' and status[i] == '0':
		females_alive = females_alive + 1

print('Total characters: ',file_len)
print('Dead males: ', males_dead)
print('Alive males: ', males_alive)
print('Dead females: ', females_dead)
print('Alive females: ', females_alive)

#Find alive people
age_dead = []
age_alive = []
for m in range(file_len):
	if status[m] == '0':
		element = int(age[m])
		age_alive.append(element)
	if status[m] == '1':
		element = int(age[m])
		age_dead.append(element)

median_alive = median(age_alive)
print('Median age alive: ',  median_alive)
median_dead = median(age_dead)
print('Median age dead: ', median_dead)
print('Mean age alive: ', np.mean(age_alive))
print('Mean age dead: ', np.mean(age_dead))

age_dead_female = []
age_dead_male = []
for m in range(file_len):
	if status[m] == '0' and gender[m] == '0':
		element = int(age[m])
		age_dead_female.append(element)
	if status[m] == '0' and gender[m] == '1':
		element = int(age[m])
		age_dead_male.append(element)


median_dead_female = median(age_dead_female)
print('Median age dead (females): ',  median_dead_female)
median_dead_male = median(age_dead_male)
print('Median age dead (males): ', median_dead_male)
print('Mean age alive(female): ', np.mean(age_dead_female))
print('Mean age dead (male): ', np.mean(age_dead_male))


#Finding longevity
age_int = []
for n in xrange(file_len):
	if n > 0:
		element = int(age[n])
		age_int.append(element)

c10=0.0
c10b = 0.0
c20=0.0
c20b=0.0
c30=0.0
c30b = 0.0
c40=0.0
c40b=0.0
c50=0.0
c50b = 0.0
c60=0.0
c60b=0.0
c70=0.0
c70b = 0.0
c80=0.0
c80b=0.0
c90=0.0
c90b = 0.0
c100=0.0
c100b=0.0

age_len = len(age_int)
for l in xrange(len(age_int)):
	if age_int[l] <= 10:
		c10 = c10 + 1
		if status[l]  == '0':
			c10b = c10 / age_len
	if age_int[l] > 10 <= 20:
		c20 = c20 + 1
		if status[l]  == '0':
			c20b = c20 / age_len
	if age_int[l] > 20 <= 30:
		 c30 = c30 + 1
		 if status[l]  == '0':
			 c30b = c30 / len(age_int)
	if age_int[l] >30 <= 40:
		c40 = c40 + 1
		if status[l]  == '0':
			c40b = c40/age_len
	if age_int[l] >40 <= 50:
		c50 = c50 + 1
		if status[l]  == '0':
			c50b = c50/age_len
	if age_int[l] > 50 <= 60:
		c60 = c60 + 1
		if status[l]  == '0':
			c60b = c60 / age_len
	if age_int[l] >60 <= 70:
		c70 = c70 + 1
		if status[l]  == '0':
			c70b = c70/age_len
	if age_int[l] >70 <= 80:
		c80 = c80 + 1
		if status[l]  == '0':
			c80b = c80 / age_len
	if age_int[l] >80 <= 90:
		c90 = c90 + 1
		if status[l]  == '0':
			c90b = c90/age_len
	if age_int[l] > 90 <= 100:
		c100 = c100 + 1
		if status[l]  == '0':
			c100b = c100/age_len

xvals = (0, 20,30,40,50,60,70,80,90,100)
yvals = (1, c20b, c30b, c40b, c50b, c60b, c70b, c80b, c90b, c100b)


fig, ax = plt.subplots()
plt.hist(age_alive, histtype='stepfilled', color='#008080', alpha = 0.2)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_color('#413839')
ax.spines['bottom'].set_color('#413839')

fig, ax = plt.subplots()
plt.hist(age_dead, histtype='stepfilled', color='#008080', alpha = 0.20)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.spines['left'].set_color('#413839')
ax.spines['top'].set_color('#413839')


#fig, ax = plt.subplots()
plt.figure(3)
plt.hist(age_dead_male, histtype='stepfilled', color='#008080', alpha = 0.20, label='Age Male Deaths')
plt.hist(age_dead_female, histtype='stepfilled', color='r', alpha = 0.20, label='Age Female Deaths')
#ax.spines['top'].set_visible(False)
#ax.spines['right'].set_visible(False)
#ax.spines['bottom'].set_visible(True)
#ax.spines['left'].set_visible(True)
#ax.yaxis.set_ticks_position('left')
#ax.xaxis.set_ticks_position('bottom')
plt.legend(loc='upper right')

plt.figure(4, figsize=(6,6))
labels = "Alive Females", "Dead Females", "Dead Males", "Alive Males"
fracs = [females_alive, females_dead, males_dead, males_alive]
colors = ['#FDD7E4', '#C2DFFF', '#81D8D0', '#C8A2C8']
plt.rcParams['patch.linewidth'] = 2
plt.rcParams['patch.edgecolor'] = 'white'
plt.pie(fracs, labels=labels, autopct = '%1.1f%%', shadow=False, startangle=90, colors=colors)
plt.axis('equal')

fig, ax = plt.subplots()
plt.plot(xvals, yvals, linewidth=2.8, alpha = 0.4, color = '#F70D1A')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
ax.set_xticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_color('#413839')
ax.spines['bottom'].set_color('#413839')
plt.title('Would you want to live in Westeros?')



plt.show()

