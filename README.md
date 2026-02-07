<div align="center">

# 🏠 House Price Prediction App

</div>

A clean Streamlit interface to estimate house prices using a pre-trained model. Provide property details like bedrooms, bathrooms, areas, renovation info, and location to get an estimated price in INR.

## 🔗 Live App
- Deployed link: <https://house-predictionn.streamlit.app/>

## 📁 Project Files
- app.py: Streamlit UI and prediction logic
- house_price_model.pkl: Trained model
- feature_order.pkl: Feature ordering used by the model

## ✅ Prerequisites
- Python 3.9+
- pip

## ⚙️ Setup
1. Create and activate a virtual environment.
   - python -m venv .venv
   - Windows: .venv\\Scripts\\activate
   - macOS/Linux: source .venv/bin/activate
2. Install dependencies:
   - pip install streamlit numpy joblib
3. Ensure the model files exist in the project root:
   - house_price_model.pkl
   - feature_order.pkl

## 🚀 Run locally
- streamlit run app.py
- Open the URL shown in the terminal (usually http://localhost:8501)

## 🤝 Contributing
- Contributions are welcome! Please:
  - Fork the repo and create a feature branch.
  - Follow consistent code style and add brief comments where needed.
  - Open a pull request with a clear description of changes.

## 📝 License
- MIT License. You are free to use, copy, modify, merge, publish, and distribute, with attribution.
