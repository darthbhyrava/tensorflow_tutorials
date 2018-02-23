import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

a = tf.constant([3,6], name='a')
b = tf.constant([2,2], name='b')
# standard addition
add_op = tf.add(a,b)
# adding n tensors
add_n_op = tf.add_n([a,b,b])
#output for the following will be [6, 12] because multiply() is element-wise
mul_op = tf.multiply(a,b)
#matrix multiplication, needs [lxm][mxn] input
re_a = tf.reshape(a,[1,2])
re_b = tf.reshape(b,[2,1])
mat_mul = tf.matmul(re_a, re_b)
# standard element-wise division
div_op = tf.div(a,b)
# modulus operations
mod_op = tf.mod(a,b)

with tf.Session() as sess:
	x,y = sess.run([div_op, mod_op])
	print x, y
