import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# normal loading
# x = tf.Variable(10, name='x')
# y = tf.Variable(20, name='y')
# z = tf.add(x,y)
# with tf.Session as sess:
# 	sess.run(tf.global_variables_initializer())
# 	writer = tf.summary.FileWriter('../../graphs', sess.graph)
# 	for _ in range(10):
# 		sess.run(z)
# 	writer.close()

# lazy loading
x = tf.Variable(10, name='x')
y = tf.Variable(20, name='y')
with tf.Session as sess:
	sess.run(tf.global_variables_initializer())
	writer = tf.summary.FileWriter('../../graphs', sess.graph)
	for _ in range(10):
		sess.run(tf.add(x,y)) #saving a line of code here
	writer.close()

# normal loading has one node for add()
# lazy loading has 10 nodes in graph for add()
# hence the latter is computationally very expensive
# use python properties to ensure function is also loaded once the first time it is called