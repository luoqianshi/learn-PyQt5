from PIL import Image

# 加载图像
image = Image.open('image.jpg')

# 显示图像信息
print('Format:', image.format)  # 图像格式
print('Size:', image.size)      # 图像大小
print('Mode:', image.mode)      # 图像模式

# 显示图像
image.show()

# 旋转图像
# rotated_image = image.rotate(45)
# rotated_image.show()

# # 保存旋转后的图像
# rotated_image.save('rotated_image.jpg')