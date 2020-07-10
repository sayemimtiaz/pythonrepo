"""
Retrain the YOLO model for your own dataset.
"""

import math
import random
import os
import cv2

import numpy as np
import keras.backend as K
from keras.layers import Input, Lambda
from keras.models import Model
from keras.optimizers import Adam
from keras.callbacks import TensorBoard, ModelCheckpoint, ReduceLROnPlateau, EarlyStopping
import keras.layers as layers

from yolo4.model import preprocess_true_boxes, yolo4_body, yolo_loss
from yolo4.utils import get_random_data

from callback_eval import Evaluate

def _main():
    print('Please visit https://github.com/miemie2013/Keras-YOLOv4 for more complete model!')

    annotation_train_path = '2012_train.txt'
    annotation_val_path = '2012_val.txt'
    log_dir = 'logs/000/'
    classes_path = 'model_data/voc_classes.txt'
    anchors_path = 'model_data/yolo4_anchors.txt'
    class_names = get_classes(classes_path)
    num_classes = len(class_names)
    class_index = ['{}'.format(i) for i in range(num_classes)]
    anchors = get_anchors(anchors_path)

    max_bbox_per_scale = 150

    anchors_stride_base = np.array([
        [[12, 16], [19, 36], [40, 28]],
        [[36, 75], [76, 55], [72, 146]],
        [[142, 110], [192, 243], [459, 401]]
    ])
    # 一些预处理
    anchors_stride_base = anchors_stride_base.astype(np.float32)
    anchors_stride_base[0] /= 8
    anchors_stride_base[1] /= 16
    anchors_stride_base[2] /= 32

    input_shape = (608, 608) # multiple of 32, hw

    model, model_body = create_model(input_shape, anchors_stride_base, num_classes, load_pretrained=False, freeze_body=2, weights_path='yolo4_weight.h5')

    logging = TensorBoard(log_dir=log_dir)
    checkpoint = ModelCheckpoint(log_dir + 'ep{epoch:03d}-loss{loss:.3f}.h5',
        monitor='loss', save_weights_only=True, save_best_only=True, period=1)
    reduce_lr = ReduceLROnPlateau(monitor='loss', factor=0.1, patience=3, verbose=1)
    early_stopping = EarlyStopping(monitor='loss', min_delta=0, patience=10, verbose=1)
    evaluation = Evaluate(model_body=model_body, anchors=anchors, class_names=class_index, score_threshold=0.05, tensorboard=logging, weighted_average=True, eval_file='2012_val.txt', log_dir=log_dir)

    with open(annotation_train_path) as f:
        lines_train = f.readlines()
    np.random.seed(10101)
    np.random.shuffle(lines_train)
    np.random.seed(None)
    num_train = len(lines_train)

    with open(annotation_val_path) as f:
        lines_val = f.readlines()
    np.random.seed(10101)
    np.random.shuffle(lines_val)
    np.random.seed(None)
    num_val = len(lines_val)

    # Train with frozen layers first, to get a stable loss.
    # Adjust num epochs to your dataset. This step is enough to obtain a not bad model.
    if False:
        model.compile(optimizer=Adam(lr=1e-3), loss={'yolo_loss': lambda y_true, y_pred: y_pred})

        batch_size = 16
        print('Train on {} samples, val on {} samples, with batch size {}.'.format(num_train, num_val, batch_size))
        model.fit_generator(data_generator_wrapper(lines[:num_train], batch_size, input_shape, anchors, num_classes),
                steps_per_epoch=max(1, num_train//batch_size),
                epochs=50,
                initial_epoch=0,
                callbacks=[logging, checkpoint])

    # Unfreeze and continue training, to fine-tune.
    # Train longer if the result is not good.
    if True:
        for i in range(len(model.layers)):
            model.layers[i].trainable = True
        model.compile(optimizer=Adam(lr=1e-5), loss={'yolo_loss': lambda y_true, y_pred: y_pred}) # recompile to apply the change
        print('Unfreeze all of the layers.')

        batch_size = 4 # note that more GPU memory is required after unfreezing the body
        print('Train on {} samples, val on {} samples, with batch size {}.'.format(num_train, num_val, batch_size))
        model.fit_generator(data_generator_wrapper(lines_train, batch_size, anchors_stride_base, num_classes, max_bbox_per_scale, 'train'),
            steps_per_epoch=max(1, num_train//batch_size),
            epochs=50000,
            initial_epoch=0,
            callbacks=[logging, checkpoint, reduce_lr, early_stopping, evaluation])

    # Further training if needed.

