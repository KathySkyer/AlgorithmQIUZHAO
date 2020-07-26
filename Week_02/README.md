学习笔记

1、树的面试题都是递归的，原因：
 1.1 节点的定义
 1.2 重复性


2、递归步骤：
2.1 递归终止条件
2.2 处理当前层逻辑
2.3 下探到下一层
2.4 清理当前层


3、二叉堆性质：
3.1 通过完全二叉树实现
3.2 树中的任意节点的值>=其子节点的值
3.3 通过数组实现


Noted:
不要人肉递归
找最近最简子问题
数学归纳法


# Python
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 
    process(level, data...) 
    # drill down 
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed



155.最小栈
没有思路，对栈还是只停留在概念里面，python对于栈的使用还是有点懵逼。。
就把题解记下来了

239.滑动窗口最大值
暴力：python切片，然后找最大，超时了。。。
题解：队列，动态规划什么的。。感觉不是难理解，但是自己写的话要注意的地方特别多。。。
然后看见一个比较独特的见解，代码简短，应该是动态规划的一些改进思路，记住了下来。。。


offer40：最小的K个数：
sort直接排序，然后取出来（通过了，哈哈哈。。）

84. 柱状图中的最大矩形：

丑数：
暴力，就一个一个算，尝试完，就是当n=2时，结果不对，然后一直没有调试出来，所以放弃
动态规划：思路很巧妙，先用归纳法总结出2，3，5与丑数之间的关系，用数学归纳法得出结果








