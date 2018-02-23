import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# tf.Variable with a capital V, but tf.constant with a small c - because op and Class

# create variable with a scalar value
a = tf.Variable(2, name='scalar')
# vector
b = tf.Variable([1,2], name='vector')
# 2d matrix
c = tf.Variable([[1,2],[3,4]], name='matrix')
# 12x4-dim matrix initialized with zeroes
d = tf.Variable(tf.zeros([12, 4]))
# tf.Variable is a class, while tf.constant is an op

x = tf.Variable(3, name='test')
# x.value() # read op
# x.assign(5) # write op
# x.assign_add(4) # and more
assign_x = x.assign(100)

# You HAVE to initialize variables
init_all = tf.global_variables_initializer() 
# init_subset = tf.global_variables_initializer([a,b], name="init_ab")
# for single, just use initializer
with tf.Session() as sess:
	writer = tf.summary.FileWriter('../../graphs',sess.graph)
	sess.run(init_all)
	print a
	# Returns the value
	print a.eval()
	# assign op initializes the variable, too, so no need for prioir initialization
	sess.run(assign_x)
	print x.eval()
	# sess.run(init_subset)
	# print init_subset
	# sess.run(x.initializer)
	# print x

# with g.control_dependencies([a,b,c]):
	# d and x will run only after a,b,c have been executed


