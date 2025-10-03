import streamlit as st
import joblib

@st.cache_resource
def load_bundle():
    return joblib.load("binary_cyberbullying_model.pkl")

def run_ml_app():
    st.subheader("Cyberbullying Detection")
    b = load_bundle()
    pipeline, model = b["pipeline"], b["model"]
    threshold, labels = b["optimal_threshold"], b["classes"]

    txt = st.text_area("Enter text to classify:", height=200)

    if st.button("Classify") and txt.strip():
        X = pipeline.transform([txt])
        prob = float(model.predict_proba(X)[0, 1])
        pred = int(prob >= threshold)

        if pred == 1:
            st.error(f"🚨 This text IS Cyberbullying\n\n**Probability:** {prob:.3f}")
        else:
            st.success(f"✅ This text is NOT Cyberbullying\n\n**Probability:** {prob:.3f}")
