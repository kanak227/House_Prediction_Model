import streamlit as st
import numpy as np
import joblib
from datetime import datetime

model = joblib.load("house_price_model.pkl")
feature_order = joblib.load("feature_order.pkl")

st.title("🏠 House Price Prediction App")
st.write("Fill in the house details below")

col1, col2 = st.columns(2)
with col1:
    bedrooms = st.selectbox("Number of Bedrooms", list(range(1, 11)))
with col2:
    bathrooms = st.number_input("Bathrooms", min_value=0.0, step=0.5)

col3, col4 = st.columns(2)
with col3:
    floors = st.selectbox("Number of Floors", [1, 2, 3])
with col4:
    views = st.selectbox("Number of Views", [0, 1, 2, 3, 4])

col5, col6 = st.columns(2)
with col5:
    condition = st.selectbox("Condition of the House", [1, 2, 3, 4, 5])
with col6:
    grade = st.selectbox("Grade of the House", list(range(4, 14)))

col7, col8 = st.columns(2)
with col7:
    waterfront_ui = st.selectbox("Waterfront Present?", ["No", "Yes"])
    waterfront = 1 if waterfront_ui == "Yes" else 0
with col8:
    schools = st.selectbox("Number of Schools Nearby", [1, 2, 3])

col9, col10 = st.columns(2)
with col9:
    living_area = st.number_input("Living Area (sq ft)", min_value=0)
    area_excl_basement = st.number_input("Area of House (Excl. Basement)", min_value=0)
with col10:
    lot_area = st.number_input("Lot Area (sq ft)", min_value=0)
    basement_area = st.number_input("Area of the Basement", min_value=0)

col11, col12 = st.columns(2)
with col11:
    living_area_renov = st.number_input("Living Area After Renovation", min_value=0)
    latitude = st.number_input("Latitude", format="%.6f")
with col12:
    lot_area_renov = st.number_input("Lot Area After Renovation", min_value=0)
    longitude = st.number_input("Longitude", format="%.6f")

col13, col14 = st.columns(2)
with col13:
    house_age = st.number_input("House Age (years)", min_value=0, max_value=150)
with col14:
    distance_airport = st.slider("Distance from Airport (km)", 0, 100, 50)

current_year = datetime.now().year

input_dict = {
    'number of bedrooms': bedrooms,
    'number of bathrooms': bathrooms,
    'living area': living_area,
    'lot area': lot_area,
    'number of floors': floors,
    'waterfront present': waterfront,
    'number of views': views,
    'condition of the house': condition,
    'grade of the house': grade,
    'Area of the house(excluding basement)': area_excl_basement,
    'Area of the basement': basement_area,
    'Built Year': current_year - house_age,
    'Lattitude': latitude,
    'Longitude': longitude,
    'living_area_renov': living_area_renov,
    'lot_area_renov': lot_area_renov,
    'Number of schools nearby': schools,
    'Distance from the airport': distance_airport
}

input_data = np.array([[input_dict[col] for col in feature_order]])

st.markdown("---")

if st.button("Predict House Price"):
    prediction = model.predict(input_data)
    st.success(f"Estimated House Price: ₹ {prediction[0]:,.2f}")
