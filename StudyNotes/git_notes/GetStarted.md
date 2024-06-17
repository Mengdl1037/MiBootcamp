# Hello Git

## 基础配置

### 配置别名 git-log

```
touch ~/.bashrc
vim ~/.bashrc
alias git-log='git log --pretty=oneline --all --graph --abbrev-commit'
alias ll='ls -al'
source ~/.bashrc
```

## 基础命令

下面这个图可以帮助理解命令是如何改变文件的状态的。

<div align = center> <img src = "./OrderAndStatus.png" alt="命令和状态转换" width = 80%> </div>

```
# 初始化
git init

# 查看日志
git log
git-log

# 查看状态
git status

# 添加到暂存区
git add <fileName>
git add <*>

# 从暂存区删除
git rm --cached <fileName>
git reset HEAD <fileName>

# 废弃当前修改
git checkout -- <fileName>

# 比较暂存区和版本库差异
git diff --staged

# 删除文件
git rm -rf <fileName>
# Hint: 不要```rm -rf *```!!!

# 提交
git commit -m "说明"

# 历史日志
git reflog

# 回退
git reset --hard <commitID>
```

## 分支命令

- Master: 主分支，通常保存官方发布历史
- Develop: 日常开发分支，集成各种功能开发的分支
- Feature：功能开发分支，每个新功能创建一个分支，完成开发后合并到Develop
- Release：预上线分支，发布提测阶段，以release分支代码为基准提测
- Hotfix：修复分支，线上出现问题时，以master分支为基线创建，合并到master和develop

```
# 查看分支
git branch <branchName>

# 创建分支
git branch <branchName>
# Hint: 常用分支：feature -> develop -> master/main，还有 hotfix, test, pre

# 切换分支
git checkout <branchName>

# 创建并切换分支
git checkout -b <branchName>

# 检查并删除分支
git branch -d <branchName>

# 强制删除分支（不进行检查）
git branch -D <branchName>
# Hint: 未完全 merge 时可用 -D 强制删除 。

# 删除分支后推送到远程
git push --delete <branchName>

# 重命名分支名称
git branch -M <main>

# 版本命名 Tag
git tag -a <v0.1> -m '部署包版本名'
```

### merge 合并分支

```
git merge <branchName>
```

Hint: 如果有冲突会将冲突位置标注，手动解决后可add和commit 。

- 手动修改产生冲突的文件，然后以add commit命令提交
- 保留当前分支修改: ```git checkout --ours  <file>```
- 保留合并分支修改: ```git checkout --theirs <file>```
- 放弃合并：```git merge --abort```

### rebase 

功能：在另一个分支基础之上重新应用，用于把一个分支的修改合并到当前分支
- 减少分支合并交叉，保持历史提交整洁
- 合并当前分支多个提交记录

官方原文解释：当执行rebase操作时，git会从两个分支的共同祖先开始提取待变基分支上的修改，然后将待变基分支指向基分支的最新提交，最后将刚才提取的修改应用到基分支的最新提交的后面。

结合例子解释：当在feature分支上执行git rebase master时，git会从master和featuer的共同祖先B开始提取feature分支上的修改，也就是C和D两个提交，先提取到。然后将feature分支指向master分支的最新提交上，也就是M。最后把提取的C和D接到M后面，注意这里的接法，官方没说清楚，实际是会依次拿M和C、D内容分别比较，处理冲突后生成新的C’和D’。一定注意，这里新C’、D’和之前的C、D已经不一样了，是我们处理冲突后的新内容，feature指针自然最后也是指向D’

通俗解释：rebase，变基，可以直接理解为改变基底。feature分支是基于master分支的B拉出来的分支，feature的基底是B。而master在B之后有新的提交，就相当于此时要用master上新的提交来作为feature分支的新基底。实际操作为把B之后feature的提交先暂存下来，然后删掉原来这些提交，再找到master的最新提交位置，把存下来的提交再接上去（接上去是逐个和新基底处理冲突的过程），如此feature分支的基底就相当于变成了M而不是原来的B了。（注意，如果master上在B以后没有新提交，那么就还是用原来的B作为基，rebase操作相当于无效，此时和git merge就基本没区别了，差异只在于git merge会多一条记录Merge操作的提交记录）

上面的例子可抽象为如下实际工作场景：远程库上有一个master分支目前开发到B了，张三从B拉了代码到本地的feature分支进行开发，目前提交了两次，开发到D了；李四也从B拉到本地的master分支，他提交到了M，然后合到远程库的master上了。此时张三想从远程库master拉下最新代码，于是他在feature分支上执行了git pull origin master:feature --rebase（注意要加–rebase参数），即把远程库master分支给rebase下来，由于李四更早开发完，此时远程master上是李四的最新内容，rebase后再看张三的历史提交记录，就相当于是张三是基于李四的最新提交M进行的开发了。（但实际上张三更早拉代码下来，李四拉的晚但提交早）

_潜在风险_
如果提交存在于你的仓库之外，而别人可能基于这些提交进行开发，那么不要执行变基！

- 不要基于rebase的分支切新分支
- 不要对已经合并到主分支的本地修改进行变基
- 不要在预发布/正式分支上使用rebase -i

_推荐使用场景_

- 拉公共分支最新代码——rebase，也就是git pull -r或git pull --rebase。这样的好处很明显，提交记录会比较简洁。但有个缺点就是rebase以后我就不知道我的当前分支最早是从哪个分支拉出来的了，因为基底变了嘛，所以看个人需求了。总体来说，即使是单机也不建议使用。
- 往公共分支上合代码——merge。如果使用rebase，那么其他开发人员想看主分支的历史，就不是原来的历史了，历史已经被你篡改了。举个例子解释下，比如张三和李四从共同的节点拉出来开发，张三先开发完提交了两次然后merge上去了，李四后来开发完如果rebase上去（注意，李四需要切换到自己本地的主分支，假设先pull了张三的最新改动下来，然后执行<git rebase 李四的开发分支>，然后再git push到远端），则李四的新提交变成了张三的新提交的新基底，本来李四的提交是最新的，结果最新的提交显示反而是张三的，就乱套了，以后有问题就不好追溯了。
  
```
# 将当前分支变基到main（远程仓库）
git pull --rebase|-r <main>

# 将当前分支变基到main
git rebase <main>


# 实操
git rebase main
# 手动合并
git rebase --continue
```

## 远程仓库

### windows 生成密钥对

```
ssh-keygen -t rsa
```

Hint: 可自行设置保存密钥的文件名以生成多个密钥 。

### 测试连接 github

```
ssh -T <git@github.com>
```

### 添加远程仓库

```
git remote add origin <http://...>
```

### 查看远程仓库

```
git remote
```

### 将本地 push 到远程仓库

```
git push origin main
git push origin main:main
git push [-f] [--set-upstream] [远端名称 [本地分支名][:远端分支名]]
git push
```

- -f : 强制覆盖

- --set-upstream : push 时建立对应关系

### 查看对应关系

```
git branch -vv
```

### 从远程仓库克隆

```
git clone <仓库路径> [本地目录]
```

### 从远程仓库抓取

```
git pull
```

### fetch+merge

### 从远程仓库拉取

```
git fetch
git merge origin/main
```

Hint: 远程分支也是分支 。

## git stash
收到紧急需求，如何临时切换

- 背景
    日常开发过程中，在某个feature分支修改了部分内容，但是还不足以commit，临时需要进行某个紧急需求开发
- 解决方式
    git stash命令可以将目前还不想提交的但是已经修改的内容进行保存至堆栈中，后续可以在某个分支上恢复出堆栈中的内容

```
(feature/xxx)$: git stash   #暂存修改内容

(feature/xxx)$: git checkout  hotfix  #切换分支，开发提交
(hotfix)$: git add .
(hotfix)$: git commit -m 'hotfix'
(hotfix)$: git push

(hotfix)$: git checkout  feature/xxx   #切回原来分支，恢复现场
(feature/xxx)$: git stash pop
```

## 后悔药


- 当前分支回退
```git reset --hard <commitID>```

- 公共远程分支版本回退
git revert用于撤销文件，并且撤销文件后不会影响其他的提交。简单来说，revert做了一个反向操作，并生成新的commitid。如果commitA中增加了几行，对commitA revert后，会生成新的commitB，内容为删除最初增加的几行。

```
git revert -n <commitId>
# 如果revert的节点是一个merge commit，需要指明保留哪个分支的内容
git revert -m 1 <commitID>  #1表示主分支
```