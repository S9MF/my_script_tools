## GoFilebundling

二开自项目[GoFileBinder](https://github.com/Yihsiwei/GoFileBinder)，修改如下：

* 修改载荷释放路径

* 修改加密算法可免杀部分杀软

```
  ________      ___________.__.__        ___.                     .___.__  .__
 /  _____/  ____\_   _____/|__|  |   ____\_ |__  __ __  ____    __| _/|  | |__| ____    ____
/   \  ___ /  _ \|    __)  |  |  | _/ __ \| __ \|  |  \/    \  / __ | |  | |  |/    \  / ___\
\    \_\  (  <_> )     \   |  |  |_\  ___/| \_\ \  |  /   |  \/ /_/ | |  |_|  |   |  \/ /_/  >
 \______  /\____/\___  /   |__|____/\___  >___  /____/|___|  /\____ | |____/__|___|  /\___  /
        \/           \/                 \/    \/           \/      \/              \//_____/
                GoFilebundling version: 1.1

[+] 恶意文件: calc.exe
[+] 诱饵文件: flashcenter_pp_ax_install_cn.exe
[+] 载荷路径: %public%
[+] 载荷名称: pYvnE.tmp
[+] 生成文件: sZPo.exe
```



## 安装

执行`GoFilebundling1.1.exe`前，先在`同目录下`运行`init.bat`初始化一个新的Go模块和安装非标准库依赖。

```
set GOPROXY=https://goproxy.cn,direct
go mod init 1
go get github.com/darkwyrm/b85
go get github.com/gonutz/ide/w32
```



## 使用

GoFilebundling1.1.exe -h

```
  ________      ___________.__.__        ___.                     .___.__  .__
 /  _____/  ____\_   _____/|__|  |   ____\_ |__  __ __  ____    __| _/|  | |__| ____    ____
/   \  ___ /  _ \|    __)  |  |  | _/ __ \| __ \|  |  \/    \  / __ | |  | |  |/    \  / ___\
\    \_\  (  <_> )     \   |  |  |_\  ___/| \_\ \  |  /   |  \/ /_/ | |  |_|  |   |  \/ /_/  >
 \______  /\____/\___  /   |__|____/\___  >___  /____/|___|  /\____ | |____/__|___|  /\___  /
        \/           \/                 \/    \/           \/      \/              \//_____/
                GoFilebundling version: 1.1


use:
        GoFilebundling.exe 恶意文件 诱饵文件
        GoFilebundling.exe main.exe 简历.pdf/flash.exe
```

运行捆绑马执行顺序：

* 当前目录生成诱饵文件并打开
* 在指定目录生成恶意文件并打开
* 移动捆绑马到指定目录下(%public%, %temp%, %appdata%, %ProgramData%)

## 参考

[Qianji](https://github.com/Pizz33/Qianji)

[GoFileBinder](https://github.com/Yihsiwei/GoFileBinder)
