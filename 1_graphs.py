# Running separate graphs
import os
import tensorflow as tf

# Filtering out warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


g1 = tf.get_default_graph()
g2 = tf.Graph()

# Run Graph1
with g1.as_default():
	x = tf.add(3,5)
with tf.Session(graph=g1) as sess1:
	print sess1.run(x)
sess1.close()

# Run Graph2
with g2.as_default():
	y = tf.add(2,7)
with tf.Session(graph=g2) as sess2:
	print sess2.run(y)
sess2.close()