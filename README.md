# yolotest
机器学习笔记1 yolov3 猫咪检测 主要参考了https://zhuanlan.zhihu.com/p/35490655
   
   
   一.有关数据集可以在网上下载这里给出一个自己动手丰衣足食版本 从爬数据开始
       这里给一个粗糙的 爬虫.py 轻松在百度图库爬取相应目标图片 图片标注工具为 labelImg 具体参见 https://github.com/tzutalin/labelImg  标注完        成后把数据放到两个相应文件夹 JPEGImages：用于存放所有的图片，格式为.jpg ; Annotations:用于存放与图片对应的XML文件

    接下来准备一下需要的 .txt文件 一共需要下面这些：
        1.train.txt:存放用于训练的图片的名字，每行一个名字（不带后缀.jpg）。
        2.val.txt:存放用于验证的图片的名字，每行一个名字（不带后缀.jpg）。
        3.path_train.txt:存放用于训练的图片的绝对路径，每行一个路径。
        4.path_val.txt:存放用于验证的图片的绝对路径，每行一个路径。
        5.labels文件夹的txt：每个文件存放的是对应图片的标注信息，每行一个目标，若有多行则表示读应图片上有多个目标。
        label.py 可以通过Annotation文件夹数据得到需要的labels文件夹 对图片做一个训练集测试集简单分类后通过 get_namelist.py可以得到train.txt         val.txtc然后使用博文里给出的利用train.txt，val.txt以及xml文件来生成path_train.txt,path_val.txt以及labels文件夹下所有txt文件的             python代码 到这里数据准备就完成了。
