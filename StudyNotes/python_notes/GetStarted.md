# Hello Python

## pyenv

- pyenv:

  - 管理 Python 版本： pyenv 是一个用于管理多个 Python 版本的工具。通过 pyenv，你可以轻松地在同一台机器上切换不同版本的 Python，以适应不同项目的需求。
  - 独立性： 每个项目可以有自己的 Python 版本，而不会影响全局的 Python 环境。这在项目需要不同 Python 版本的情况下非常有用。
  - 全局和局部配置： pyenv 支持全局 Python 版本的设置，也支持在项目级别进行配置。

- pipenv:

  - 虚拟环境管理： pipenv 是一个用于管理 Python 项目的依赖和虚拟环境的工具。它使用 Pipfile 和 Pipfile.lock 来定义项目的依赖关系。
  - 自动化： pipenv 可以自动创建和管理虚拟环境，同时记录项目的依赖版本。这使得在不同环境之间共享项目变得更加简单。
  - 清晰的依赖关系： pipenv 通过清晰的依赖关系图和版本锁定，确保了项目的依赖关系的可重现性。

### 安装 pyenv

```
# 安装
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
cd ~/.pyenv && src/configure && make -C src

# 配置环境 
## ~/.bashrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

## ~/.profile
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
echo 'eval "$(pyenv init -)"' >> ~/.profile

## ~/.bash_profile
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```

### wsl2 设置

<https://learn.microsoft.com/en-us/windows/wsl/wsl-config#wslconfig>

```
# wsl2 中可以将 Windows 的环境变量移除，防止冲突
# 编辑 Windows 的 C:/User/Username/.wslconfig 
# 添加
[interop]
enabled=false
appendWindowsPath=false
```

### pyenv 基本指令

```
# 查看当前 Python 版本
pyenv version

# 查看全部 Python 版本
pyenv versions

# 查看可安装 Python 版本
pyenv install --list

# 安装指定版本 Python
pyenv install 3.7.9

# 卸载指定版本 Python
pyenv uninstall 3.7.9

# 切换 Python 版本
pyenv global 3.10.9
pyenv global 3.6.5 2.7.14

# 切换 Python 版本
pyenv local 3.10.9

# 重建环境变量，每次增删 Python 版本或带有可执行文件的包（如 pip）都应当使用此命令
pyenv rehash

# 设置 pip 的默认镜像源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 安装 Python

```
# 可以先去下载 Python 的安装包
wget https://registry.npmmirror.com/-/binary/python/3.11.9/Python-3.11.9.tar.xz -P ~/.pyenv/cache

# 然后进行安装
pyenv install 3.11.9
```

```
# 安装前可能需要的一些包和依赖库
sudo apt update
sudo apt upgrade
sudo apt install build-essential
sudo apt install libssl-dev libffi-dev libncurses5-dev zlib1g zlib1g-dev libreadline-dev libbz2-dev libsqlite3-dev make gcc
sudo apt-get install liblzma-dev
```

## pipenv

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pipenv
```

## pyenv-virtualenv

```
git clone https://github.com/pyenv/pyenv-virtualenv.git $PYENV_ROOT/plugins/pyenv-virtualenv
```

## conda

### conda 安装

```
#下载Miniconda安装脚本
#官网下载地址 https://repo.anaconda.com/miniconda/
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

#运行安装脚本
sh Miniconda3-latest-Linux-x86_64.sh

#检查安装是否成功
conda --version
```

### conda 基本命令 

```
#创建虚拟环境
conda create -n your_env_name python=X.X（3.6、3.7等）
 
#激活虚拟环境
source activate your_env_name(虚拟环境名称)
 
#退出虚拟环境
source deactivate your_env_name(虚拟环境名称)
 
#删除虚拟环境
conda remove -n your_env_name(虚拟环境名称) --all
 
#查看安装了哪些包
conda list
 
#安装包
conda install package_name(包名)
conda install scrapy==1.3 # 安装指定版本的包
conda install -n 环境名 包名 # 在conda指定的某个环境中安装包
 
#查看当前存在哪些虚拟环境
conda env list 
#或 
conda info -e
#或
conda info --envs
 
#检查更新当前conda
conda update conda
 
#更新anaconda
conda update anaconda
 
#更新所有库
conda update --all
 
#更新python
conda update python
```