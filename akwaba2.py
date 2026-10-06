import streamlit as st
st.set_page_config(page_title="TOTO AKWABA WORLD", page_icon="👑")
st.markdown("### 👑 TOTO AKWABA WORLD")
st.title("AKWABA WORLD")
st.caption("Made in Toumodi par Toto Emmanuel")
st.divider()
if "messages" not in st.session_state:
    st.session_state.messages = [{"user": "Toto", "text": "Akwaba ! 🚀"}]
for m in st.session_state.messages:
    with st.chat_message(m["user"]):
        st.write(f"**{m['user']}**: {m['text']}")
if prompt := st.chat_input("Message..."):
    st.session_state.messages.append({"user": "Toi", "text": prompt})
    st.rerun()
st.success("✅ Toto Emmanuel - CEO & Fondateur")
