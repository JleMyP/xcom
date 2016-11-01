# -*- coding: utf-8 -*-

from math import *


def m_vektor(p1, p2):
  m = (p2[0]-p1[0])**2+(p2[1]-p1[1])**2
  return m**0.5

def mv(v): return (v[0]**2+v[1]**2)**.5

def c_okr(r,a=360): return pi*r/180*a
def s_okr(r,a=360): return pi*r**2/360*a

def sct(a,typ=1):
  rad = pi*a/180
  if typ == 1 :
    if a in (180,360): return 0
    return sin(rad)
  elif typ == 2 :
    if a in (90,270): return 0
    return cos(rad)
  elif typ == 3 :
    if a in (180,360): return 0
    return tan(rad)
  elif typ == 4 :
    return 1/sct(a, 3)

def asct(x, typ=1):
  if   typ == 1 : sct_list = sin_list
  elif typ == 2 : sct_list = cos_list
  elif typ == 3 : sct_list = tan_list
  if x in sct_list :
    a = sct_list.index(x)
    if a > 180 : a = 360-a
    return a
  for a in range(360):
    if sct_list[a] < x < sct_list[a+1] :
      if a > 180 : a = 360 - a
      return a

def gip(a,b,c=None):
  if not c : return (a**2+b**2)**0.5
  if not a : return (c**2-b**2)**0.5
  if not b : return (c**2-a**2)**0.5

def v_to_func_from_x(v,x): return x*v[1]/v[0]
def v_to_func_from_y(v,y): return y*v[0]/v[1]

def move(angle,ln): return ln*sct(angle,1),-ln*sct(angle,2)

def init_lists():
  global sin_list,cos_list,tan_list
  sin_list = [sct(a,1) for a in range(361)]
  cos_list = [sct(a,2) for a in range(361)]
  tan_list = [sct(a,3) for a in range(361)]
  tan_list[90] = tan_list[270] = None

def angle_to_point(pos0,pos1):
  x0,y0 = pos0
  x1,y1 = pos1
  ln = m_vektor(pos0, pos1)
  sin = abs(y0-y1)/ln
  a = asct(sin)
  if y0 < y1 : a = -a
  if 0 < a < 90 and x0 > x1 : a = 180-a
  if a < 0 : a += 360
  return a

def ln_vektor(x1,y1,x2,y2,ln):
  ab = m_vektor((x1,y1),(x2,y2))
  k = ln/ab
  x,y = x2-x1,y2-y1
  return x*k,y*k

def sum_v_in_point(x1,y1,x2,y2): return x2+(x1-x2)/2,y2+(y1-y2)/2

def n_angle(g,n):
  px,py,a,an,clr = x,y,0,(n-2)*180/n,0
  colors = [0xff,0xff00,0xff0000]
  while 1:
    a += 180-an
    k1,k2 = g*sct(a,1),g*sct(a,2)
    if a == 180 : k2 = -g
    img.line((px,py,px+k2,py-k1),colors[clr])
    px,py = px+k2,py-k1
    if a in (0,360) : break
    clr += 1
    if clr == len(colors) : clr = 0
  img.line((x,y,px,py),colors[clr])

def get_func(p1, p2, typ=1):
  angle = angle_to_point(p1, p2)
  a = float(p2[1]-p1[1])/float(p2[0]-p1[0])
  b = float(p1[1]-a*p1[0])
  print a, b
  if typ == 1 :
    return lambda x : a*x+b
  elif typ == 2 :
    if a :
      return lambda y : (y-b)/a
    else :
      return lambda y : p1[0]

#an = 2Rsin(180/n)
#r = Rcos(180/n)

global sin_list,cos_list,tan_list
init_lists()
