import os
import tensorflow as tf

# Filter out warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

a = tf.add(3,5)
# Look at how printing a isn't enough.
print a
# You need to run within a session.
with tf.Session() as sess:
    print sess.run(a)


