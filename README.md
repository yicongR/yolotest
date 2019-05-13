# yolotest
机器学习笔记1 yolov3 猫咪检测 主要参考了https://zhuanlan.zhihu.com/p/35490655
   
   
一.有关数据集可以在网上下载这里给出一个自己动手丰衣足食版本 从爬数据开始
   这里给一个粗糙的 爬虫.py 轻松在百度图库爬取相应目标图片 图片标注工具为 labelImg 具体参见 https://github.com/tzutalin/labelImg  标注完        成后把数据放到两个相应文件夹 JPEGImages：用于存放所有的图片，格式为.jpg ; Annotations:用于存放与图片对应的XML文件 这两个文件夹防止自己的项目目录下就好

    接下来准备一下需要的 .txt文件 一共需要下面这些：
        1.train.txt:存放用于训练的图片的名字，每行一个名字（不带后缀.jpg）。
        2.val.txt:存放用于验证的图片的名字，每行一个名字（不带后缀.jpg）。
        3.path_train.txt:存放用于训练的图片的绝对路径，每行一个路径。
        4.path_val.txt:存放用于验证的图片的绝对路径，每行一个路径。
        5.labels文件夹的txt：每个文件存放的是对应图片的标注信息，每行一个目标，若有多行则表示读应图片上有多个目标。
        label.py 可以通过Annotation文件夹数据得到需要的labels文件夹 对图片做一个训练集测试集简单分类后通过 get_namelist.py可以得到train.txt val.txtc然后使用博文里给出的利用train.txt，val.txt以及xml文件来生成path_train.txt,path_val.txt以及labels文件夹下所有txt文件的python代码 到这里数据准备就完成了。

二.修改相应的文件
   1.在项目目录下建立一个.names文件（也可以把data文件夹中的voc.names复制过来修改并重命名。
   2.把cfg文夹中的voc.data复制到自己项目目录下，改名为xxx_voc.data，并修改：

       classes= 20  #类别数
       train  = /home/wlin/darknet/cat_detect/cat_train.txt #path_train.txt路径
       valid  = /home/wlin/darknet/cat_detect/cat_val.txt  #path_val.txt路径
       names = /home/wlin/darknet/cat_detect/cat_voc.names #xxx_voc.names路径
       backup = /home/wlin/darknet/cat_detect/backup/ #建一个backup文件夹用于存放中间结果

   3.把cfg文夹中的yolov3-voc.cfg复制到自己项目目录下，并修改：

       [net]
       # Testing
       # batch=1
       # subdivisions=1    #训练时候把上面Testing的参数注释
       # Training
       batch=64
       subdivisions=32     #这个参数根据自己GPU的显存进行修改，显存不够就改大一些
       ...                 #因为训练时每批的数量 = batch/subdivisions
       ...
       ...
       learning_rate=0.001  #根据自己的需求还有训练速度学习率可以调整一下
       burn_in=1000
       max_batches = 30000  #根据自己的需求还有训练速度max_batches可以调整一下
       policy=steps
       steps=10000,20000    #跟着max_batches做相应调整
       ...
       ...
       ...
       [convolutional]
       size=1
       stride=1
       pad=1
       filters=30         #filters = 3*(classes + 5)
       activation=linear

       [yolo]
       mask = 0,1,2
       anchors = 10,13,  16,30,  33,23,  30,61,  62,45,  59,119,  116,90,  156,198,  373,326
       classes=5          #修改类别数
       num=9
       jitter=.3
       ignore_thresh = .5
       truth_thresh = 1
       random=0           #显存小的话 =0

       #这个文件的最下面有3个YOLO层，这里我才放上来了一个，这三个地方的classes做相应修改
       #每个YOLO层的上一层的convolutional层的filters也要修改

4.下载预训练模型（权重）

在项目目录下打开终端，运行命令：

    wget https://pjreddie.com/media/files/darknet53.conv.74
5.训练

到此，训练所需的文件就准备好了，可以尝试着开始训练，在darknet目录下执行：

    ./darknet detector train cat_detect/boat_voc.data cat_detect/yolov3-voc.cfg darknet53.conv.74 
    
测试自己训练的模型
我的训练集有大概2000图，最后的模型存在 /backup目录下。

（1）单张图片测试：

在darknet目录下打开终端，运行：

    ./darknet detector test ./cat_detect/cat_voc.data ./cat_detect/yolov3-voc.cfg ./cat_detect/backup/yolov3-voc_30000.weights ./cat_detect/test_data/test.jpg

2）视频测试：

在darknet目录下打开终端，运行：

./darknet detector demo ./cat_detect/cat_voc.data ./cat_detect/yolov3-voc.cfg ./cat_detect/backup/yolov3-voc_30000.weights ./cat_detect/test_data/test.mp4

