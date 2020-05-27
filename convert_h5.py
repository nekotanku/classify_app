import coremltools

coreml_model = coremltools.converters.keras.convert('animal_cnn_aug.h5', input_names='image',
image_input_names='image', output_names='Prediction', class_labels=['monkey', 'boar', 'crow', 'cat', 'lion', 'gorila', 'giraffe', 'dog'])

coreml_model.save('./animal_cnn_aug.mlmodel')
