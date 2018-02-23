import os
import tensorflow as tf

#filter out warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

val = [[1,2],[2,3],[4,5]]

# tf.zeros(shape, dtype=tf.float32, name=None)
# creates a tensor of shape and all elements will be zeroes(when run in a session)'
a = tf.zeros([2,3], tf.int32)
# tf.zeros_like(input_tensor, dtype=None, name=None, optimize=True)
# creates a tensor of shape and type as inp_t, but all elements are 0
b = tf.zeros_like(val)
# same for ones
c = tf.ones([2,3], tf.int32)
d = tf.ones_like(val)

# tf.fill(dims, value, name=None)
# creates a tensor filled with a scalar value
e = tf.fill([3,4], 5.5)

with tf.Session() as sess:
	writer = tf.summary.FileWriter('./graphs',sess.graph)
	e = sess.run(e)
	print e
