import os
import re


root_dir = r"/MDEditor_OneNote2MD\file_source"
assets_path = r"/MDEditor_OneNote2MD\file_source\assets"
markdown_image_pattern = r'!\[(.*?)\]\((.*?)\)'


def process_markdown_files(root_dir_input, assets_path_input):
    # 重新匹配所有图片的相对路径
    print(os.path.isdir(root_dir_input))
    for root, dirs, files in os.walk(root_dir_input):
        for file in files:
            if file.endswith('.md'):
                print("find the " + file)
                full_path = os.path.join(root, file)
                with open(full_path, 'r', encoding='utf-8') as file_con:
                    content = file_con.read()
                    print(f"读取了文件 {file}")
                    # 查找所有的图片表达式
                    img_expression = re.findall(markdown_image_pattern, content)
                    # 遍历所有的图片表达式
                    for expr in img_expression:
                        print(f"查找到图片链接 {expr}")
                        # 获取图片文件名，并去掉相对和绝对路径
                        img_filename = os.path.basename(expr[1])
                        # 求相对路径
                        relative_path_to_assets = relative_path(assets_path_input, root)
                        # 拼接新的路径和图片文件名
                        new_img_expr = os.path.join(relative_path_to_assets, img_filename)
                        print(f"修改为 {new_img_expr}")
                        # 将原图片表达式替换为新的图片表达式
                        content = content.replace(expr[1], new_img_expr)
                        # 将修改后的内容写回文件
                        with open(full_path, 'w', encoding='utf-8') as file_done:
                            file_done.write(content)
                            print(f"完成写入 {file_done}")


def clean_unused_images(root_dir_input, assets_path_input):
    # 清除无效图片
    used_images = set()

    # Step 1: Traverse all markdown files and collect used images
    for root, dirs, files in os.walk(root_dir_input):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                with open(full_path, 'r', encoding='utf-8') as file_con:
                    content = file_con.read()
                    img_expression = re.findall(markdown_image_pattern, content)
                    for expr in img_expression:
                        img_filename = os.path.basename(expr[1])
                        used_images.add(img_filename)
                        print(f"find a used image: {img_filename}")

    # Step 2: Traverse the assets directory and remove unused images
    for root, dirs, files in os.walk(assets_path_input):
        for file in files:
            if file not in used_images:
                full_path = os.path.join(root, file)
                os.remove(full_path)
                print(f"Removed unused image: {full_path}")


def rename_image_files_by_alt_text(root_dir_input, assets_path_input):
    print(os.path.isdir(root_dir_input))
    img_counter = 1
    for root, dirs, files in os.walk(root_dir_input):
        for file in files:
            if file.endswith('.md'):
                print("find the " + file)
                full_path = os.path.join(root, file)
                with open(full_path, 'r', encoding='utf-8') as file_con:
                    content = file_con.read()
                    print(f"读取了文件 {file}")
                    # 查找所有的图片表达式
                    img_expression = re.findall(markdown_image_pattern, content)
                    # 遍历所有的图片表达式
                    for expr in img_expression:
                        print(f"查找到图片链接 {expr}")
                        # 获取图片文件名，并去掉相对和绝对路径
                        img_filename = os.path.basename(expr[1])
                        # 获取方括号中的文本
                        alt_text = expr[0]
                        # 求相对路径
                        relative_path_to_assets = relative_path(assets_path_input, root)
                        # 修改图片文件名为 方括号中的文本+原图片文件后缀
                        new_img_filename = str(img_counter) + "_" + alt_text + os.path.splitext(img_filename)[1]
                        img_counter += 1
                        # 修改图片的url为修改名字后 对应的url
                        new_img_url = os.path.join(relative_path_to_assets, new_img_filename)
                        # 重命名图片文件
                        os.rename(os.path.join(assets_path_input, img_filename),
                                  os.path.join(assets_path_input, new_img_filename))
                        print(f"修改为 {new_img_filename}")
                        # 将原图片表达式替换为新的图片表达式
                        content = content.replace(expr[1], new_img_url)
                        # 将修改后的内容写回文件
                        with open(full_path, 'w', encoding='utf-8') as file_done:
                            file_done.write(content)
                            print(f"完成写入 {file_done}")


def relative_path(target_path_input, reference_path_input):
    # 正确 ： .md 跟png在同一个文件夹下时候，.md 与 image存在一个../ ，root 与图片同一路径
    # 参考：F:\pycharm\project\3.10\MDEditor_OneNote2MD\file_source\4.具体工作\2.Mujoco\c.石块几何
    # 目标：F:\pycharm\project\3.10\MDEditor_OneNote2MD\file_source\assets
    # 相对路径计算..\..\..\assets
    # 错误
    # 参考路径F:\pycharm\project\3.10\MDEditor_OneNote2MD\file_source\4.具体工作\2.Mujoco\c.石块几何\几何库安装建立.md
    # 目标路径F:\pycharm\project\3.10\MDEditor_OneNote2MD\file_source\assets
    # 相对路径计算..\..\..\..\assets
    # 明显计算错误了 多计算了一个../
    relative_path_1 = os.path.relpath(target_path_input, reference_path_input)
    # print("相对路径计算" + reference_path_input)
    # print("相对路径计算" + target_path_input)
    # print("相对路径计算" + relative_path_1)
    return relative_path_1

# 打印当前工作目录
# print(os.getcwd())
#  打印文件的绝对路径
# print(os.path.abspath('./data/files'))


# Main
# run it！
# process_markdown_files(root_dir, assets_path)
# clean_unused_images(root_dir, assets_path)
# rename_image_files_by_alt_text(root_dir, assets_path)
