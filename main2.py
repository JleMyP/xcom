# -*- coding: utf-8 -*-

import pygame, sys, geom
from pygame.locals import *
from random import randrange as rnd, choice


class Images(object) :
  def __init__(self):
    US = pygame.Surface((70, 35))
    US.fill((255, 255, 255))
    pygame.draw.polygon(US, (100, 100, 100), ((h/2+5, h/2+5), (h/2+5, h/2), (h/2+35, h/2), (h+35, h), (h+35, h+5), (h+5, h+5)))
    pygame.draw.rect(US, 0, (h/2+5, h/2, 30, 5), 1)
    pygame.draw.lines(US, 0, 0, ((h+5, h+5), (h+35, h+5), (h+35, h)))
    for x, y in ((h/2+5,h/2+5), (h/2+35, h/2+5), (h/2+35, h/2)) :
      pygame.draw.line(US, 0 , (x, y), (x+h/2, y+h/2))
    US.set_colorkey((255, 255, 255))  
    self.US = US.convert_alpha()
    
    LS = pygame.Surface((35, 70))
    LS.fill((255, 255, 255))
    pygame.draw.polygon(LS, (100, 100, 100), ((h/2, h/2+5), (h/2+5, h/2+5), (h+5, h+5), (h+5, h+35), (h, h+35), (h/2, h/2+35)))
    pygame.draw.rect(LS, 0, (h/2, h/2+5, 5, 30), 1)
    pygame.draw.lines(LS, 0, 0, ((h, h+35), (h+5, h+35), (h+5, h+5)))
    for x, y in ((h/2, h/2+35), (h/2+5, h/2+35), (h/2+5, h/2+5)) :
      pygame.draw.line(LS, 0, (x, y), (x+h/2, y+h/2))
    LS.set_colorkey((255, 255, 255))
    self.LS = LS.convert_alpha()
    
    UB = pygame.Surface((70, 35))
    UB.fill((255, 255, 255))
    pygame.draw.polygon(UB , (100, 100, 100), ((5, 0), (35, 0), (h+35, h), (h+35, h+5), (h+5, h+5), (5,5)))
    pygame.draw.rect(UB, 0, (5, 0, 30, 5), 1)
    pygame.draw.lines(UB, 0, 0, ((h+5, h+5), (h+35, h+5), (h+35, h)))
    for x, y in ((5,5), (35, 5), (35, 0)) :
      pygame.draw.line(UB, 0 , (x, y), (x+h, y+h))
    UB.set_colorkey((255, 255, 255))
    self.UB = UB.convert_alpha()
    
    LB = pygame.Surface((35, 70))
    LB.fill((255, 255, 255))
    pygame.draw.polygon(LB, (100, 100, 100), ((0, 5), (5, 5), (h+5, h+5), (h+5, h+35), (h, h+35), (0, 35)))
    pygame.draw.rect(LB, 0, (0, 5, 5, 30), 1)
    pygame.draw.lines(LB, 0, 0, ((h, h+35), (h+5, h+35), (h+5, h+5)))
    for x, y in ((0, 35), (5, 35), (5, 5)) :
      pygame.draw.line(LB, 0, (x, y), (x+h, y+h))
    LB.set_colorkey((255, 255, 255))
    self.LB = LB.convert_alpha()
    
    Block = pygame.Surface((70, 70))
    Block.fill((255, 255, 255))
    pygame.draw.polygon(Block, 0, ((h/2+5, h/2+35), (h/2+5, h/2+5), (h/2+35, h/2+5), (h+35, h+5), (h+35, h+35), (h+5, h+35)))
    pygame.draw.rect(Block, (120, 120, 120), (h/2+5, h/2+5, 30, 30), 1)
    pygame.draw.lines(Block, (120, 120, 120), 0, ((h+5, h+35), (h+35, h+35), (h+35, h+5)))
    for x, y in ((h/2+5, h/2+35), (h/2+35, h/2+35), (h/2+35, h/2+5)) :
      pygame.draw.line(Block, (120, 120, 120), (x, y), (x+h/2, y+h/2))
    Block.set_colorkey((255, 255, 255))
    self.Block = Block.convert_alpha()
    

class Classes(object):
  def __init__(self):
    self.w_pistolet = {'name': ru('пистолет'), 'damag': 1, 'crit': 2, 'ammo': 6, 'func': self.f_pistolet}
    self.w_automat = {'name': ru('автомат'), 'damag': 3, 'crit': 5, 'ammo': 5, 'func': self.f_automat}
    self.w_shotgun = {'name': ru('дробовик'), 'damag': 5, 'crit': 7, 'ammo': 4, 'func': self.f_shotgun}
    self.w_rifle = {'name': ru('винтовка'), 'damag': 5, 'crit': 8, 'ammo': 4, 'func': self.f_rifle}
    self.w_pulemet = {'name': ru('пулемет'), 'damag': 4, 'crit': 6, 'ammo': 4, 'func': self.f_pulemet}
    self.w_bazooka = {'name': ru('базука'), 'damag_center': 5, 'damag_range':3, 'range': 5, 'first': True, 'ammo':1, 'func': self.f_bazooka}
    self.w_grenade = {'name': ru('граната'), 'damag_center': 4, 'damag_range': 3, 'range': 4, 'first': False, 'ammo': 1, 'func': self.f_grenade}
    
    self.support = {'hp': 5, 'move': 5, 'weapons': (self.w_pistolet, self.w_automat), 'skills': 0}
    self.sturm = {'hp': 5, 'move': 4, 'weapons': (self.w_pistolet, self.w_shotgun), 'skills': 0}
    self.sniper = {'hp': 4, 'move': 4, 'weapons': (self.w_pistolet, self.w_rifle), 'skills': 0}
    self.heavy = {'hp': 6, 'move': 3, 'weapons': (self.w_pulemet, self.w_bazooka), 'skills': 0}
  
  def get_wall(self, source, target):
    fx, fy = target.pos
    a = geom.angle_to_point(target.pos, source.pos)
    if    45 < a < 135 : wall = map[fx][fy][1]
    elif 225 < a < 315 : wall = map[fx][fy][2]
    elif 135 < a < 225 : wall = map[fx][fy][3]
    elif a < 45 or a > 315 : wall = map[fx][fy][4]
    elif a == 45  : wall = min(map[fx][fy][2], map[fx][fy][3])
    elif a == 135 : wall = min(map[fx][fy][2], map[fx][fy][4])
    elif a == 225 : wall = min(map[fx][fy][1], map[fx][fy][4])
    elif a == 315 : wall = min(map[fx][fy][1], map[fx][fy][3])
    else : print a
    return wall
  
  def f_pistolet(self, source, target):
    distanc = geom.m_vector(source.pos, target.pos)
    wall = self.get_wall(source, target)
    acc = 100-distance-wall*10
    return acc
  
  def f_automat(self, source, target):
    distanc = geom.m_vector(source.pos, target.pos)
    wall = self.get_wall(source, target)
    acc = 100-distance*2-wall*10
    return acc
  
  def f_pulemet(self, source, target):
    distanc = geom.m_vector(source.pos, target.pos)
    wall = self.get_wall(source, target)
    acc = 100-distance*3-wall*10
    return acc
  
  def f_shotgun(self, source, target):
    distanc = geom.m_vector(source.pos, target.pos)
    wall = self.get_wall(source, target)
    acc = 100-distance*4-wall*10
    return acc
  
  def f_rifle(self, source, target):
    distanc = geom.m_vector(source.pos, target.pos)
    wall = self.get_wall(source, target)
    acc = 100-distance/2-wall*10
    return acc

  def f_bazooka(self, source, target):
    pass
   
  def f_grenade(self, source, target):
    pass


class Soldat(object) :
  def __init__(self, cls, r, hp, attack, accuracy, cmd, pos=None, color=(255, 0, 0)):
    self.r, self.full_hp, self.uron = r, hp, attack
    self.accuracy, self.command = accuracy, cmd
    self.pos, self.color = None, color
    self.rad, self.turns, self.hp, self.path = None, 2, hp, 0
    cmd.append(self)
    if pos : self.start(pos)
    soldats.append(self)
    
    self.img = pygame.Surface((70, 70))
    self.img.fill((10, 10, 10))
    pygame.draw.polygon(self.img, color, ((h/3+5, h/3+5), (h/3+35, h/3+5), (35+h, 5+h), (35+h, 35+h), (5+h, 35+h), (h/3+5, h/3+35)))
    pygame.draw.rect(self.img, 0, (h/3+5, h/3+5, 30, 30), 1)
    pygame.draw.lines(self.img, 0, 0, ((35+h, 5+h), (35+h, 35+h), (5+h, 35+h)))
    for x, y in ((h/3+35, h/3+5), (h/3+35, h/3+35), (h/3+5, h/3+35)) :
      pygame.draw.line(self.img, 0, (x, y), (x+h-h/3, y+h-h/3))
    self.img.set_colorkey((10, 10, 10))
    self.img = self.img.convert_alpha()
  
  def draw(self):
    x, y = self.pos[0]*cell, self.pos[1]*cell
    window.blit(self.img, (x, y))
  
  def start(self, pos):
    self.pos = tuple(pos)
    map[pos[0]][pos[1]][0] = self
    self.rad = []
  
  def focus(self):
    global focus
    if self.turns and not self.rad : self.rad = radius(self.pos, self.r)
    focus = [self, None, None]
  
  def unfocus(self):
    global focus
    self.rad, self.path, self.acc, focus = [], 0, 0, 0
  
  def hide(self): map[self.pos[0]][self.pos[1]][0] = 0
  
  def move(self):
    if self.path :
      self.hide()
      self.rad = []
      for p in self.path :
        self.pos = p
        draw()
        pygame.time.wait(100)
      self.turns -= 1
      self.path = 0
      self.start(p)
      if self.turns : self.focus()
      else : self.unfocus()
  
  def get_acc(self):
    fx, fy = focus[1].pos
    '''path = path_attack(self.pos, focus[1].pos)
    for x, y in path :
      if map[x][y][0] == 1 : return 0'''
    distanc = geom.m_vektor(self.pos, focus[1].pos)
    a = geom.angle_to_point(focus[1].pos, self.pos)
    if    45 < a < 135 : wall = map[fx][fy][1]
    elif 225 < a < 315 : wall = map[fx][fy][2]
    elif 135 < a < 225 : wall = map[fx][fy][3]
    elif a < 45 or a > 315 : wall = map[fx][fy][4]
    elif a == 45  : wall = min(map[fx][fy][2], map[fx][fy][3])
    elif a == 135 : wall = min(map[fx][fy][2], map[fx][fy][4])
    elif a == 225 : wall = min(map[fx][fy][1], map[fx][fy][4])
    elif a == 315 : wall = min(map[fx][fy][1], map[fx][fy][3])
    else : print a
    acc = self.accuracy-distanc-wall*10
    return acc
  
  def attack(self):
    self.turns = 0
    chanc = rnd(100)
    if chanc <= focus[2] : focus[1].damag(self.uron)
    else :
      x, y = focus[1].pos[0]*cell, focus[1].pos[1]*cell
      mimo = font30.render(ru('мимо'), True, (0, 0, 0))
      window.blit(mimo, (x, y))
      pygame.display.update()
      pygame.time.wait(1000)
    self.unfocus()
  
  def damag(self, dmg):
    x, y = self.pos[0]*cell, self.pos[1]*cell
    text = font30.render(u'-%i'%dmg, True, (0, 0, 0))
    window.blit(text, (x, y))
    pygame.display.update()
    pygame.time.wait(1000)
    if dmg > self.hp : dmg = self.hp
    self.hp -= dmg
    if not self.hp : self.kill()
  
  def kill(self):
    soldats.remove(self)
    self.command.remove(self)
    self.hide()


def draw(clr=True):
  if clr : window.fill((255, 255, 255))
  for x in range(map_w):
    for y in range(map_h):
      px, py = x*cell, y*cell
      pygame.draw.rect(window, 0, (px+h, py+h, cell, cell), 1)
      if   map[x][y][0] == 1 : window.blit(images.Block, (px, py))
      if   map[x][y][1] == 1 : window.blit(images.US, (px, py))
      elif map[x][y][1] == 2 : window.blit(images.UB, (px, py))
      if   map[x][y][3] == 1 : window.blit(images.LS, (px, py))
      elif map[x][y][3] == 2 : window.blit(images.LB, (px, py))
      if map[x][y][0] in soldats : map[x][y][0].draw()
      if   map[x][y][2] == 1 : window.blit(images.US, (px, py+35))
      elif map[x][y][2] == 2 : window.blit(images.UB, (px, py+35))
      if   map[x][y][4] == 1 : window.blit(images.LS, (px+35, py))
      elif map[x][y][4] == 2 : window.blit(images.LB, (px+35, py))
  if focus :
    if   focus[0].turns == 2 : color = (0, 255, 0)
    elif focus[0].turns == 1 : color = (255, 255, 0)
    for p in focus[0].rad :
      pygame.draw.rect(window, color, (p[0]*cell+h+5, p[1]*cell+h+5, cell-10, cell-10), 3)
    if focus[0].path :
      path = [(x*cell+h+cell/2, y*cell+h+cell/2) for x, y in focus[0].path]
      pygame.draw.lines(window, (255, 0, 0), 0, path, 3)
    focus[0].draw()
    if focus[1] :
      x, y = focus[1].pos[0]*cell+h, focus[1].pos[1]*cell+h
      pygame.draw.rect(window, (255, 0, 0), (x, y, cell, cell), 3)
      focus[1].draw()
      pygame.draw.rect(window, 0, btn_attack)
    if not (focus[2] is None) :
      text = font30.render(ru('попадание : %i'%focus[2]+'%'), True, (0, 0, 0))
      window.blit(text, (450, win_h-135))
      text = font30.render(ru('здоровье : %i'%focus[1].hp), True, (0, 0, 0))
      window.blit(text, (450, win_h-95))
    
    text = font30.render(ru('здоровье : %i'%focus[0].hp), True, (0, 0, 0))
    window.blit(text, (200, win_h-135))
    text = font30.render(ru('точность : %i'%focus[0].accuracy+'%'), True, (0, 0, 0))
    window.blit(text, (200, win_h-95))
    text = font30.render(ru('урон : %i'%focus[0].uron), True, (0, 0, 0))
    window.blit(text, (200, win_h-55))
  pygame.draw.line(window, 0, (0, win_h-150), (win_w, win_h-150))
  pygame.draw.rect(window, commands[turn][0].color, btn_next)
  pygame.display.update()

def event_callback():
  for event in pygame.event.get() :
    if event.type == MOUSEBUTTONDOWN :
      px, py = event.pos
      if py < win_h-150 :
        x, y = int((px-h)/cell), int((py-h)/cell)
        if not focus :
          for s in commands[turn] :
            if s.pos == (x, y) :
              s.focus()
              break
        else :
          if focus[0].pos == (x, y) : focus[0].unfocus()
          elif map[x][y][0] == focus[1] : focus[1] = focus[2] = None
          elif map[x][y][0] in soldats and map[x][y][0] not in focus[0].command and focus[0].turns :
            focus[1] = map[x][y][0]
            focus[2] = focus[0].get_acc()
            focus[0].path = None
          elif focus[0].path and [x, y] == focus[0].path[-1] : focus[0].move()
          elif [x, y] in focus[0].rad : focus[0].path = find_path_astar(focus[0].pos, (x, y))
      else :
        if btn_next.collidepoint(px, py) : next_turn()
        elif btn_attack.collidepoint(px, py) :
          attack()
 
def is_step(pos, dir, map):
  x, y = pos
  this, next = map[x][y], None
  if dir == 1 and y > 0 : next = map[x][y-1]
  elif dir == 2 and y < map_h-1 : next = map[x][y+1]
  elif dir == 3 and x > 0 : next = map[x-1][y]
  elif dir == 4 and x < map_w-1 : next = map[x+1][y]
  elif dir == 5 and is_step(pos, 1, map) and is_step(pos, 3, map) and is_step((x-1, y), 1, map) and is_step((x, y-1), 3, map) :
    next = map[x-1][y-1]
  elif dir == 6 and is_step(pos, 1, map) and is_step(pos, 4, map) and is_step((x, y-1), 4, map) and is_step((x+1, y), 1, map) :
    next = map[x+1][y-1]
  elif dir == 7 and is_step(pos, 2, map) and is_step(pos, 4, map) and is_step((x+1, y), 2, map) and is_step((x, y+1), 4, map) :
    next = map[x+1][y+1]
  elif dir == 8 and is_step(pos, 2, map) and is_step(pos, 3, map) and is_step((x-1, y), 2, map) and is_step((x, y+1), 3, map) :
    next = map[x-1][y+1]
  if dir<5 and next and not next[0] and this[dir] < 2 :
    return next
  elif dir > 4 and next and not next[0] :
    return next
  return False

def sort_opens(opens):
  min = -1
  for n in range(len(opens)-1):
    if opens[n][5][2] < opens[min][5][2] : min = n
  opens[-1], opens[min] = opens[min], opens[-1]
  return opens

def find_path_astar(start, finish):
  mmap = []
  for x in range(map_w):
    mmap.append([
      map[x][y] + [[x, y]] for y in range(map_h)
    ])
  xs, ys = start
  xf, yf = finish
  opens, closed, path = [mmap[xs][ys]], [], []
  mmap[xs][ys][5] = [0, 0, 0, None, xs, ys]
  while opens :
    v = opens.pop(-1)
    closed.append(v)
    if v[5][-2:] == [xf, yf] : break
    for d in range(1,9):
      next = is_step(v[5][-2:], d, mmap)
      if not next or next in closed : continue
      if d < 5 : g = v[5][0] + 10
      else : g = v[5][0] + 14
      if next not in opens :
        hh = h_func(next[5], finish)
        next[5] = [g, hh, g+hh, v]+list(next[5])
        opens.append(next)
      else :
        if g < next[5][0] :
          next[5][0], next[5][2], next[5][3] = g, g+next[5][1], v
    if opens : opens = sort_opens(opens)
  if closed[-1][5][-2:] == [xf, yf] :
    v = closed[-1]
    while 1 :
      path.append(v[5][-2:])
      if v[5][-2:] == [xs, ys] : break
      v = v[5][3]
    path.reverse()
  #opens = [o[0][-2:] for o in opens]
  #closed = [c[0][-2:] for c in closed]
  return path

def radius(pos, r):
  mmap = []
  for x in range(map_w):
    mmap.append([
      map[x][y] + [[x, y]] for y in range(map_h)
    ])
  xs, ys = pos
  opens, closed, path = [mmap[xs][ys]], [], []
  mmap[xs][ys][5] = [0, xs, ys]
  while opens :
    v = opens.pop(0)
    closed.append(v)
    for d in range(1,9):
      next = is_step(v[5][-2:], d, mmap)
      if not next or next in closed : continue
      if d < 5 : g = v[5][0] + 10
      else :     g = v[5][0] + 14
      if next not in opens and g <= r*10 :
        next[5] = [g]+next[5]
        opens.append(next)
      else :
        if g < next[5][0] :  next[5][0] = g
  del closed[0]
  closed = [c[5][-2:] for c in closed]
  return closed

def path_attack(pos1, pos2):
  sx, sy = pos1
  fx, fy = pos2
  pc, points = [sx, sy], []
  sx_pos, sy_pos = sx*cell+cell/2, sy*cell+cell/2
  fx_pos, fy_pos = fx*cell+cell/2, fy*cell+cell/2
  func_x = geom.get_func((sx_pos, sy_pos), (fx_pos, fy_pos))
  func_y = geom.get_func((sx_pos, sy_pos), (fx_pos, fy_pos), 2)
  while pc != [fx, fy] :
    print pc
    tlx, tly = pc[0]*cell, pc[1]*cell
    brx, bry = tlx+cell, tly+cell
    coll_y_l, coll_y_r = func_x(tlx), func_x(brx)
    coll_x_u, coll_x_d = func_y(tly), func_y(bry)
    if tlx < coll_x_u < brx and sx_pos < coll_x_u < fx_pos and (coll_x_u, tly) not in points :
      pc[1] -= 1
      points.append((coll_x_u, tly))
    if tlx < coll_x_d < brx and sx_pos < coll_x_d < fx_pos and (coll_x_d, bry) not in points :
      pc[1] += 1
      points.append((coll_x_d, bry))
    if tly < coll_y_l < bry and sy_pos < coll_y_l < fy_pos and (tlx, coll_y_l) not in points :
      pc[0] -= 1
      points.append((tlx, coll_y_l))
    if tly < coll_y_r < bry and sy_pos < coll_y_r < fy_pos and (brx, coll_y_r) not in points :
      pc[0] += 1
      points.append((brx, coll_y_r))
  cells = [(sx, sy)] + [(int(x/cell), int(y/cell)) for x, y in points]
  return cells

def rotate_map(map, po_chas=True):
  nmap = []
  for y in range(map_h):
    n = []
    for x in range(map_w):
      if po_chas :
        n.append([map[x][y][0], map[x][y][3], map[x][y][4], map[x][y][2], map[x][y][1]])
      else :
        n.append([map[x][y][0], map[x][y][4], map[x][y][3], map[x][y][1], map[x][y][2]])
    if not po_chas : n.reverse()
    nmap.append(n)
  if po_chas :
    nmap.reverse()
  for s in soldats :
    if po_chas : s.pos = (map_w-1-s.pos[1], s.pos[0])
    else :       s.pos = (s.pos[1], map_w-1-s.pos[0])
  return nmap

def rectangle(surf, color1, color2, rect, width=1):
  pygame.draw.rect(surf, color2, rect)
  pygame.draw.rect(surf, color1, rect, width)


def next_turn():
  global turn
  if focus : focus[0].unfocus()
  turn += 1
  if turn == len(commands) : turn = 0
  if commands[turn] :
    for s in commands[turn] : s.turns = 2
  else : next_turn()

def attack():
  if focus and focus[1] : focus[0].attack()



sys.stderr = sys.stdout = open('err.txt','w')

win_w,win_h = 900,600
pygame.init()
window = pygame.display.set_mode((0, 0), FULLSCREEN)
win_w,win_h = window.get_size()
pygame.display.set_caption('xcom')
clock = pygame.time.Clock()
font30 = pygame.font.Font('freesansbold.ttf',30)
font28 = pygame.font.Font('freesansbold.ttf',28)

cell, soldats, turn = 40, [], 0
commands, focus = [[], [], []], None
h, run = int(cell*0.5), True
map_w, map_h = int((win_w-h)/cell), int((win_h-h-150)/cell)
#map_w = map_h
map = [[[0,0,0,0,0] for y in range(map_h)] for x in range(map_w)]
h_func = lambda a, b : max(abs(a[0]-b[0]), abs(a[1]-b[1]))*10
ru = lambda x : str(x).decode('utf-8')
images = Images()
classes = Classes()

btn_next = pygame.Rect(50, win_h-135, 100, 50)
btn_attack = pygame.Rect(50, win_h-65, 100, 50)

map[3][3][1] = map[3][2][2] = 1
map[3][3][4] = map[4][3][3] = 2
map[3][3][2] = map[3][4][1] = 1
map[5][2][0] = 1
map[5][3][0] = 1
map[4][2][0] = 1

Soldat(classes.support, 4, 4, 2, 80, commands[0], (3, 3))
Soldat(classes.sturm, 3, 4, 2, 80, commands[0], (3, 4))
Soldat(0, 4, 4, 2, 80, commands[1], (8, 3), (0, 255, 0))
Soldat(0, 3, 4, 2, 80, commands[1], (8, 4), (0, 255, 0))
Soldat(0, 4, 4, 2, 80, commands[2], (5, 7), (0, 0, 255))
Soldat(0, 3, 4, 2, 80, commands[2], (6, 7), (0, 0, 255))
#map = rotate_map(map)

#print path_attack((1,1),(3,5))

while run :
  event_callback()
  draw()
  clock.tick()

pygame.quit()