学习笔记

LRU Cache应用
1、比特币网络
2、分布式系统
3、Redis缓存
4、垃圾邮件、评论等的过滤
# Python 
from bitarray import bitarray 
import mmh3 
class BloomFilter: 
	def __init__(self, size, hash_num): 
		self.size = size 
		self.hash_num = hash_num 
		self.bit_array = bitarray(size) 
		self.bit_array.setall(0) 
	def add(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			self.bit_array[result] = 1 
	def lookup(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			if self.bit_array[result] == 0: 
				return "Nope" 
		return "Probably" 
bf = BloomFilter(500000, 7) 
bf.add("dantezhao") 
print (bf.lookup("dantezhao")) 
print (bf.lookup("yyj")) 


比较类排序：通过比较来决定元素间的相对次序，由于其时间复杂度不能突破nlogn,因此也称为非线性时间比较类排序
（交换排序，插入，选择，归并）
非比较类排序：不通过比较来决定元素间相对次序，可以突破基于比较排序的时间下届，以线性时间运行，因此也称为线性时间非比较类排序
（计数，桶，基数排序）

1、选择排序：每次找到最小值，然后放到待拍讯数组的起始位置
2、插入排序：从前往后逐步后加有序序列，对于排序的数据，在已排序的序列中从后往前扫描，找到相应位置并插入
3、冒泡排序：嵌套循环，每次查看相邻的元素，如果逆序，则交换
4、快排：数组取标杆pivot，将小元素放在pivot做欧变，大元素放在右侧，然后依次对右边和右边的字数组继续快排，已达到整个序列有序。
5、计数排序：将输入的数据值转换为键存储在额外的数组空间中，然后依次把计数大于1的填充回原数组
6、桶排序：假设输入数据服从均匀分布，将数据分到有限数量的痛里，每个桶再分别排序
7、基数排序：按照低位先排序，然后收集；再按照高位排序，在收集，依次类推，直到最高位。有时候有些属性是具有优先级排序的，先按低优先排序，再按高位优先排序




