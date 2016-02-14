#!/usr/bin/python
# -*- coding:utf-8 -*-

import unittest
import quadtree
import math


class TestQuadTree(unittest.TestCase):
	def setup(self):
		pass
		
	def test_index_leve1_0(self):
		quadTree = quadtree.QuadTree(0, math.Vec3(0, 0), math.Vec3(10, 10))
		self.assertEqual(0, quadTree.getIndexOf(math.Circle(math.Vec2(2, 2), 1)))
		self.assertEqual(0, quadTree.getIndexOf(math.Circle(math.Vec2(8, 2), 1)))
		self.assertEqual(0, quadTree.getIndexOf(math.Circle(math.Vec2(2, 8), 1)))
		self.assertEqual(0, quadTree.getIndexOf(math.Circle(math.Vec2(8, 8), 1)))
		self.assertEqual(0, quadTree.getIndexOf(math.Circle(math.Vec2(5, 5), 1)))
		
	def test_index_leve1_1(self):
		quadTree = quadtree.QuadTree(1, math.Vec3(0, 0), math.Vec3(10, 10))
		self.assertEqual(0, quadTree.getIndexOf(math.Circle(math.Vec2(5, 5), 1)))
		self.assertEqual(1, quadTree.getIndexOf(math.Circle(math.Vec2(2, 2), 1)))
		self.assertEqual(2, quadTree.getIndexOf(math.Circle(math.Vec2(8, 2), 1)))
		self.assertEqual(3, quadTree.getIndexOf(math.Circle(math.Vec2(2, 8), 1)))
		self.assertEqual(4, quadTree.getIndexOf(math.Circle(math.Vec2(8, 8), 1)))

if __name__ == "__main__":
	unittest.main()

