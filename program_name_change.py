import tensorflow as tf 

def read_image(filename_queue):
  reader = tf.WholeFileReader()
  key,value = reader.read(filename_queue)
  image = tf.image.decode_jpeg(value)
  return key,image
