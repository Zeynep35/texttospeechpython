import streamlit as st
from gtts_makinesi import yaziyi_sese_donustur

st.title("Yazıyı ses dönüştüren uygulamaya hoşgeldiniz!")
text = st.text_input("Dönüşmesini istediğiniz yazıyı yazın lütfen: ")

if st.button("dönüştür"):
    yaziyi_sese_donustur(text)
    st.success("ses dosyası hazır.")
