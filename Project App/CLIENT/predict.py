import numpy as np
from keras.models import load_model  
from transformers import pipeline, set_seed
from transformers import BioGptTokenizer, BioGptForCausalLM
from tensorflow.keras.preprocessing.image import load_img
import matplotlib.pyplot as plt

class Predict():

    def __init__(self, model_path):
        self.model = load_model(model_path)

    def predict(self, image_path):
        test = np.zeros((1, 256, 256, 3), dtype="float32") 
        test[0] = np.asarray(
            load_img(
                image_path,
                target_size=(256, 256)
            )
        )
        self.pred = self.model.predict(test / 255)
        self.preds_t = (self.pred[0] > 0.5).astype(np.uint8)
        if self.preds_t.any() == 0:
            message = 'No Tumor'
            plt.imshow(self.pred[0])
            plt.savefig('CLIENT/static/result/prediction.png')
        else:
            message = 'Tumor'
            plt.imshow(self.pred[0])
            plt.savefig('CLIENT/static/result/prediction.png')

        return message
    
class BioGpt():

    def __init__(self):
        self.model = BioGptForCausalLM.from_pretrained("microsoft/biogpt")
        self.tokenizer = BioGptTokenizer.from_pretrained("microsoft/biogpt")
        self.generator = pipeline('text-generation', model=self.model, tokenizer=self.tokenizer)
        set_seed(42)
        
    def predict(self):
        return self.generator(
                "To Save yourSelf From brain tumor you need ", 
                max_length=500, 
                num_return_sequences=3, 
                do_sample=True
            )