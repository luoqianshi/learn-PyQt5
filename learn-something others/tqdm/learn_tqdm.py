from tqdm import tqdm
import time

# 创建一个进度条，循环100次
for i in tqdm(range(100)):
    time.sleep(0.1)  # 模拟任务