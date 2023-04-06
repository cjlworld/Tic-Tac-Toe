# 一个基于 Flask 实现的博客系统

开坑！ 2023/4/5

### Python 构建虚拟环境

官方文档：[venv --- 创建虚拟环境 — Python 3.11.3 文档](https://docs.python.org/zh-cn/3/library/venv.html) 

#### 创建虚拟环境

GPT：

> python 在 a-blog-system 文件夹（项目）下 怎么 搭建虚拟环境

好的，如果您希望使用 Python 自带的 venv 模块来创建虚拟环境，您可以按照以下步骤进行操作：

1. 确认已经安装了 Python：在命令行终端中输入 `python --version`，如果返回 Python 版本信息，则表示已经安装了 Python。

2. 进入 a-blog-system 项目文件夹：在命令行终端中使用 `cd` 命令切换到 a-blog-system 项目文件夹的路径下。

3. 创建虚拟环境：在命令行终端中输入 `python -m venv venv`，其中 `venv` 是虚拟环境的名称，您也可以选择其他名称。

4. 激活虚拟环境：在命令行终端中输入 `venv\Scripts\activate`（在 Windows 上）或 `source venv/bin/activate`（在 Linux 或 macOS 上）。

5. 在虚拟环境中安装所需的 Python 模块：在虚拟环境中使用 `pip` 命令安装所需的 Python 模块，例如 `pip install Flask`。

完成以上步骤后，您就可以在 a-blog-system 项目文件夹中使用虚拟环境来运行 Python 程序了。当您完成工作时，可以使用 `deactivate` 命令退出虚拟环境。

---

Vscode：

也可以在 vscode 中操作，控制栏输入 `>python` 点击 `Python:创建环境` 即可。

#### 激活环境

Windows 在项目文件夹下

```powershell
./.venv/Scripts/activate
```

[windows 终端无法加载文件 Scripts\Activate.ps1，因为在此系统上禁止运行脚本-更改执行策略 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/484073745) 

若出现 禁止运行脚本，则

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

然后再次激活即可。
