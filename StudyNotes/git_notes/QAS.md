# Question And Solve

## push 到远程仓库失败 - 鉴权失败

```
fatal: 'https://github.com/Mengdl1037/MiBootcamp.git/' 鉴权失败
```

出现此问题的原因是本地使用了新的github用户，需要重新配置ssh和远程仓库的连接，方式如下。

## 生成多个密钥并将密钥对应到不同用户

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
PreferredAuthenticatoins publickey
User user1

# 配置2
Host user2.github.com
HostName github.com
IdentityFile ~/.ssh/id_rsa2
PreferredAuthenticatoins publickey
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
