import os
import tensorflow as tf

# Filter out warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# 0_d vectors
t_0 = 19
s1 = tf.zeros_like(t_0)
s2 = tf.ones_like(t_0)
# 1_d vectors
t_1 = ['apple','banana','citrus']
s3 = tf.zeros_like(t_1)
# s4 = tf.ones_like(t_1) | Throws up error
# 2_d vectors
t_2 = [[True, False, False],[True, False, False],[True, False, False]]
s4 = tf.zeros_like(t_2)
s5 = tf.ones_like(t_2)

with tf.Session() as sess:
	s1, s2 = sess.run([s5,s4])
	print s1, s2

