import tensorflow as tf
with tf.compat.v1.Session() as sess:

  # Build a dataflow graph.
  c = tf.constant(3,dtype=tf.int32)
  d = tf.constant(5,dtype=tf.int32)
  e = tf.multiply(c,d)

  # Execute the graph and store the value that `e` represents in `result`.
  result = sess.run(e)
  print("the result is ",result)
