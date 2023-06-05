# 软件截图
- ![image](https://github.com/Avoconal/toolbox/assets/72078508/f81d9cc9-e65c-496b-a0a9-df3be5676c0d)
- ![image](https://github.com/Avoconal/toolbox/assets/72078508/231d2e12-8bcb-4534-a024-f43c99c8e105)
- ![image](https://github.com/Avoconal/toolbox/assets/72078508/717d75f5-feb4-4abb-96d0-d54fc8bf1727)
- ![image](https://github.com/Avoconal/toolbox/assets/72078508/d093a834-c9a8-40f1-97a5-91a7e2caac24)
- ![image](https://github.com/Avoconal/toolbox/assets/72078508/e0b42b23-3c15-4f6a-9a08-bb3b6ab3f408)

# 插件名称对应表

|中文名|英文全称|缩写|
|-|-|-|
|~~*安卓应用数据备份*~~|~~*Android application backup*~~|~~*aab*~~|
|安卓应用管理|Android application manage|aam|
|文件软链接|create symbol link|csl|
|文件校验|file hash check|fhc|

# v1.0

- 安卓应用数据备份

- 文件软链接

# v1.1
- ~~*安卓应用数据备份*~~ --> 安卓应用管理

- 新增安装、卸载、冻结、解冻、命令行等功能

- 更改了 ***暗黑主题*** `qdarkstyle`

# v1.2
- 新增文件校验功能

- 新增设置，支持本地保存

- 允许自定义主题和动画

- 新增文件拖拽校验

- 新增apk拖拽安装

# v2.0
- 更换设计风格为 [Fluent Design](https://github.com/zhiyiYo/PyQt-Fluent-Widgets)

- 修复 [v1.2版本](#v12) 中 [fhc组件](#插件名称对应表) 拖拽文件变为 `file:///` 的bug

- 将各窗口独立为plugins,减少 [main.py](main.py) 中的代码

- [csl组件](#插件名称对应表) 支持拖拽文件夹
