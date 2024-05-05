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
python convert.py
```

- 你的笔记应该转化成了markdown文件并存在 `~/Desktop/OneNoteExport`. 建议用[obsidian](https://obsidian.md)管理markdown笔记！

# Reference

这部分代码来自 https://github.com/pagekeytech/onenote-to-markdown 。
喜欢用powershell脚本的朋友可以使用仓库中的 convert3.ps1 脚本。

# 已知问题

部分OneNote笔记的笔记名包含特殊字符，可能转换失败。因为目标格式是markdown并且以文件、文件夹格式存储，必然受到操作系统对文件名的限制。对于这种情况，我的建议是以后不要在标题里用特殊字符。
