xy = xy[::-1] 
for i in range(0, len(time_series) - seq_length):
    _x = time_series[i:i + seq_length, :]
    
    _, step_loss = sess.run([train, loss], feed_dict={
                                X: trainX, Y: trainY})
 print("RMSE: {}".format(rmse_val))
