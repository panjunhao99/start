## yolov1
### 1
图片分成SxS大小的单元格，单元格预测B个预测框，每个框有置信度（含目标的可能，边界框准确度）
每个单元格需要预测 5B+C 个值
网络最后输出7x7x(C+B+4B)             C为类别数，前一个B代表置信度，后4B代表（x,y,w,h）框的定位信息


## yolov4
### Bag of freebies
①数据增广
②模拟目标物体遮挡问题上
③另外一个非常重要的问题就是使用one-hot很难描述不同类别之间关联度的关系
④设计边界框回归的目标函数