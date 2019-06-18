#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 下面是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
' a test module '

__author__ = 'SmiteLi'

# 导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能
import sys

# 在交互环境导入模块后，这样运行函数：hello.test()
def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果
# 在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行
# 一些额外的代码，最常见的就是运行测试。
if __name__=='__main__':
    print(sys.path)
    test()
