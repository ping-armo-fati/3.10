from pathlib import Path

# 指定你的顶级目录
docs_dir = Path('./MarkDown_Notes')


def tribe_idx_build(top_dir):
    # 遍历顶级目录下的所有子目录
    for sub_dir in top_dir.iterdir():
        if sub_dir.is_dir() and sub_dir.name != 'assets':
            # 在每个Sub*目录下的所有Tribe*目录中创建index.md文件

            for tribe_dir in sub_dir.iterdir():
                if tribe_dir.is_dir():
                    file_path = tribe_dir / 'index.md'
                    print(tribe_dir, ": create a index.md below")
                    file_path.touch(exist_ok=True)

                    # 打开文件并清空内容
                    with open(file_path, 'w', encoding='utf-8') as f:
                        pass
                    print(tribe_dir, ": index.md have been cleaned")

                    # 填写内容
                    with open(file_path, 'w', encoding='utf-8') as f:
                        tribe_dir_title = tribe_dir.name.split('.', 1)[-1]
                        f.write(f"# {tribe_dir_title}\n")
                        f.write("****\n")
                        f.write("****\n")
                        for file in tribe_dir.iterdir():
                            if file.suffix == '.md' and file != file_path:
                                # 去掉文件名中的数字和点的前缀
                                file_title = file.stem.split('.', 1)[-1]
                                f.write(f"  - [{file_title}]({file.stem}{file.suffix})\n")
                        f.write("****\n")
                print(tribe_dir.name, ":index.md built success")


def sub_idx_build(top_dir):
    for sub_dir in top_dir.iterdir():
        # 遍历每一个Sub文件
        if sub_dir.is_dir() and sub_dir.name != 'assets':
            # 在每个Sub*目录下创建index.md文件
            index_file_path = sub_dir / 'index.md'
            index_file_path.touch(exist_ok=True)
            # 打开文件并清空内容
            with open(index_file_path, 'w', encoding='utf-8') as f:
                pass
            print(sub_dir, ": index.md have been cleaned")
            # 写入内容
            sub_dir_title = sub_dir.name.split('.', 1)[-1]
            with open(index_file_path, 'w') as f:
                # 添加标题
                f.write(f"# {sub_dir_title}\n")
                f.write("****\n")
                f.write("****\n")
                # 在每个Sub*目录下的所有Tribe*目录中添加链接
                for tribe_dir in sub_dir.iterdir():
                    if tribe_dir.is_dir():
                        tribe_dir_title = tribe_dir.name.split('.', 1)[-1]
                        f.write(f"  - [{tribe_dir_title}]({tribe_dir.name}/index.md)\n")
                f.write("****\n")
            print(sub_dir.name, ":index.md built success")


def docs_idx_build(top_dir):
    # 创建目录文件
    index_file_path = top_dir / 'index.md'
    index_file_path.touch(exist_ok=True)
    # 打开文件并清空内容
    with open(index_file_path, 'w', encoding='utf-8') as f:
        pass
    print(top_dir, ": index.md have been cleaned")

    # 写入内容
    with open(index_file_path, 'w', encoding='utf-8') as f:
        # 添加标题
        f.write(f"# Home\n")
        f.write("****\n")
        f.write("****\n")
        # 在每个Sub*目录下的所有Tribe*目录中添加链接
        for sub_dir in top_dir.iterdir():
            if sub_dir.is_dir() and sub_dir.name != 'assets':
                sub_dir_title = sub_dir.name.split('.', 1)[-1]
                f.write(f"  - [{sub_dir_title}]({sub_dir.name}/index.md)\n")
        f.write("****\n")
    print(top_dir.name, ":index.md built success")


def yaml_nav_build(top_dir):
    # 创建目录文件
    yaml_file_path = top_dir / 'nav.yaml'
    yaml_file_path.touch(exist_ok=True)
    # 打开文件并清空内容
    with open(yaml_file_path, 'w', encoding='utf-8') as f:
        pass
    print(top_dir, ": nav.yaml have been cleaned")

    # 写入内容
    with open(yaml_file_path, 'w', encoding='utf-8') as f:
        # 添加标题
        f.write(f"nav:\n")
        f.write(f"  - Home: 'home.md'\n")
        f.write(f"  - Index: 'MarkDown_Notes/index.md'\n")
        # 在每个Sub*目录下的所有Tribe*目录中添加链接
        for sub_dir in top_dir.iterdir():
            if sub_dir.is_dir() and sub_dir.name != 'assets':
                sub_dir_title = sub_dir.name.split('.', 1)[-1]
                f.write(f"  - {sub_dir_title}: \n")
                f.write(f"    - Contents: 'MarkDown_Notes/{sub_dir.name}/index.md'\n")
                for tribe_dir in sub_dir.iterdir():
                    if tribe_dir.is_dir():
                        tribe_dir_title = tribe_dir.name.split('.', 1)[-1]
                        f.write(f"    - {tribe_dir_title}: 'MarkDown_Notes//{sub_dir.name}/{tribe_dir.name}/index.md'\n")
    print(top_dir.name, ":nav.yaml built success")


if __name__ == "__main__":
    tribe_idx_build(docs_dir)
    print("所有二级目录创建完成")
    sub_idx_build(docs_dir)
    print("所有一级目录创建完成")
    docs_idx_build(docs_dir)
    print("根目录创建完成")
    yaml_nav_build(docs_dir)

