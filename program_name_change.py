import tensorflow as tf 

def read_image(filename_queue):
  reader = tf.WholeFileReader()
  tf.train.start_queue_runners()
  key,value = reader.read(filename_queue)
  image = tf.image.decode_jpeg(value)
  return key,image
