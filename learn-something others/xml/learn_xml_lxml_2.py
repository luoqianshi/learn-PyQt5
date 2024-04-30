from xml.etree import ElementTree

from lxml import etree

def readXML():
    # 读取已有的 XML 标注文件
    tree = ElementTree.parse(r'annotation/test.xml')
    root = tree.getroot()

    # 提取目标检测标注信息
    for obj in root.findall('object'):
        name = obj.find('name').text
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)

        print(f"Object: {name}, Bounding Box: ({xmin}, {ymin}, {xmax}, {ymax})")


def writeXML(filepath):

    # 创建 XML 结构
    root = etree.Element('annotation')
    filename = etree.SubElement(root, 'filename')
    filename.text = 'image1.jpg'

    # 添加目标检测信息
    object1 = etree.SubElement(root, 'object')
    name = etree.SubElement(object1, 'name')
    name.text = 'car'
    bndbox = etree.SubElement(object1, 'bndbox')
    xmin = etree.SubElement(bndbox, 'xmin')
    xmin.text = '100'
    ymin = etree.SubElement(bndbox, 'ymin')
    ymin.text = '50'
    xmax = etree.SubElement(bndbox, 'xmax')
    xmax.text = '200'
    ymax = etree.SubElement(bndbox, 'ymax')
    ymax.text = '150'

    # 将 XML 结构写入文件
    xml_str = etree.tostring(root, pretty_print=True).decode()
    with open(filepath, 'w') as f:
        f.write(xml_str)


if __name__ == '__main__':
    filepath = r'annotation/new_annotation.xml'
    # readXML()
    writeXML(filepath)