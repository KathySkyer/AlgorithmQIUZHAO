学习笔记

DFS(python)
递归：
visited = set()
def DFS(node, visited):
    if node in visited:
       return 
       visited.add(node)
       for node_next in node.children():
           if node_next not in visited:
	       DFS(node_next,visited)
非递归（维护一个栈）
def DFS(self,tree)
    if tree.node is None:return []
    visited, stack = [],[tree.root]
    while stack:
          stack.pop()
	  stack.add(node)
	  process(node)
	  nodes = generated_related_nodes(node)
	  stack.push(nodes)
BFS(python)
def BFS(graph,start,end):
      visited = set()
      queue = []
      queue.append(start)
      while queue:
               node = queue.pop()
               visited.add(node)
               process(node)
               nodes = generate_related_nodes(node)
               queue.push(nodes)


392.判断子序列
暴力解法：遍历字符串s（因为已经限制了序列长度，所以不需要判断s和t的长度问题），同时记录下标


前中后遍历树：
用深度优先的方式：
前：
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
          def dfs(cur):
                if not cur:return 
                res.append(cur.val)
	dfs(cur.left)
	dfs(cur.right)
          res =[]
          dfs(root)
          return res
中：
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
           def dfs(cur):
                 if not cur:return
	 dfs(cur.left)
	 res.append(cur.val)
	 dfs(cur.right)
           res =[]
           dfs(root)
           return res
后：
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
          def dfs(cur):
                if not cur:return 
                dfs(cur.left)
                dfs(cur.right)
                res.append(cur.val)
          res=[]
          dfs(root)
          return res
二分查找模板：(先分析能用二分查找的原因，单调递增且有上下界)
left, right = 0, len(array) - 1
while left<=right:
         mid = (left + right) /2
         if array[mid] == target：
             break or return result
         elif array[left] < target:
             left =mid + 1
         else: right = mid - 1


贪心与动态规划的区别：贪心对每个子问题的解决方案都作出选择，不能回退。而动态规划则保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。
贪心：当下做局部最优判断
回溯：能够回退
动态规划：最优判断+回退

122.买卖股票最佳时机：
贪心：通过。。。
455.分发饼干
一个一个比较，只想到了总数，没有想到每一个对比，哎。。


50.pow(x,n)
暴力求解：我又超时了，哎
乖乖看视频，记下来

169.多数元素
想到了字典。所以我又偷懒了，直接用Counter，通过了
题解里面有个排序然后取众数的思想很不错。。。






