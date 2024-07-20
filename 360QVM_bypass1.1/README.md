# 360QVM_bypass二开
* 随机文件名
* 随机文件信息
* 加上sigthief签名窃取功能

帮助：
`python3 icon-exe.py -h`
```
Author:pant0m & Hyyrent 修改版 v 1.3

usage: icon-exe.py [-h] -f INPUT_ICON_FILE [-n NUM_ICONS] [-maxc MAX_COLOR_CHANGE] -i INPUTFILE -s SIGTHIEF

默认会生成带签名和不带签名的文件。

options:
  -h, --help            show this help message and exit
  -f INPUT_ICON_FILE, --file INPUT_ICON_FILE
                        输入ICO文件。
  -n NUM_ICONS, --number NUM_ICONS
                        要生成的图标数量。
  -maxc MAX_COLOR_CHANGE, --maxcolorchange MAX_COLOR_CHANGE
                        最大颜色变化范围。
  -i INPUTFILE, --inputfile INPUTFILE
                        输入目标PE文件。
  -s SIGTHIEF, --sigthief SIGTHIEF
                        输入要伪造签名exe路径。(必填)
```

使用：
`python3 icon-exe.py -i calc.exe -f pdf.ico -n 1 -s EALauncher.exe`

![image](https://github.com/user-attachments/assets/78f5a6dc-8a8c-4cd3-95f8-821951795bda)

二开自项目：[360QVM_bypass](https://github.com/Pizz33/360QVM_bypass)，感谢hyyrent师傅的项目。

