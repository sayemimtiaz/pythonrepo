import tensorflow as tf

a=34

def _build_model():
    self.classifier = ImageClassifier(self.base_model_name)
    self.classifier.build()
    
b=45

def _fit_model():
    training_generator = TrainDataGenerator(
        self.classifier.get_preprocess_input()
    )

      
