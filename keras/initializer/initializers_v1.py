@keras_export(v1=['keras.initializers.RandomNormal',
                  'keras.initializers.random_normal',
                  'keras.initializers.normal'])
class RandomNormal(tf.compat.v1.random_normal_initializer):

  def __init__(self, mean=0.0, stddev=0.05, seed=None, dtype=tf.float32):
    super(RandomNormal, self).__init__(
        mean=mean, stddev=stddev, seed=seed, dtype=dtype)
        

@keras_export(v1=['keras.initializers.RandomUniform',
                  'keras.initializers.random_uniform',
                  'keras.initializers.uniform'])
class RandomUniform(tf.compat.v1.random_uniform_initializer):

  def __init__(self, minval=-0.05, maxval=0.05, seed=None,
               dtype=tf.float32):
    super(RandomUniform, self).__init__(
        minval=minval, maxval=maxval, seed=seed, dtype=dtype)
