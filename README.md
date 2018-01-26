# answer_the_question
适用于iOS设备的头脑王者答题辅助脚本，能够起到一定程度的辅助作用。仅供娱乐学习交流使用!

# 关于
程序fork自[Allen-Liang/answer_the_question](https://github.com/Allen-Liang/answer_the_question) ，原git适用于android设备。

本程序适用于iOS设备，同时你需要一台macOS的系统。

程序会依次做以下事情：

1. 通过WDA(简单来说类似于安卓的adb)调试iOS设备，进行截图操作
2. 通过事先确定的坐标进行截图
3. 利用OCR的api(本程序使用百度的OCR)分别识别出题目和选项
4. 在百度上搜索题目，并将多个选项与搜索结果进行关键词统计，并推荐可能性最大的结果。

# 使用方法

1. 环境安装 wda 和 facebook-wda。具体可以参考这个[跳一跳辅助](https://www.jianshu.com/p/ff973a5910ae)的第一大点
2. 注册百度OCRapi的OCRApi，将appid,appkey,secret填到`answer_the_question.py`对应的变量里
3. 调整问题区和选项区的区域值。根据自己手机（目前仅限iOS）的分辨率，调整image_cut()中的参数，可以用`cut_images-size.py`来慢慢调整，不过推荐将手机截图，然后将截图的原图传到电脑上，并通过sketch等画图软件，确定切图的区域。区域由一个4元组定义，表示为坐标是 (x0, y0, x1, x2)。（x0,y0）为起点坐标，（x1,y2）为终点点坐标。
4. iOS手机USB连接电脑，打开wda的Test(具体见1的文章)，如果需要端口映射,可以执行`iProxy 8100 8100`
5. 打开头脑王者等答题软件，进入到答题页，并保证题目展示完整(即不是在展示题目的动画过程中)
6. 执行`python answer_the_question.py`，计算后的结果会出现在最后，用红色标出。

# 注意
经过简单测试，程序至少在以下场景下效果不佳：

1. 选项是比较简单的数字（比如选项分别是: 5% 10% 15% 20%）
2. 题目太偏，以至于百度搜不到(即四个选项的匹配值都是0)
3. 选项仅一个简单字符，有时候会将多个选项识别成一个。

# 图

以下图来自于原Git仓库。我的修改点主要是

1. 修改原脚本在mac系统上使用时的中文展示问题
2. 图片压缩，尽量减少百度OCR的耗时。

![](https://github.com/Allen-Liang/answer_the_question/raw/master/example_images/zuixin.JPG)<br>
![](https://github.com/Allen-Liang/answer_the_question/raw/master/example_images/1.jpg)<br>
![](https://github.com/Allen-Liang/answer_the_question/raw/master/example_images/2.jpg)<br>
![](https://github.com/Allen-Liang/answer_the_question/raw/master/example_images/one.jpg)<br>
![](https://github.com/Allen-Liang/answer_the_question/raw/master/example_images/two.jpg)<br>
![](https://github.com/Allen-Liang/answer_the_question/raw/master/example_images/three.JPG)<br>

