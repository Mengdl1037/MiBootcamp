# Question And Solve

## 生成多个密钥并将密钥对应到不同用户

本地使用了新的github用户，需要重新配置ssh和远程仓库的连接，方式如下。

1. 在使用 ssh-keygen 命令时自行设置文件名

2. 移除全局设置

    ```
    git config --global --unset user.name
    git config --global --unset user.email
    git config --global --unset user.password

    git config --global user.name
    git config --global user.email
    git config --global user.password

    git config --list
    ```

3. 配置 ~/.ssh/config 文件

    ```
    # 配置1
    Host user1.github.com
    HostName github.com
    IdentityFile ~/.ssh/id_rsa1
    PreferredAuthentications publickey
    User user1

    # 配置2
    Host user2.github.com
    HostName github.com
    IdentityFile ~/.ssh/id_rsa2
    PreferredAuthentications publickey
    User user2
    ```

    ```
    # 只对当前bash生效
    ssh-agent bash
    ssh-add ~/.ssh/id_rsa2
    ```

4. 测试连接

    ```
    ssh -T git@user1.github.com
    ssh -T git@user2.github.com
    ```

5. 分别设置用户

    ```
    git config user.name "user1"
    git config user.email "user1@email.com"
    ```

## 区分 pull 和 fetch

- Git Pull
git pull命令是一个高层次的命令，它相当于git fetch和git merge两个命令的组合。简而言之，git pull用于从远程仓库拉取更新并将它们合并到当前分支。
```git pull <remote> <branch>```
这个命令会从指定的远程仓库（remote）拉取指定分支（branch）的更新，然后将这些更新合并到当前所在的分支。

- Git Fetch
git fetch命令则是用于从远程仓库获取更新，但它不会自动合并到当前分支。相反，它将获取的更新保存在本地，让你可以在需要的时候进行合并操作。
```git fetch <remote> <branch>```
与git pull不同，git fetch只会将远程仓库的更新下载到本地，并不会直接影响当前分支。这为开发者提供了更多的控制权，可以在合适的时机进行合并。

## apt包管理

```
# 列出所有可更新的软件清单命令：
sudo apt update

# 升级软件包：
sudo apt upgrade

# 列出可更新的软件包及版本信息：
apt list --upgradeable

# 升级软件包，升级前先删除需要更新软件包：
sudo apt full-upgrade

# 安装指定的软件命令：
sudo apt install <package_name>

# 安装多个软件包：
sudo apt install <package_1> <package_2> <package_3>

# 更新指定的软件命令：
sudo apt update <package_name>

# 显示软件包具体信息,例如：版本号，安装大小，依赖关系等等：
sudo apt show <package_name>

# 删除软件包命令：
sudo apt remove <package_name>

# 清理不再使用的依赖和库文件: 
sudo apt autoremove

# 移除软件包及配置文件: 
sudo apt purge <package_name>

# 查找软件包命令： 
sudo apt search <keyword>

# 列出所有已安装的包：
apt list --installed

# 列出所有已安装的包的版本信息：
apt list --all-versions
```
