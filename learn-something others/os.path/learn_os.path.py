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

'''
6. os.path.splitext()
`os.path.splitext()`方法用于分割文件路径，获取文件名（包含前置路径）和拓展名
'''
# 分割文件路径，获取文件名和扩展名
path = '/path/to/file.txt'
filename, extension = os.path.splitext(path)

print(f'文件名: {filename}')
print(f'扩展名: {extension}')

'''
7. str.endwith()
'''
file_path = '/path/to/file.txt'

# 检查文件路径是否以指定后缀结尾
if file_path.endswith('.txt'):
    print(f'{file_path} 是以 .txt 结尾的文件路径')
else:
    print(f'{file_path} 不是以 .txt 结尾的文件路径')