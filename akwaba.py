import streamlit as st
st.title("AKWABA WORLD de TOUMODI 👑")
st.write("App de Toto - Ca marche !")
nom = st.text_input("Ton nom")
if st.button("Entrer"):
    st.success(f"Akwaba {nom} de Toumodi !")
