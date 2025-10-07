import streamlit as st

st.set_page_config(page_title="Cyberbullying App", page_icon="🔎", layout="wide")

from ml_app import run_ml_app

def main():
    menu = ["Home", "Cyberbullying Detector"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        # --- banner centered ---
        col_l, col_c, col_r = st.columns([1, 6, 1])
        with col_c:
            # add cyberbully pic
            st.image("cyberbully_pic.jpeg", width=700)

        # --- title under banner ---
        st.markdown("## 🔎 Cyberbullying Text Classification")

        # --- descr box ---
        st.info(
            """This app uses an **XGBoost** model to classify text as **Cyberbullying** or **Not Cyberbullying**.

**How to use:**
- Open the **Cyberbullying Detector** page from the sidebar.
- Paste a sentence and click **Classify**.
"""
        )
    else:
        run_ml_app()

if __name__ == "__main__":
    main()
