import copy, random, numpy as np

people = ['Long-Chen', 'Xin-Yan', 'Wenbo-Ma', 'Yifeng-Huang', 'Xin-Yu', 'Shaoning-Xiao',
          'Zhihong-Jiang', 'Feifei-Shao', 'Yunan-Ye', 'Xingchen-Li', 'Weike-Jin', 'Chujie-Lu']

def conflict(xlist):
  for i in range(len(xlist) // 3):
    current = xlist[i*3: (i+1)*3]
    if len(current) != len(set(current)): return True
  return False

num = 2
xlist = num * people

while True:
  random.shuffle(xlist)
  if conflict(xlist) == False: break

for i in range(len(xlist) // 3):
  current = xlist[i*3: (i+1)*3]
  print('{:02d}-th senimar : {:}'.format(i, current))
