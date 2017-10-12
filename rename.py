# coding: utf8
# @Author: 杨振宇
# @File: rename.py
# @Time: 2017/10/11
# @blog: http://blog.csdn.net/u010300028
# @Description: 对指定文件夹下的文件批量的添加编号，便于查看记录

import os
import re

path = input('请输入文件路径(结尾加上/)：')


def addNumToFile(path):
    # 获取该目录下所有文件，存入列表中
    f = os.listdir(path)

    n = 0
    for i in f:
        filepath = os.path.join(path, i + '/')
        if os.path.isdir(filepath):
            addNumToFile(filepath)  # 递归遍历嵌套文件夹
            continue   # 文件夹不编号
        print(i, sep=' ', end='\n')
        # 设置旧文件名（就是路径+文件名）
        oldname = path + i
        # 判断此文件名是否以#开头
        if(i[0] == '#'):
            # 若以#开头，则提取#后数字，并保存（默认除编号外，文件名中无其他数字）
            n = int(re.sub("\D", "", i))
            continue
        # 设置新文件名
        newname = path + '#' + str(n + 1) + ' ' + i

        # 用os模块中的rename方法对文件改名
        os.rename(oldname, newname)
        n += 1


addNumToFile(path)
