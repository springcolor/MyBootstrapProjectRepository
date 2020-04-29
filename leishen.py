# 这道题想必大家在面试或者练习时都遇到过，是一道经典的Python笔试题，主要考察的是对python标准库的基本使用。之所以说是详解，并不是着重说代码而是对于os模块操作的一个思路。
# os模块介绍
#
# operating system 用于访问操作系统功能的模块
# os模块的基本方法
#
# os.getcwd(): 查看当前所在路径
# os.listdir(path): 列举目录下的所有文件（包含目录）,返回一个列表
# os.path.abspsth(path): 返回目录的绝对路径
# os.path.split(path): 将路径分为文件夹、文件名
# os.path.join(path1,path2): 将路径进行组合
# os.mkdir() 创建一个空目录
# os.rmdir() 删除一个空目录
# os.makedirs() 生成多层递归目录。
# os.removedirs(dirname) 删除多层递归空目录
# os.rename() 修改目录名或者文件名
# os.path.exists(path): 判断文件或者目录是否存在
# os.path.isfile(path): 判断是否为文件 os.path.isdir(path): 判断是否为目录 这两个方法返回的都是True或者False 所以记住一个和 os.path.exists则可以判断目录或者文件夹了
# os.path.getsize(name):获得绝对路径
# 大概就是这些方法了，其他方法可以去官方文档细致的查看。
#     再这里再啰嗦一下,os模块真的很简单，语法以及方法的命名都十分的简洁且易理解。但是os模块却是十分之重要的,无论是初学者还是开发人员都应该把上述最简单的os模块给熟记，命令很少找几个时间点花个十分钟记住他吧。
# 解题思路
#
# 这道题的解题思路同样十分的简单，无非就是经典的三步走。
# 数据输入: 这里面则是获取当前目录以及子目录下的所有文件或目录的名字
# 数据处理:判断名字是否为文件，再判断名称是否包含指定的字符串
# 数据输出:确定了包含指定字符串的文件,然后输出其相对/绝对路径
# 具体实现
#
# 先实现第一步，获取当前目录以及子目录下的所有文件或目录的名字。
# 这一步很简单，通过简单的递归就能实现。具体代码如下:

# -*- coding: utf-8 -*
import os
Path = r"C:\Users\use\Desktop\2019-12-31"
path = r"C:\Users\Admin\Desktop\a\f1"
str = "5"
pwd = os.getcwd()
Aggregate_list = []


def search_file(path, str, other):  # other传-1时为相对路径，否则为相对路径
    for file in os.listdir(path):
        this_path = os.path.join(path, file)
        if os.path.isfile(this_path):
            if this_path.find(str) != -1:
                if other == -1:
                    the_path = this_path.replace(Path, "")[1:]
                    Aggregate_list.append(the_path)
                else:
                    Aggregate_list.append(this_path)
        else:
            search_file(this_path, str, 1)
    return Aggregate_list


print(search_file(path, str, 1))
print('新建 XLSX 工作表.xlsx')