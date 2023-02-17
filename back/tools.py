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


# Détection de visage avec MTCNN
def extract_face(filename, required_size=(224, 224)):
    pixels = pyplot.imread(filename)
    # Initialisation du détecteur de visage
    detector = MTCNN()
    # détecter les visages dans l'image
    results = detector.detect_faces(pixels)
    # extraire la coordonnée du visage
    x1, y1, width, height = results[0]['box']
    x2, y2 = x1 + width, y1 + height
    face = pixels[y1:y2, x1:x2]
    # extraction du visage
    image = Image.fromarray(face)
    # redimensionner les pixels de l'image dans le modèle
    image = image.resize(required_size)
    face_array = asarray(image)
    return face_array

# Predicting the identity of a person in an image with the VGGFace2 model


def predict(file_path):
    # Extaire le visage
    pixels = extract_face(file_path)
    # convertir en float32
    pixels = pixels.astype('float32')
    # ajouter une dimension
    samples = expand_dims(pixels, axis=0)
    # prétraitement des données
    samples = preprocess_input(samples, version=2)
    # charger le modèle
    model = VGGFace(model='resnet50')
    # prédiction
    yhat = model.predict(samples)
    # décodage des résultats
    results = decode_predictions(yhat)

    # stockage du résultat dans un dictionnaire
    json_return = {}
    for result in results[0]:
        json_return[result[0]] = result[1]*100

    return json_return


def predictSENET50(file_path):
    # Extaire le visage
    pixels = extract_face(file_path)
    # convertir en float32
    pixels = pixels.astype('float32')
    # ajouter une dimension
    samples = expand_dims(pixels, axis=0)
    # prétraitement des données
    samples = preprocess_input(samples, version=2)
    # charger le modèle
    model = VGGFace(model='senet50')
    # prédiction
    yhat = model.predict(samples)
    # décodage des résultats
    results = decode_predictions(yhat)

    # stockage du résultat dans un dictionnaire
    json_return = {}
    for result in results[0]:
        json_return[result[0]] = result[1]*100

    return json_return


def predictModelBenjamin(file_path):
    pixels = extract_face(file_path)
    pixels = pixels.astype('float32')
    samples = expand_dims(pixels, axis=0)
    samples = preprocess_input(samples, version=2)
    model = keras.models.load_model('../../vgg_face_weights.h5')
    yhat = model.predict(samples)
    results = decode_predictions(yhat)

    json_return = {}
    for result in results[0]:
        json_return[result[0]] = result[1]*100

    return json_return
