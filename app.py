import streamlit as st
import requests

st.set_page_config(page_title="Housing Price Prediction")

st.title("Prédiction du prix d'une maison")

BACKEND_URL = "https://bookish-enigma-74wrpw657pr2x64g-8000.app.github.dev"

st.write("Renseigne les informations ci-dessous puis clique sur Predict.")

MedInc = st.number_input("MedInc", value=8.3)
HouseAge = st.number_input("HouseAge", value=41.0)
AveRooms = st.number_input("AveRooms", value=6.9)
AveBedrms = st.number_input("AveBedrms", value=1.0)
Population = st.number_input("Population", value=322.0)
AveOccup = st.number_input("AveOccup", value=2.5)
Latitude = st.number_input("Latitude", value=37.88)
Longitude = st.number_input("Longitude", value=-122.23)

if st.button("Predict"):
    payload = {
        "MedInc": MedInc,
        "HouseAge": HouseAge,
        "AveRooms": AveRooms,
        "AveBedrms": AveBedrms,
        "Population": Population,
        "AveOccup": AveOccup,
        "Latitude": Latitude,
        "Longitude": Longitude
    }

    try:
        response = requests.post(f"{BACKEND_URL}/predict", json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success("Prédiction réussie")
            st.write(result)
        else:
            st.error("Erreur API")
            st.write(response.text)

    except Exception as e:
        st.error("Impossible de contacter le backend")
        st.write(e)