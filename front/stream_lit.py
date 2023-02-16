import requests
import json
import streamlit as st


st.title("Who Famous I Am ?")

# Utilisez le File Uploader de Streamlit pour obtenir l'image téléversée
uploaded_file = st.file_uploader("Choose an image...", type=["jpg"])

# Si une image est téléversée, affichez-la à l'utilisateur
if uploaded_file is not None:
    image = uploaded_file.read()
    st.image(image, caption='Uploaded Image.')

if st.button('Envoyer'):
    # Envoyer l'image à l'API
    files = {'file': ('image.jpg', image)}
    headers = {"Content-Disposition": "attachment"}
    endPoint = "http://127.0.0.1:8000/api/upload"

    # send image file to api without request
    response = requests.post(endPoint, files=files, headers=headers)

    # log the response
    st.write(response.json())

    # Télécharger l'image via l'API et l'enregistrer dans un dossier
    if response.status_code == 200:
        st.success('Image téléversée avec succès!')
    else:
        st.error('Échec du téléchargement de l\'image.')
