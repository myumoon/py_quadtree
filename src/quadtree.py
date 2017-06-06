#!/usr/bin/python
# -*- coding:utf-8 -*-

import math
	
class QuadTree(object):
	u"""四分木
	"""
	
	def __init__(self, level, rectBeginXY, rectEndXY):
		"""コンストラクタ
		@param level        空間を分割する深さ(0=空間数0, 1=空間数9, 2=空間数73 ...)
		@param rectBeginXY  空間開始座標
		@param rectEndXY    空間終点座標
		"""
		self.__level = level
		self.__begin = rectBeginXY
		self.__end   = rectEndXY
		assert self.__begin.x < self.__end.x
		assert self.__begin.y < self.__end.y
		self.__size  = math.Vec2(self.__end - self.__begin)
		self.clear()

	def add(self, obj):
		u"""オブジェクトをツリーに登録
		"""
		idx = self.getIndexOf(obj)
		if 0 <= idx:
			self.linerTree[idx].append(obj)
			
	def clear(self):
		u"""ツリーの内容をクリア
		"""
		# 線形ツリーに必要な要素分だけ確保
		self.linerTree = [[] for i in range(2 ** (2 * self.__level))]
		
	def traverse(self, traverser):
		"""ツリー内を探索
		"""
		pass
		
	def getIndexOf(self, sphere):
		"""指定オブジェクトが所属する空間インデックスを返す
		"""
		print "sphere", sphere
		sphereMin = math.Vec2(sphere.pos.x - sphere.r, sphere.pos.y - sphere.r)
		sphereMax = math.Vec2(sphere.pos.x + sphere.r, sphere.pos.y + sphere.r)
		print "sphereMin", sphereMin
		print "sphereMax", sphereMax
		minIdx = math.Vec2(
			self.__getAxisIndex(sphereMin.x, self.__begin.x, self.__end.x),
			self.__getAxisIndex(sphereMin.y, self.__begin.y, self.__end.y)
		)
		maxIdx = math.Vec2(
			self.__getAxisIndex(sphereMax.x, self.__begin.x, self.__end.x),
			self.__getAxisIndex(sphereMax.y, self.__begin.y, self.__end.y)
		)
		if minIdx.x < 0 or minIdx.y < 0 or maxIdx.x < 0 or maxIdx.y < 0:
			return -1

		print "minIdx", minIdx
		print "maxIdx", maxIdx
		minMortonIndex    = self.__getMortonIndex(minIdx.x, minIdx.y)
		maxMortonIndex    = self.__getMortonIndex(maxIdx.x, maxIdx.y)
		print "minMortonIndex", minMortonIndex
		print "maxMortonIndex", maxMortonIndex
		commonLevel       = self.__getCommonLevel(minMortonIndex, maxMortonIndex)
		print "commonLevel", commonLevel
		if 0 < commonLevel:
			commonMortonIndex = minMortonIndex >> ((self.__level - commonLevel) * 2)
			print "commonMortonIndex", commonMortonIndex
			
			# todo:事前に計算したほうがいい
			offset = (4 ** commonLevel - 1) / 3
			sphereIndex       = offset + commonMortonIndex
			return sphereIndex
		return 0

	def __separateBit(self, n):
		result = 0
		for i in reversed(xrange(0, self.__level + 1)):
			result |= (n & (1 << i)) << i
		return result
			
	def __getMortonIndex(self, idxX, idxY):
		return self.__separateBit(idxX) | self.__separateBit(idxY) << 1
		
	def __getCommonLevel(self, idx0, idx1):
		u"""2点の共有空間レベルを取得
		"""
		print "idx0:%d(%s)" % (idx0, bin(idx0))
		print "idx1:%d(%s)" % (idx1, bin(idx1))
		if self.__level == 0:
			return 0
		xor = idx0 ^ idx1
		print "xor", bin(xor)
		level = self.__level
		while 0 < xor:
			xor = xor >> 2
			level -= 1
			print "shift level", level
		return level
		
	def __getAxisIndex(self, pos, begin, end):
		"""軸に対するインデックスを返す
		"""
		# 範囲外はマイナス値を返す
		if pos < begin or end < pos:
			return -1
		width = end - begin
		return int((pos - begin) / (float(width) / (2 ** self.__level)))


# test
#sphere1 = math.Sphere(math.Vec3(200, 300, 400), 50.0)
#sphere2 = math.Sphere(math.Vec3(300, 400, 500), 20.0)
sphere1 = math.Sphere(math.Vec3(0, 0, 0), 0.5)
sphere2 = math.Sphere(math.Vec3(1, 0, 0), 0.5)
#camera  = math.Sphere(math.Vec3(210, 310, 410), 1.0)

octtree = QuadTree(3, math.Vec3(0, 0, 0), math.Vec3(4, 4, 4))
#octtree.add(sphere1)
#octtree.add(sphere2)
#print octtree.getIndexOf(sphere1)
#print octtree.getIndexOf(sphere2)
#octtree.traverse(camera)

#print octtree._OctTree__getCommonLevel(16, 23)
#print octtree.getIndexOf(math.Sphere(math.Vec2(1, 1), 0.8))
#print octtree.getIndexOf(math.Sphere(math.Vec2(2, 2), 0.8))
#print octtree.getIndexOf(math.Sphere(math.Vec2(3, 3), 0.8))
#print octtree.getIndexOf(math.Sphere(math.Vec2(0.5, 0.5), 0.1))
#print octtree.getIndexOf(math.Sphere(math.Vec2(3.5, 3.5), 0.1))
octtree.add(math.Sphere(math.Vec2(3.5, 3.5), 0.1))


