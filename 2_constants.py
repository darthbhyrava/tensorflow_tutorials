import os
import tensorflow as tf

# Filter out warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# tf.constant(value, dtype=None, shape=None, name='Const', verify_shape=False)
a = tf.constant([2,2], name='a')
b = tf.constant([[0,1],[2,3]], name='b')
x = tf.add(a, b, name='add')
y = tf.multiply(a, b, name='mul')

with tf.Session() as sess:
	#activating Tensorboard
	writer = tf.summary.FileWriter('./graphs', sess.graph)
	x,y = sess.run([x, y])
	print x, y

writer.close()