import tensorflow as tf

optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
capped_gvs = [(tf.clip_by_value(grad, -1., 1.), var) for grad, var in gvs]
train_op = optimizer.apply_gradients(capped_gvs)
