import Augmentor
import os
import shutil
classes=['tulip','daisy','dandelion','rose','sunflower']
for i in classes:
	# 1. 指定图片所在目录
	str = "/"
	seq = ("./train", i)
	p = Augmentor.Pipeline(str.join(seq))
	# # 2. 增强操作
	# # 旋转 概率0.7，向左最大旋转角度10，向右最大旋转角度10
	p.rotate(probability=0.4,max_left_rotation=25, max_right_rotation=25)
	# # 放大 概率0.3，最小为1.1倍，最大为1.6倍；1不做变换
	p.zoom(probability=0.3, min_factor=1.1, max_factor=1.6)
	p.random_distortion(probability=0.3, grid_height=3, grid_width=3, magnitude=6)
	# # 3. 指定增强后图片数目总量
	p.sample(1000)

	seq = ("./train", i,"output")
	allphoto=os.listdir(str.join(seq))
	for photo in allphoto:
		shutil.copyfile(str.join(seq)+"/"+photo,"./train/"+i+"/"+photo)
	shutil.rmtree(str.join(seq),True)
