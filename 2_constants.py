import os
import tensorflow as tf

# Filter out warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# tf.constant(value, dtype=None, shape=None, name='Const', verify_shape=False)
a = tf.constant([2,2], name='a')
b = tf.constant([[0,1],[2,3]], name='b')
x = tf.add(a, b, name='add')
y = tf.multiply(a, b, name='mul')

# Constants as sequences:
# tf.linspace(start, stop, num, name=None)
p1 = tf.linspace(1.0, 10.0, 5, name="J1")
# tf.range(start, limit, delta)
p2 = tf.range(3, 18, 0.5)
# tf.range(limit)
p3 = tf.range(6)

# Randomly Generated Constants
# s1 = tf.random_normal(shape, mean=0.0, stddev=1.0, dtype=tf.float32, seed=None, name=None)
s1 = tf.random_normal([1,2,3])
# s2 = tf.truncated_normal(shape, mean=0.0, stddev=1.0, dtype=tf.float32, seed=None, name=None)
s2 = tf.truncated_normal([1,2,3])


with tf.Session() as sess:
	#activating Tensorboard
	writer = tf.summary.FileWriter('./graphs', sess.graph)
	p1, p2, p3 = sess.run([p1, p2, p3])
	print p1, p2, p3

writer.close()