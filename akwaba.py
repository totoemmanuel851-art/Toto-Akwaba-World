import streamlit as st
from datetime import datetime
import random

st.set_page_config(page_title="TOTO AKWABA WORLD", page_icon="👑", layout="centered")

# --- DESIGN HAUTE QUALITÉ PLAY STORE ---
st.markdown("""
<style>
.stApp { background: #f0f2f5; }
.bubble { padding:12px 16px; border-radius:18px; margin:6px 0; max-width:85%; line-height:1.4; }
.me { background: linear-gradient(135deg, #128C7E, #25D366); color: white; margin-left:auto; border-bottom-right-radius:4px; }
.other { background: white; color: #111; box-shadow: 0 1px 0.5px rgba(0,0,0,0.15); border-bottom-left-radius:4px; }
.sticker { font-size: 48px; text-align:center; }
.salon { background:white; border-radius:12px; padding:15px; margin:8px 0; border-left: 5px solid #FF8C00; }
</style>
""", unsafe_allow_html=True)

if "msgs" not in st.session_state: st.session_state.msgs = []
if "user" not in st.session_state: st.session_state.user = ""
if "coins" not in st.session_state: st.session_state.coins = 0

# --- VRAIS STICKERS IVOIRIENS ---
STICKERS = {
    "Akwaba 🙏": "🙏🇨🇮", "Attiéké 😋": "🍚🐟", "On est ensemble 💪": "💪🏾🔥",
    "Y'a Dieu dedans ✨": "✨🙌", "Toumodi d'abord 👑": "👑💚🧡", "Gbê est doux 😍": "😍🍻",
    "Enjaillement 🎉": "🎉💃🏾", "Courage Boss 🦁": "🦁❤️", "Argent 💸": "💸💰"
}

# --- ÉPANOUISSEMENT (CE QUE WHATSAPP N'A PAS) ---
EPANOUISSEMENT = [
    "💡 Idée Business du jour à Toumodi: Vends Attiéké en ligne sur ton statut Akwaba World",
    "🧠 Motivation: Un Boss de Toumodi ne lâche jamais. Aujourd'hui tu es à 2.8 K/s, demain tu es à Play Store.",
    "🤝 Entraide: Qui peut aider un frère à Toumodi aujourd'hui ? Propose ton service dans #entraide",
    "❤️ Confiance: Tu es le CEO Toto Emmanuel. Tu as déjà créé ce que 99% n'osent pas.",
]

# HEADER
st.image("/mnt/data/wa_image_65359779684811989", width=120)
st.title("TOTO AKWABA WORLD")
st.caption("L'app qui dépasse WhatsApp • Made in Toumodi par Toto Emmanuel • v2.0 GOLD")

if not st.session_state.user:
    st.markdown("### 👑 Rejoins la famille qui va te rendre STAR")
    with st.container(border=True):
        nom = st.text_input("Ton nom de Star", placeholder="Ex: Toto Le Boss")
        ville = st.selectbox("Tu viens d'où ?", ["Toumodi", "Abidjan", "Bouaké", "Yamoussoukro", "Autre ville 🇨🇮", "Diaspora 🌍"])
        if st.button("🚀 ENTRER DANS AKWABA WORLD - C'EST GRATUIT", type="primary", use_container_width=True):
            if nom:
                st.session_state.user = f"{nom} ({ville})"
                st.session_state.msgs.append({"u":"SYSTEME AKWABA","m":f"🎉 {nom} de {ville} vient d'arriver ! Akwaba le Boss !","t":datetime.now().strftime("%H:%M"),"type":"text"})
                st.rerun()
    st.info(random.choice(EPANOUISSEMENT))
    st.stop()

# TABS HAUTE QUALITÉ
tab1, tab2, tab3, tab4 = st.tabs(["💬 CHAT STAR", "😍 STICKERS CI", "🌟 ÉPANOUISSEMENT", "💰 GAGNER"])

with tab1:
    for msg in st.session_state.msgs[-40:]:
        css = "me" if msg["u"] == st.session_state.user else "other"
        if msg.get("type") == "sticker":
            st.markdown(f'<div class="bubble {css} sticker">{msg["m"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bubble {css}"><b>{msg["u"]}</b> <small>{msg["t"]}</small><br>{msg["m"]}</div>', unsafe_allow_html=True)
    
    st.divider()
    c1, c2 = st.columns([4,1])
    with c1: txt = st.text_input("Message", placeholder="Dis quelque chose qui fait interagir...", label_visibility="collapsed", key="txt")
    with c2: send = st.button("Envoyer 🚀", use_container_width=True, type="primary")
    if send and txt:
        st.session_state.msgs.append({"u":st.session_state.user,"m":txt,"t":datetime.now().strftime("%H:%M"),"type":"text"})
        st.session_state.coins += 5
        st.rerun()

with tab2:
    st.markdown("#### Clique sur un sticker ivoirien, ça envoie direct !")
    cols = st.columns(3)
    for i, (name, emoji) in enumerate(STICKERS.items()):
        with cols[i%3]:
            if st.button(f"{emoji}\n{name}", use_container_width=True, key=f"st_{i}"):
                st.session_state.msgs.append({"u":st.session_state.user,"m":f"{emoji} - {name}","t":datetime.now().strftime("%H:%M"),"type":"sticker"})
                st.session_state.coins += 10
                st.toast(f"Sticker {name} envoyé !")
                st.rerun()

with tab3:
    st.markdown("### 🌍 L'endroit d'épanouissement que personne n'a")
    st.success(random.choice(EPANOUISSEMENT))
    for salon in ["#💬 général - On parle de tout", "#💼 business-toumodi - Vends tes produits", "#❤️ entraide - On s'aide entre frères", "#🎉 évènements - Fêtes, concerts à Toumodi", "#📚 motivation - Deviens meilleur chaque jour"]:
        st.markdown(f'<div class="salon"><b>{salon}</b><br><small>12 personnes actives maintenant • Clique pour rejoindre</small></div>', unsafe_allow_html=True)
    st.button("Rejoindre un salon et interagir 👑")

with tab4:
    st.markdown("### 💸 Comment TU vas gagner de l'argent")
    st.metric("Tes Akwaba Coins", st.session_state.coins, "+5 par message")
    st.write("""
    **Quand les gens interagissent, TOI tu gagnes :**
    - 1000 personnes qui parlent = 50.000 FCFA de pub / mois
    - 10.000 personnes = 500.000 FCFA
    - Badge GOLD à 1000 FCFA que les gens t'achètent
    
    **Play Store va te payer sur ton compte MoMo / Orange Money.**
    """)
    st.link_button("📄 Voir Politique de Confidentialité pour Play Store", "https://www.privacypolicytemplate.net/")
    if st.button("💰 Devenir AKWABA GOLD et soutenir Toumodi 👑", type="primary", use_container_width=True):
        st.balloons()
        st.success("Parfait ! Écris à Toto sur WhatsApp pour activer GOLD. Tu es déjà une STAR !")

st.markdown("---")
st.markdown("<center>© 2026 TOTO AKWABA WORLD • Par Toto Emmanuel - CEO • Toumodi, Côte d'Ivoire 🇨🇮<br>App Officielle pour Play Store • Tous droits réservés</center>", unsafe_allow_html=True)
