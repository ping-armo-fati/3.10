# OneNote导出成Markdown文件

## Dependence
- pandoc
- requirements 

```bash
pip install -r requirements.txt
```

## 步骤
- 打开OneNote及相关笔记本
> （注意，需要是OneNote 2016，不能是OneNote For Win10之类的版本，详情查看 https://support.microsoft.com/zh-cn/office/onenote-%E7%89%88%E6%9C%AC%E6%9C%89%E4%BD%95%E5%8C%BA%E5%88%AB-a624e692-b78b-4c09-b07f-46181958118f ）

- 运行代码
> （代码里有个 ASSETS_DIR 变量，是图片存放路径。如果你在obsidian里有相关设置，可以修改这个变量）

```bash
# One Note  to MD files
python convert.py
# MD files Editor : change img path ; delete used img ; rename img
python markdown_image_editor.py
# Markdown system index create for MkDocs
python MkDocs_index_system_create.py
```

- 你的笔记应该转化成了markdown文件并存在 `~/Desktop/OneNoteExport`. 建议用[obsidian](https://obsidian.md)管理markdown笔记！

## 开发日志

### 整体任务描述

- MarkDown文件系统架构

```commandline
    Docs
    ├─Sub1
    │  ├─Tribe1
    │  │      file1.md
    │  │      file2.md
    │  │      file3.md
    │  │      file4.md
    │  │      file5.md
    │  ├─Tribe2
    │  └─Tribe3
    ├─Sub2
    ├─Sub3
    └─Sub4
```

- 操作过程
  - 首先创建最低级目录索引-`index.md-Tribe*`位于每一个Tribe下
  - 再创建次级目录索引-`index.md-Sub*`位于每一个Sub下
  - 之后创建顶级索引-`nav.yaml`位于Docs根下
- 索引 or 导航 文件结构
  - `Tribe:index.md`
    ```markdown
    # Tribe
      - [xyz](xyz.md)
      - [xyz1](xyz1.md)
      -
    ```
        
  - `Sub:index.md`
    ```markdown
    # Sub
    - [Tribe1](Tribe1/index.md)
    - [Tribe2](Tribe2/index.md)
    ****
    ****
    # OverView
    ****
    ****    
    ## Tirbe1
    - [xyz](Tribe1/index.md)
    - [xyz1](Tribe1/index.md)
    - 
    ```

  - `nav.yaml`
    ```yaml
    - nav:
      - Home: index.md
      - sub1: 
        - Contents: sub1/index.md
        - Tribe1: sub1/Tribe1/index.md
    ............. 
    ```

  - `docs:index.md`
    ```markdown
    # Home
    
    ****
    ## [Sub1](Sub1/index.md)
    ## [Sub2](Sub2/index.md)
    ......
    ```

##  Reference

这部分代码来自 https://github.com/pagekeytech/onenote-to-markdown 。
喜欢用powershell脚本的朋友可以使用仓库中的 convert3.ps1 脚本。

##  Issues

部分OneNote笔记的笔记名包含特殊字符，可能转换失败。
因为目标格式是markdown并且以文件、文件夹格式存储，
必然受到操作系统对文件名的限制。对于这种情况，我的建议是以后不要在标题里用特殊字符。

- 目前函数`rename_image_files_by_alt_text(root_dir, assets_path)` 重命名还存在Bug 需要修改，暂时 注释掉
- 