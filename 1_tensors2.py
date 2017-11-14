import os
import tensorflow as tf

# Filter out warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

x = 2
y = 3
add_op = tf.add(x,y)
mul_op = tf.multiply(x,y)
useless = tf.multiply(x, add_op)
pow_op = tf.pow(add_op, mul_op)
with tf.Session() as sess:
	z = sess.run(pow_op)
	# Won't compute useless because not required in the session
	print z
