def create_model(input_shape, anchors_stride_base, num_classes, load_pretrained=True, freeze_body=2,
            weights_path='model_data/yolo_weights.h5'):
    K.clear_session() # get a new session
    image_input = Input(shape=(None, None, 3))
    h, w = input_shape

    if load_pretrained:
        if freeze_body in [1, 2]:
            num = (250, len(model_body.layers)-3)[freeze_body-1]
            for i in range(num): model_body.layers[i].trainable = False
            print('Freeze the first {} layers of total {} layers.'.format(num, len(model_body.layers)))

    y_true = [
        layers.Input(name='input_2', shape=(None, None, 3, (num_classes + 5)))
    ]
    loss_list = layers.Lambda(yolo_loss, name='yolo_loss',
                           arguments={'num_classes': num_classes, 'iou_loss_thresh': iou_loss_thresh,
                                      'anchors': anchors_stride_base})([*model_body.output, *y_true])

    model = Model([model_body.input, *y_true], loss_list)

    return model, model_body
