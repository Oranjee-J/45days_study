# 配置conda环境

### 1.下载anaconda和vscode

注意事项：如果本地已有python安装，和anaconda不冲突，直接下载即可。

anaconda下载版本注意选择windows-x86_64的版本，这里是清华镜像源的地址，这个地址下载相对于官网来说更快和流畅。

```http
https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/
```

双击安装包，然后一直选择继续；在自己使用的电脑上，安装面对用户选择建议选择All Users，这样切换用户无需重新安装。我的conda安装地址为

```
C:\ProgramData\anaconda3
```

安装完成后，先不要运行，关闭运行程序，然后打开cmd验证是否完成安装。

```cmd
conda --version
```





关于 conda 环境设置（使用anaconda powershell promt打开）：

1. 我的系统用户名为中文，所以不要在默认目录下创建conda环境

2. conda环境目录和conda包缓存目录都要修改：

   ```powershell
   conda config --add envs_dirs C:\conda_envs
   conda config --add pkgs_dirs C:\conda_pkgs
   ```

   

3. 创建的时候也需要指定路径，不然会自动保存到默认路径（即带中文编码的路径里）：

   ```powershell
   conda create -p C:\conda_envs\myenv python=3.8 -y
   ```

   

4. 激活时也建议加上物理路径，更加严谨

   ```powershell
   conda activate C:\conda_envs\myenv
   ```

   

5. 创建完成后需要验证python版本和python的位置，还要查看所有环境

   ```powershell
   python --version
   where.exe python
   conda env list
   ```

   

6. 删除时也加上物理路径

   ```powershell
   conda remove -p C:\conda_envs\myenv --all
   ```



关于如何登录jupyter server：

```cmd
jupyter notebook --ip=192.168.0.187
```

这里的ip是输入ipconfig，查看IPv4地址得到的。将cmd所给的链接粘贴到浏览器内即可。

注意！！！每次token都会不一样，不能直接粘贴以下网址，如果网址用不了就重新运行一下上面的cmd命令生成新的可用token

```cmd
[C 2026-05-14 17:16:01.778 ServerApp]

    To access the server, open this file in a browser:
        file:///C:/Users/%E5%B0%8F%E6%A9%98/AppData/Roaming/jupyter/runtime/jpserver-91192-open.html
    Or copy and paste one of these URLs:
        http://192.168.0.187:8888/tree?token=8dc7bbd4de5804160a63efaa39466f281c355fcff0b8d4d7
        http://127.0.0.1:8888/tree?token=8dc7bbd4de5804160a63efaa39466f281c355fcff0b8d4d7
```

