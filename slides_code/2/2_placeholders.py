import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# tf.placeholder(dtype, shape=None, name=None)
# shape = None means that tensor of any shape will be accepted - this leads to issues usually, though.
a = tf.placeholder(tf.float32, shape=[3])
b = tf.constant([5,5,5], tf.float32)
# c = tf.add(a,b)
c = a + b

with tf.Session() as sess:
	# feeding [1,2,3] to placeholder a via the dict {a: [1,2,3]}
	# tensor a is the key, not the string 'a'
	print sess.run(c,{a:[1,2,3]})