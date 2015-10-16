import fnmatch
import os

class ImageLoader(object):
	def __init__(self):
		self.images = None
		self.neutral = None
		self.peak = None

	def load(self, root_dir, pattern):
		'''
		Recursively loads filenames from root_dir matching pattern
			OUTPUT: list
		'''
		files = []
		for root, dirnames, filenames in os.walk(root_dir):
			for filename in fnmatch.filter(filenames, pattern):
				self.images.append(os.path.join(root, filename))
		return files

	def load_all(self, root_dir):
		self.images = self.load(root_dir, '*.png')

	def load_neutral(self, root_dir):
		self.neutral = self.load(root_dir, '*01.png')

	def load_peaks(self, root_dir):
		self.peak = []
		for root, dirnames, filenames in os.walk(root_dir):
			for filename in fnmatch.filter(filenames, '*01.png'):
				self.images.append(os.path.join(root, filename))