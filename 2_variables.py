import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# create variable with a scalar value
a = tf.Variable(2, name='scalar')
# vector
b = tf.Variable([1,2], name='vector')
# 2d matrix
c = tf.Variable([[1,2],[3,4]], name='matrix')
# n-dim matrix initialized with zeroes
d = tf.Variable(tf.zeros([12, 4]))
# tf.Variable is a class, while tf.constant is an op
# Many ops for Variable:
x = tf.Variable(3, name='test')

x.value() # read op
x.assign() # write op
x.assign_add() # and more


with tf.Session() as sess:
	x.initializer() # init op - you HAVE to initialize your variables
	print d.value()