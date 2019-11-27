import copy, random, numpy as np

people = ['Long-Chen', 'Xin-Yan', 'Wenbo-Ma', 'Yifeng-Huang', 'Xin-Yu', 'Shaoning-Xiao',
          'Zhihong-Jiang', 'Feifei-Shao', 'Yunan-Ye', 'Xingchen-Li', 'Weike-Jin', 'Chujie-Lu',
          'Jiahui-Li', 'Kaifeng-Gao', 'Nuanxin-Hong']

def conflict(xlist):
  for i in range(len(xlist) // 2):
    current = xlist[i*2: (i+1)*2]
    if len(current) != len(set(current)): return True
  return False

num = 1
xlist = num * people

while True:
  random.shuffle(xlist)
  if conflict(xlist) == False: break

for i in range(len(xlist) // 2):
  current = xlist[i*2: (i+1)*2]
  print('{:02d}-th senimar : {:}'.format(i, current))
