import os
from pathlib import Path

# 指定你的顶级目录
top_dir = Path('path_to_your_directory')


def create_tribe_idx():
    # 遍历顶级目录下的所有子目录
    for sub_dir in top_dir.iterdir():
        if sub_dir.is_dir() and 'Sub' in sub_dir.name:
            # 在每个Sub*目录下的所有Tribe*目录中创建index.md文件
            for tribe_dir in sub_dir.iterdir():
                if tribe_dir.is_dir() and 'Tribe' in tribe_dir.name:
                    file_path = tribe_dir / 'index.md'
                    file_path.touch(exist_ok=True)
