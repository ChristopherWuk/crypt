# 实现获取文件哈希值

## 代码结构
### 1.指定文件路径
读写文件采用read

### 2.获取哈希值
python hashlib模块获取文件哈希值

#### 以上两步用循环拼接在一块

### 3.交互界面
命令行指定路径，指定文件路径

## 更新日志
### 10.20 version1.0

使用listdir方法发现当目录含有子目录时报错，但若目录下只有文件时可以运行。

### 10.21 version2.0：

采用os.walk方法代替listdir，使得程序可以遍历目录下所有文件。

在读取文件时，编码出现错误，因为有些符号在utf-8中没有。解决方法：errors='ignore'，指定忽略解决。