import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

#using tf.Variable.assign()
my_var = tf.Variable(10, name='my_var')
my_var_times_two = my_var.assign(2*my_var)

#using tf.Variable.assign_add()/sub()
add_var = my_var.assign_add(10)
sub_var = my_var.assign_sub(5)

# using one variable to initialize another
w = tf.Variable(tf.truncated_normal([70,10]))
# this can lead to issues
u = tf.Variable(2*w)
# ensure that w is initialized
u = tf.Variable(2*w.initialized_value())

with tf.Session() as sess:
	sess.run(my_var.initializer)

	# x = sess.run(my_var_times_two)
	# print x
	# #repeating does the operation again
	# x = sess.run(my_var_times_two)
	# print x

	# x = sess.run(add_var)
	# print x
	# y = sess.run(sub_var)
	# print y
	sess.close()

# Each session maintains its own copy of variable
sess1 = tf.Session()
sess2 = tf.Session()

sess1.run(my_var.initializer)
sess2.run(my_var.initializer)

print sess1.run(my_var.assign_add(10))
print sess2.run(my_var.assign_sub(5))

sess1.close()
sess2.close()

# an interactive session makes itself the default
sess = tf.InteractiveSession()
p = tf.constant(5)
q = tf.constant(6)
r = p + q
# now no need to mention sess.run(a), it's implied
print r.eval()
sess.close()

