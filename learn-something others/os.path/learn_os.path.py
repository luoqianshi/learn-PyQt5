import os


'''
1. `os.path.join()`
`os.path.join()` 方法用于将多个路径组合成一个路径。它会根据操作系统的规则正确地拼接路径。
'''
# 将多个路径组合成一个路径
path = os.path.join('folder', 'subfolder', 'file.txt')
print(path)

'''
2. `os.path.basename()`
`os.path.basename()` 方法用于获取路径中的文件名部分。
'''

# 获取路径中的文件名部分
filename = os.path.basename('/path/to/file.txt')
print(filename)

'''
3. `os.path.dirname()`
`os.path.dirname()` 方法用于获取路径中的目录部分。
'''
# 获取路径中的目录部分
dirname = os.path.dirname('/path/to/file.txt')
print(dirname)

'''
4. `os.path.exists()`
`os.path.exists()` 方法用于检查路径是否存在。
'''

# 检查路径是否存在
path = './path/to/file.txt'
if os.path.exists(path):
    print(f'{path} 存在')
else:
    print(f'{path} 不存在')

'''
5. `os.path.isfile()`
`os.path.isfile()` 方法用于检查路径是否为文件。
'''

# 检查路径是否为文件
path = './path/to/file.txt'
if os.path.isfile(path):
    print(f'{path} 是一个文件')
else:
    print(f'{path} 不是一个文件')