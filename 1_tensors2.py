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
	z1 = sess.run(pow_op)
	# Won't compute useless in z1 because not required in the session
	z2, not_useless = sess.run([pow_op, useless])
	# tf.Session.run(fetches, feed_dict=None, options=None, run_metadata=None)
	# pass variables through fetches
	print z1, z2, not_useless
