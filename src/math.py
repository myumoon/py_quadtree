#!/usr/bin/python
# -*- coding:utf-8 -*-


class Vec2(object):
	u"""2次元ベクトル
	"""
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
		
	def __add__(self, vec2):
		return Vec2(self.x + vec2.x, self.y + vec2.y)
		
	def __sub__(self, vec2):
		return Vec2(self.x - vec2.x, self.y - vec2.y)
	
	def __repr__(self):
		return "(x:%f, y:%f)" % (self.x, self.y)
	
class Vec3(object):
	u"""3次元ベクトル
	"""
	def __init__(self, x = 0, y = 0, z = 0):
		self.x = x
		self.y = y
		self.z = z
		
	def __add__(self, vec3):
		return Vec3(self.x + vec3.x, self.y + vec3.y, self.z + vec3.z)
		
	def __sub__(self, vec3):
		return Vec3(self.x - vec3.x, self.y - vec3.y, self.z - vec3.z)
	
	def __repr__(self):
		return "(x:%f, y:%f, z:%f)" % (self.x, self.y, self.z)
		
class Circle(object):
	u"""円
	"""
	def __init__(self, pos, radius):
		self.pos = pos
		self.r   = radius
		
	def __repr__(self):
		return "<pos:%s, r:%f>" % (self.pos, self.r)

class Sphere(object):
	u"""球体
	"""
	def __init__(self, pos, radius):
		self.pos = pos
		self.r   = radius
		
	def __repr__(self):
		return "<pos:%s, r:%f>" % (self.pos, self.r)

