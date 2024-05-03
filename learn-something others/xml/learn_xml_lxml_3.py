from lxml import etree

# 创建一个 XMLParser 对象
parser = etree.XMLParser(encoding='utf-8')

# 解析 XML 文件
xml_tree = etree.parse(r'./annotation/test.xml', parser=parser)

# 获取根元素
root = xml_tree.getroot()

# 遍历并打印子元素
for child in root:
    print(child.tag)