import os
import time

file = r'D:\统一用户中心截图.rar'  # 文件路径

print(os.path.getatime(file))   # 输出最近访问时间
print(os.path.getctime(file))   # 输出文件创建时间
print(os.path.getmtime(file))   # 输出最近修改时间
print(time.gmtime(os.path.getmtime(file)))  # 以struct_time形式输出最近修改时间
print(os.path.getsize(file))   # 输出文件大小（字节为单位）
print(os.path.abspath(file))   # 输出绝对路径
print(os.path.normpath(file))  # 规范path字符串形式
line='My name is Lilong'

if 'long' in line:
    print(line)

print(line.upper())
print(line.lower())
print(line.isupper())
print(line.islower())
print(line.swapcase())
print(line.capitalize())
print(line.istitle())
print(line.startswith('My'))
print(line.endswith('Long'))

# print(os.path.basename('/root/runoob.txt'))   # 返回文件名
# print(os.path.dirname('/root/runoob.txt'))    # 返回目录路径
# print(os.path.split('/root/runoob.txt'))      # 分割文件名与路径
# print(os.path.join('root', 'test', 'runoob.txt'))  # 将目录和文件名合成一个路径
print(";".join(['a','b','c']))
splitstr="a:b:c:d:e"
print(splitstr.split(':'))
