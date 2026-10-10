import streamlit as st
from datetime import datetime, timedelta
import random
import time

st.set_page_config(page_title="TOTO AKWABA WORLD BUSINESS", page_icon="👑", layout="wide")

# --- SPLASH SCREEN GOLD 3 SECONDES - COMME WHATSAPP ---
if 'splash_done' not in st.session_state:
    st.session_state.splash_done = False

if not st.session_state.splash_done:
    splash_box = st.empty()
    with splash_box.container():
        st.markdown("""
        <style>
       .splash { background: linear-gradient(135deg, #0A3D1A 0%, #FFD700 50%, #FF6B00 100%); height:100vh; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; border-radius:20px; padding:40px; color:white; }
       .splash h1 { font-size:45px; color:white; text-shadow:2px 2px 8px black; }
       .splash h3 { color:#FFD700; }
        </style>
        <div class="splash">
            <h1>👑 TOTO AKWABA WORLD</h1>
            <h2>Mieux que WhatsApp</h2>
            <h3>Par Toto Emmanuel - Toumodi 🇨🇮</h3>
            <p>Chargement Extraordinaire en cours...</p>
            <p>🇨🇮 225 à vie - Business & Communauté</p>
        </div>
        """, unsafe_allow_html=True)
        try:
            st.image("splash.png", use_container_width=True)
        except:
            pass
        time.sleep(3)
    splash_box.empty()
    st.session_state.splash_done = True

# --- DESIGN WHATSAPP + BUSINESS ---
st.markdown("""
<style>
body { background:#ECE5DD; }
.header { background: linear-gradient(90deg, #075E54, #FFD700, #FF6B00); color:white; padding:14px; border-radius:12px; text-align:center; font-size:22px; font-weight:bold; }
.chat-box { background:white; border-radius:12px; padding:10px; height:450px; overflow-y:auto; }
.bubble-mine { background:#DCF8C6; padding:10px 14px; border-radius:12px 0px 12px 12px; margin:6px 0 6px auto; max-width:75%; text-align:right; }
.bubble-other { background:white; padding:10px 14px; border-radius:0px 12px 12px 12px; margin:6px auto 6px 0; max-width:75%; box-shadow:0 1px 1px #ccc; }
.tick { color:#34B7F1; font-weight:bold; }
.product-card { background:white; border:1px solid #FFD700; border-radius:12px; padding:12px; margin-bottom:10px; box-shadow:0 2px 5px rgba(0,0,0,0.1); }
.boost-badge { background:gold; color:black; padding:3px 8px; border-radius:20px; font-size:12px; font-weight:bold; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">👑 TOTO AKWABA WORLD - BUSINESS & MARCHÉ 🇨🇮</div>', unsafe_allow_html=True)

# --- DONNEES COMPLETES + BUSINESS ---
if "contacts" not in st.session_state:
    st.session_state.contacts = {
        "Maman Toumodi ❤️": {"num":"+225 07 01 02 03", "online":True, "badge":"👑 Toumodi"},
        "Boss Entreprise": {"num":"+225 07 07 07 07", "online":False, "badge":"✅ Vérifié"},
        "Yaya Abidjan": {"num":"+225 05 04 03 02", "online":True, "badge":"💎 Joie"},
    }
if "msgs" not in st.session_state: st.session_state.msgs = {}
if "status" not in st.session_state: st.session_state.status = ["On est ensemble! 🇨🇮 - Toto", "YAKO à tous - On avance 🚀"]
if "calls" not in st.session_state: st.session_state.calls = []
if "blocked" not in st.session_state: st.session_state.blocked = []
if "market_products" not in st.session_state:
    st.session_state.market_products = [
        {"id":1, "seller":"Awa Pagne Toumodi", "name":"Pagne Baoulé Authentique", "price":15000, "city":"Toumodi", "desc":"100% coton, fait main", "boost":"premium", "likes":23},
        {"id":2, "seller":"Koffi Téléphones", "name":"Tecno Spark 20", "price":85000, "city":"Abidjan", "desc":"Neuf, garantie 1 an", "boost":"top", "likes":12},
        {"id":3, "seller":"Maman Attiéké", "name":"Attiéké + Poisson 1kg", "price":3500, "city":"Toumodi", "desc":"Livraison chaude", "boost":"gratuit", "likes":45},
    ]
if "my_shop" not in st.session_state: st.session_state.my_shop = {"name":"Ma Boutique Toumodi", "city":"Toumodi", "wave":"0701010203"}
if "orders" not in st.session_state: st.session_state.orders = []
if "business_mode" not in st.session_state: st.session_state.business_mode = False
if "gains" not in st.session_state: st.session_state.gains = 0

# --- SIDEBAR ---
with st.sidebar:
    try:
        st.image("logo.png", width=110)
    except:
        st.markdown("## 👑 TOTO AKWABA")
    st.write("**Par Toto Emmanuel - Toumodi**")

    # SWITCH BUSINESS - CÔTÉ BUSINESS
    st.divider()
    st.markdown("### 💼 MODE BUSINESS")
    st.session_state.business_mode = st.toggle("Activer Mode Business", value=st.session_state.business_mode)
    if st.session_state.business_mode:
        st.success(f"🟢 Mode Business ON - Gains: {st.session_state.gains} FCFA")
        st.caption(f"Boutique: {st.session_state.my_shop['name']}")
    else:
        st.caption("🔴 Mode Perso - Active pour vendre")

    st.divider()
    search = st.text_input("🔍 Rechercher", placeholder="Nom ou numéro...")
    st.write("**Ajouter un ami - 100% libre**")
    new_name = st.text_input("Nom complet", placeholder="Ex: Koffi Yopougon")
    new_num = st.text_input("Numéro WhatsApp", placeholder="+225...")
    if st.button("➕ Ajouter cet ami", use_container_width=True, type="primary"):
        if new_name:
            st.session_state.contacts[new_name] = {"num":new_num or "+225...", "online":random.choice([True,False]), "badge":"👑 Nouveau"}
            st.session_state.msgs[new_name] = []
            st.toast(f"{new_name} ajouté! ❤️", icon="✅")
            st.rerun()

    st.divider()
    contact_names = [c for c in st.session_state.contacts.keys() if search.lower() in c.lower()]
    if contact_names:
        selected = st.radio("Tes conversations:", contact_names, index=0)
    else:
        selected = list(st.session_state.contacts.keys())[0]

# --- ONGLETS PRINCIPAUX AVEC BUSINESS ---
t1, t2, t3, t4, t5, t6 = st.tabs(["💬 CHATS", "🏪 MARCHÉ AKWABA", "💼 MA BOUTIQUE", "👀 STATUTS", "📞 APPELS", "⚙️ PARAM"])

with t1:
    c1, c2 = st.columns([3,1])
    c1.subheader(f"💬 {selected} {st.session_state.contacts[selected]['badge']}")
    c1.caption(f"{st.session_state.contacts[selected]['num']} - {'En ligne' if st.session_state.contacts[selected]['online'] else 'Vu à '+datetime.now().strftime('%H:%M')}")

    with c2:
        if st.button("🚨 Signaler arnaque"):
            st.session_state.blocked.append(selected)
            st.error(f"{selected} bloqué et signalé 🛡️")
        if st.button("🗑️ Supprimer chat"):
            st.session_state.msgs[selected] = []
            st.rerun()

    chat_container = st.container(height=420)
    msgs = st.session_state.msgs.get(selected, [])
    with chat_container:
        for m in msgs:
            if m["me"]:
                chat_container.markdown(f"<div class='bubble-mine'>{m['text']}<br><small>{m['time']} <span class='tick'>✓✓</span></small></div>", unsafe_allow_html=True)
            else:
                chat_container.markdown(f"<div class='bubble-other'><b>{m['user']}</b><br>{m['text']}<br><small>{m['time']}</small></div>", unsafe_allow_html=True)

    with st.expander("🎨 STICKERS NOUCHI 30+ - Notre force"):
        stickers = ["😎 C'est comment?", "✊🏾 On est ensemble 🇨🇮", "🙏 YAKO", "🔥 Ça va molo?", "👀 Y'a quoi?", "🧠 Faut sciencer", "💪 On est là!", "❤️ Doucement", "😂 Kill", "👑 Gâté!", "🍚 On a mangé?", "🚀 On avance", "💰 Y'a l'argent?", "🙏 Dieu est grand", "😇 Akwaba", "😅 Dosé", "🥳 Joie", "🤣 Wouh", "🇨🇮 225 à vie", "🙌 On va y arriver", "✨ Extraordinaire", "❤️ Famille", "🫶 Yako fort", "🔒 Sécurisé", "💎 Diamant", "⚡ Rapide", "🌍 Mondial", "👑 Toumodi", "🙏 Bénédiction", "🎉 Fête"]
        cols = st.columns(5)
        for i,s in enumerate(stickers):
            if cols[i%5].button(s, key=f"stk{i}"):
                st.session_state.msgs.setdefault(selected, []).append({"user":"Moi","text":s,"me":True,"time":datetime.now().strftime("%H:%M")})
                st.rerun()

    col_in, col_send = st.columns([4,1])
    prompt = col_in.text_input("Écris avec joie...", label_visibility="collapsed", placeholder="Message chiffré...")
    if col_send.button("Envoyer 🚀", use_container_width=True):
        if prompt:
            st.session_state.msgs.setdefault(selected, []).append({"user":"Moi","text":prompt,"me":True,"time":datetime.now().strftime("%H:%M")})
            if random.random() > 0.5:
                st.session_state.msgs[selected].append({"user":selected,"text":random.choice(["On est ensemble Boss ❤️","YAKO, je suis là","Faut sciencer, on avance 🇨🇮"]),"me":False,"time":datetime.now().strftime("%H:%M")})
            st.rerun()

with t2:
    st.subheader("🏪 MARCHÉ AKWABA - Tout Toumodi vend ici 🇨🇮")
    st.caption("Côté communauté marketing pour les personnes qui veulent vendre en ligne - Ton Jumia local")

    col_f1, col_f2, col_f3 = st.columns(3)
    filtre_ville = col_f1.selectbox("Ville", ["Toutes", "Toumodi", "Abidjan", "Bouaké", "Yamoussoukro"])
    filtre_cat = col_f2.selectbox("Catégorie", ["Tout", "Pagnes", "Téléphones", "Nourriture", "Coiffure", "Autres"])
    tri = col_f3.selectbox("Trier par", ["Boostés d'abord 🔥", "Moins cher", "Plus récent"])

    # Tri boost
    produits_affiches = sorted(st.session_state.market_products, key=lambda x: {"banniere":0, "premium":1, "top":2, "gratuit":3}.get(x["boost"], 3))

    if filtre_ville!= "Toutes":
        produits_affiches = [p for p in produits_affiches if p["city"] == filtre_ville]

    for prod in produits_affiches:
        badge = "⭐ PREMIUM" if prod["boost"]=="premium" else "🔥 TOP" if prod["boost"]=="top" else "📢 BANNIÈRE" if prod["boost"]=="banniere" else ""
        with st.container():
            st.markdown(f"""
            <div class="product-card">
                <b>{prod['name']}</b> {f'<span class="boost-badge">{badge}</span>' if badge else ''}<br>
                💰 <b>{prod['price']} FCFA</b> - 📍 {prod['city']} - 👤 {prod['seller']}<br>
                <small>{prod['desc']} - ❤️ {prod['likes']} likes</small>
            </div>
            """, unsafe_allow_html=True)
            b1, b2, b3 = st.columns(3)
            if b1.button(f"🛒 Acheter", key=f"buy{prod['id']}"):
                st.session_state.orders.append(prod)
                st.success(f"Commande {prod['name']}! Le vendeur {prod['seller']} va te contacter sur TOTO. Paie via Wave: {st.session_state.my_shop['wave']}")
                st.balloons()
            if b2.button(f"💬 Chat vendeur", key=f"chat{prod['id']}"):
                st.info(f"Discussion ouverte avec {prod['seller']} dans CHATS")
            if b3.button(f"❤️ {prod['likes']}", key=f"like{prod['id']}"):
                prod["likes"] += 1
                st.rerun()

    st.divider()
    st.markdown("### 💸 GAGNEZ AVEC LE PARRAINAGE")
    st.info("Ton lien parrain: `akwaba.world/parrain/TotoEmmanuel` - Gagne 10% sur chaque BOOST de tes filleuls! Partage dans tes groupes WhatsApp!")

with t3:
    st.subheader("💼 MA BOUTIQUE - Côté Business")
    if not st.session_state.business_mode:
        st.warning("Active le Mode Business dans la barre de gauche pour vendre!")
    else:
        col_shop1, col_shop2 = st.columns(2)
        with col_shop1:
            st.markdown("#### ⚙️ Config Boutique")
            shop_name = st.text_input("Nom boutique", value=st.session_state.my_shop["name"])
            shop_city = st.selectbox("Ville", ["Toumodi", "Abidjan", "Bouaké", "Yamoussoukro", "Autre"])
            shop_wave = st.text_input("Numéro Wave / OM pour recevoir l'argent", value=st.session_state.my_shop["wave"])
            if st.button("💾 Sauver boutique"):
                st.session_state.my_shop = {"name":shop_name, "city":shop_city, "wave":shop_wave}
                st.success("Boutique sauvée!")

        with col_shop2:
            st.markdown("#### 📦 Mes Commandes & Gains")
            st.metric("Gains BOOST", f"{st.session_state.gains} FCFA")
            st.metric("Commandes reçues", len(st.session_state.orders))
            for o in st.session_state.orders[-5:]:
                st.write(f"✅ {o['name']} - {o['price']} FCFA - {o['seller']}")

        st.divider()
        st.markdown("#### ➕ Ajouter un produit à vendre (Marketing)")
        with st.form("add_product"):
            p_name = st.text_input("Nom produit", placeholder="Ex: Pagne Baoulé Rouge")
            p_price = st.number_input("Prix FCFA", min_value=0, value=5000)
            p_desc = st.text_area("Description marketing")
            p_city = st.selectbox("Ville de vente", ["Toumodi", "Abidjan", "Bouaké"])
            p_boost = st.selectbox("🚀 AKWABA BOOST MARKETING - Pour vendre vite", ["Gratuit - En bas de liste", "TOP 500F / 24h - En haut", "PREMIUM 2000F / 7 jours + badge ⭐", "BANNIÈRE 5000F / Accueil de tous"])
            submit = st.form_submit_button("Publier sur le MARCHÉ AKWABA 🚀", type="primary", use_container_width=True)
            if submit and p_name:
                boost_map = {"Gratuit": "gratuit", "TOP": "top", "PREMIUM": "premium", "BANNIÈRE": "banniere"}
                boost_val = "gratuit"
                for k,v in boost_map.items():
                    if k in p_boost:
                        boost_val = v

                # Simulation paiement
                if boost_val!= "gratuit":
                    st.info(f"💳 Paiement {p_boost} à faire sur Wave: 0701010203 (Toto) - Après paiement, ton produit sera boosté automatiquement!")
                    if "500F" in p_boost: st.session_state.gains += 500
                    if "2000F" in p_boost: st.session_state.gains += 2000
                    if "5000F" in p_boost: st.session_state.gains += 5000

                new_prod = {"id": len(st.session_state.market_products)+1, "seller": st.session_state.my_shop["name"], "name": p_name, "price": p_price, "city": p_city, "desc": p_desc, "boost": boost_val, "likes": 0}
                st.session_state.market_products.insert(0, new_prod)
                st.success(f"Produit {p_name} publié sur le MARCHÉ! Avec boost {boost_val}!")
                st.balloons()

with t4:
    st.subheader("👀 Statuts - 24h")
    img = st.file_uploader("Ajoute photo/vidéo statut", type=["png","jpg","mp4"])
    txt_stat = st.text_input("Légende statut - Promo boutique?")
    if st.button("Publier statut 👑"):
        st.session_state.status.append(f"{txt_stat} - {datetime.now().strftime('%H:%M')} - Boutique: {st.session_state.my_shop['name']}")
        st.success("Statut publié!")
    for s in st.session_state.status:
        st.success(s)

with t5:
    st.subheader("📞 Appels - Chiffrés")
    for cal in st.session_state.calls[-10:]:
        st.write(cal)
    if st.button(f"🎤 Appeler {selected} en vocal", use_container_width=True):
        st.session_state.calls.append(f"Vocal avec {selected} - {datetime.now().strftime('%H:%M')} - 🔒")
        st.info("Appel vocal lancé... chiffré")
    if st.button(f"🎥 Appel vidéo avec {selected}", use_container_width=True, type="primary"):
        st.session_state.calls.append(f"Vidéo avec {selected} - {datetime.now().strftime('%H:%M')} - 🔒")
        st.info("Appel vidéo lancé... HD")

with t6:
    st.subheader("⚙️ TOTO AKWABA WORLD BUSINESS 4.0")
    st.markdown(f"""
    **👑 Auteur: Toto Emmanuel - Toumodi 🇨🇮**
    **Version 4.0 BUSINESS MARKET - Extraordinaire**
    **Gains actuels: {st.session_state.gains} FCFA**

    **NOUVEAUTÉS BUSINESS QUE WHATSAPP N'A PAS:**
    1. 🏪 MARCHÉ AKWABA - Place de marché Toumodi
    2. 💰 AKWABA BOOST - 500F, 2000F, 5000F pour vendre
    3. 💼 Ma Boutique - Catalogue FCFA + Wave/OM
    4. 🤝 Parrainage 10% - Deviens commercial
    5. 🛒 Commande directe dans le chat
    6. 🔴 LIVE Vente (bientôt)
    7. Tous les extras d'avant: Stickers Nouchi, Anti-arnaque, etc.
    """)
    st.checkbox("J'accepte de rendre Toumodi riche et conquérir le monde ❤️", value=True)

st.caption(f"© 2026 TOTO AKWABA WORLD BUSINESS - Toto Emmanuel - {st.session_state.gains} FCFA générés - On est ensemble 🚀")
