import os
import tensorflow as tf

# Filter out warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

a = tf.constant([2,2], name='a')
b = tf.constant([3,6], name='b')
x = tf.add(a,b, name='add')	

with tf.Session() as sess:
	#activating Tensorboard
	writer = tf.summary.FileWriter('./graphs', sess.graph)
	print sess.run(x)

writer.close()