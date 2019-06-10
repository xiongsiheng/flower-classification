import os
#os.system('python slim/download_and_convert_data.py --dataset_name=mydataset --dataset_dir=data/train')
for i in range(1,20,2):
	os.system('python slim/train_image_classifier.py --train_dir=data/inception_v4_model --dataset_name=flowers --dataset_split_name=train --dataset_dir=data/tfrecord --model_name=inception_v4 --checkpoint_exclude_scopes=InceptionV4/Logits,InceptionV4/AuxLogits/Aux_logits --trainable_scopes=InceptionV4/Logits,InceptionV4/AuxLogits/Aux_logits --clone_on_cpu=False --max_number_of_steps='+str(i*1000)+' --batch_size=50 --learning_rate=0.01')
	os.system('python slim/eval_image_classifier.py --checkpoint_path=data/inception_v4_model --eval_dir=data/inception_v4_model_eval_result --dataset_name=flowers --dataset_split_name=validation --dataset_dir=data/tfrecord --model_name=inception_v4')
	alldir=os.listdir("data/inception_v4_model")
	if i<19:
		for dir in alldir:
			os.remove("data/inception_v4_model/"+dir)
# tensorboard --logdir data/inception_v4_model
