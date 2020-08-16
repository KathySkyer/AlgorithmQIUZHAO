学习笔记
1、Tries树基本性质：
（1）节点本身不存在完整单词
（2）从从根结点到某一结点，路径上进过的字符连起来，为该结点对应的字符串
（3）每个结点的所有子结点路径代表的字符都不相同


python实现Trie:
class: Trie(object):
	def  __init__(self):
	      self.root ={}
	      self.end_of _word ="#"
	def insert(self,word):
	      node = self.root
	      for char in word:
	            node = node.setdefault(char,{})
	      node[self.end_of_word]=self.end_of _word 
	def search(self,word):
	      node = self.node
	      for char in word:
	           if char not in node:
	              return False
	           node = node[char]
	       return self.end_of_word in node
	def starsWith(self,prefix):
	      node = self.root
	      for char in prefix:
	           if char not in node:
	              return False
	           node = node[char]
	      return True


AVL树
平衡因子：是左子树的高度减去右子树的高度
通过旋转操作达到平衡
每一个结点存balance factor（缺点：结点需要存储额外信息，且调整次数频率）
红黑树：是一种近似平衡的二叉搜索树，能够确保任何一个结点的右左右子树的高度小于两倍
特点：每个结点非黑即红
根结点是黑色
每一个叶子结点是黑色
不能有相邻接的两个红色结点
