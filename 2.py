# 适配所有Ultralytics版本的配置定位代码
from ultralytics import YOLO
from ultralytics.data.utils import check_dataset
import os

# 核心：直接解析voc.yaml的真实路径和配置
def find_real_voc_yaml():
    # 1. 强制检查dataset，返回配置详情
    data_dict = check_dataset('voc.yaml')
    # 2. 提取关键信息
    real_yaml_path = data_dict.get('yaml_file', '未找到')
    real_path_field = data_dict.get('path', '未找到')
    test_path = os.path.join(real_path_field, 'images/test2007')
    
    # 3. 打印结果（核心！）
    print('='*60)
    print(f'✅ 实际调用的voc.yaml文件路径：{real_yaml_path}')
    print(f'✅ voc.yaml中配置的path字段：{real_path_field}')
    print(f'✅ 拼接后的test数据集路径：{test_path}')
    print('='*60)
    
    # 4. 验证该文件是否存在
    if os.path.exists(real_yaml_path):
        print(f'✅ 配置文件存在，文件内容预览：')
        with open(real_yaml_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()[:10]  # 只看前10行
            for line in lines:
                print(line.strip())
    else:
        print(f'❌ 配置文件不存在，可能是缓存路径！')

if __name__ == '__main__':
    find_real_voc_yaml()