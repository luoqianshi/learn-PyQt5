from xml.etree import ElementTree
'''
ElementTree 是 Python 标准库中用于解析和操作 XML 的模块。
它提供了一种简单的方式来解析 XML 数据并构建 XML 树结构，以便对 XML 数据进行操作。
'''
from xml.etree.ElementTree import Element, SubElement
'''
Element 和 SubElement 是 ElementTree 模块中的类，用于创建 XML 元素和子元素。
Element 用于创建 XML 元素，SubElement 用于创建 XML 元素的子元素。
'''
from lxml import etree
'''
lxml 是一个功能强大且易于使用的 XML 处理库，它是基于 libxml2 和 libxslt 库的 Python 绑定。
lxml.etree 模块提供了高性能的 XML 解析和处理功能，支持 XPath 查询、XSLT 转换等功能。
'''

# 使用 ElementTree 创建 XML 元素
root = Element('root')
child1 = SubElement(root, 'child1')
child2 = SubElement(root, 'child2')
child1.text = 'Hello'
child2.text = 'World'

# 打印 XML 结构
xml_str = ElementTree.tostring(root).decode()
print(xml_str)

# 使用 lxml 解析 XML 数据

# 解析 XML 字符串
root = etree.fromstring(xml_str)

# 遍历 XML 元素
for element in root:
    print(element.tag, element.text)
