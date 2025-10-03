## 📖 About this Project
This repository is the **Datanauts final project**, created as part of our Data Science Bootcamp journey.

It showcases a simple **machine learning model deployment** using Streamlit.
We trained a **LightGBM classifier** to detect **cyberbullying texts**, then exported the model and pipeline as a `.pkl` file and deployed it as an interactive web application.  

The focus of this project was not only on model training but also on:
- Applying text preprocessing and feature engineering.
- Building a clean and user-friendly Streamlit interface.
- Deploying the model to **Streamlit Cloud** for easy public access.

## 🚀 Live Demo
👉 Try it out here: [Cyberbullying Detector App](https://final-project-datanauts.streamlit.app)

## 📊 Dataset
The model was trained on the **Cyberbullying Classification Dataset** from [Kaggle](https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification).  

This dataset contains social media posts labeled into categories such as:
- **Age**
- **Ethnicity**
- **Gender**
- **Religion**
- **Other cyberbullying**
- **Not cyberbullying**

For this project, we approached it as a **binary classification task**:
- `Cyberbullying` (all bullying categories combined)
- `Not Cyberbullying`

This allowed us to simplify the prediction into two clear outcomes for deployment in the Streamlit app.
