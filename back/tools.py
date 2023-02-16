# Example of face detection with a vggface2 model
from numpy import expand_dims
from matplotlib import pyplot
from PIL import Image
from numpy import asarray
from mtcnn.mtcnn import MTCNN
from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input
from keras_vggface.utils import decode_predictions
from tensorflow import keras

# extract a single face from a given photograph
def extract_face(filename, required_size=(224, 224)):
	pixels = pyplot.imread(filename)
	detector = MTCNN()
	results = detector.detect_faces(pixels)
	x1, y1, width, height = results[0]['box']
	x2, y2 = x1 + width, y1 + height
	face = pixels[y1:y2, x1:x2]
	image = Image.fromarray(face)
	image = image.resize(required_size)
	face_array = asarray(image)
	return face_array



def predict(file_path):
    pixels = extract_face(file_path)
    pixels = pixels.astype('float32')
    samples = expand_dims(pixels, axis=0)
    samples = preprocess_input(samples, version=2)
    model = VGGFace(model='resnet50')
    yhat = model.predict(samples)
    results = decode_predictions(yhat)

    json_return = {}
    for result in results[0]:
        json_return[result[0]] = result[1]*100
    
    return json_return


def predictModelBenjamin(file_path):
    pixels = extract_face(file_path)
    pixels = pixels.astype('float32')
    samples = expand_dims(pixels, axis=0)
    samples = preprocess_input(samples, version=2)
    model = keras.models.load_model('../../model/faceScan.h5')
    yhat = model.predict(samples)
    results = decode_predictions(yhat)
    return results
    # json_return = {}
    # for result in results[0]:
    #     json_return[result[0]] = result[1]*100
    
    # return json_return