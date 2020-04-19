import sys

print(sys.path)


'''
一般按照如下路径寻找模块文件（按照顺序寻找，找
到即停不继续往下寻找）：
1. 内置模块
2. 当前目录
3. 程序的主目录
4. pythonpath 目录（如果已经设置了pythonpath 环境变量）
5. 标准链接库目录
6. 第三方库目录（site-packages 目录）
7. .pth 文件的内容（如果存在的话）
8. sys.path.append()临时添加的目录
'''