import streamlit as st
import pandas as pd
import json
import os
from PIL import Image

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Dashboard NLP : Analyse de Biais Médiatiques",
    page_icon="⚖️",
    layout="wide"
)

# --- CSS PERSONNALISÉ (Pour le look "Expert") ---
st.markdown("""
    <style>
    .main {background-color: #f8f9fa;}
    .stTabs [data-baseweb="tab-list"] {gap: 24px;}
    .stTabs [data-baseweb="tab"] {height: 50px; white-space: pre-wrap; background-color: #ffffff; border-radius: 4px 4px 0px 0px; box-shadow: 0px 2px 4px rgba(0,0,0,0.1);}
    div[data-testid="stMetricValue"] {font-size: 24px;}
    </style>
""", unsafe_allow_html=True)

# --- FONCTIONS DE CHARGEMENT ---
@st.cache_data
def load_data(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def afficher_image(path, caption):
    if os.path.exists(path):
        image = Image.open(path)
        st.image(image, caption=caption, use_container_width=True)
    else:
        st.warning(f"⚠️ Image manquante : {path}. Veuillez exécuter les scripts d'analyse.")

# --- SIDEBAR (Navigation) ---
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Aller vers :", 
    ["🏠 Accueil & Hypothèses", 
     "📂 Consultation des Corpus", 
     "📊 1. Analyse Lexicale", 
     "🧠 2. Analyse Sémantique", 
     "⚖️ 3. Sentiment & Agence",
     "🏁 Conclusion Globale"])

st.sidebar.markdown("---")
st.sidebar.info("**Auteur :** NLP Expert\n**Projet :** Biais Gaza vs Ukraine")

# --- PAGE 1 : ACCUEIL ---
if page == "🏠 Accueil & Hypothèses":
    st.title("⚖️ Analyse Automatisée des Biais Médiatiques")
    st.markdown("### *Comparaison des couvertures médiatiques : Gaza vs Ukraine*")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("### 🎯 Objectif\nDétecter par NLP les **double standards** dans les médias occidentaux (Fox News, BBC, CNN).")
    with col2:
        st.success("### 🛠️ Méthodologie\n1. **Scraping** Ciblé\n2. **Nettoyage** Chirurgical\n3. **NLP Multi-Vues** (Lexique, Sémantique, Syntaxe)")

    st.markdown("---")
    st.subheader("🧐 Hypothèses à Vérifier")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### 1. Biais Systémiques (Gaza vs Ukraine)")
        st.write("👉 **Ukraine :** Empathie, Héroïsme, Droit International.")
        st.write("👉 **Gaza :** Neutralité froide, Sécuritaire, Fatalité.")
    with c2:
        st.markdown("#### 2. Biais Internes (Acteurs)")
        st.write("👉 **Palestiniens :** Déshumanisés, Passifs.")
        st.write("👉 **Israéliens :** Légitimés, Défensifs.")

# --- PAGE 2 : CONSULTATION ---
elif page == "📂 Consultation des Corpus":
    st.title("📂 Exploration des Données")
    st.markdown("Cette section permet de **consulter les corpus bruts et nettoyés**, conformément aux exigences.")

    tab1, tab2 = st.tabs(["🇺🇦 CORPUS UKRAINE", "🇵🇸 CORPUS GAZA"])

    with tab1:
        data_ukr = load_data('corpus/corpus_ukraine_pretraiter.json')
        st.metric("Nombre d'articles", len(data_ukr))
        if data_ukr:
            df_ukr = pd.DataFrame(data_ukr)
            st.dataframe(df_ukr[['title', 'scraped_at', 'lexical_view']], use_container_width=True)
            with st.expander("Voir un exemple complet (JSON)"):
                st.json(data_ukr[0] if len(data_ukr) > 0 else {})

    with tab2:
        data_gaza = load_data('corpus/corpus_gaza_pretraiter.json')
        st.metric("Nombre d'articles", len(data_gaza))
        if data_gaza:
            df_gaza = pd.DataFrame(data_gaza)
            st.dataframe(df_gaza[['title', 'scraped_at', 'lexical_view']], use_container_width=True)
            with st.expander("Voir un exemple complet (JSON)"):
                st.json(data_gaza[0] if len(data_gaza) > 0 else {})

# --- PAGE 3 : LEXICAL ---
elif page == "📊 1. Analyse Lexicale":
    st.title("📊 Analyse Lexicale & Cadres")
    st.markdown("Identification des **obsessions narratives** via les fréquences (Top 20) et les nuages de mots.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Les Mots-Clés (Top 20)")
        afficher_image("images/Fig1_Top20_Mots.png", "Figure 1 : Asymétrie thématique (Enfant vs Hôpital)")
        st.caption("👉 **Ukraine** : Vocabulaire de l'Humain (Child, Family). **Gaza** : Vocabulaire de l'Infrastructure (Hospital, Tunnel).")
    
    with col2:
        st.subheader("Les Nuages de Concepts")
        afficher_image("images/Fig2_WordClouds.png", "Figure 2 : Visualisation des champs lexicaux")

    st.markdown("---")
    st.subheader("Grammaire du Conflit")
    col3, col4 = st.columns(2)
    with col3:
        afficher_image("images/Fig3_Verbes_Adjectifs.png", "Figure 3 : Verbes (Action vs État)")
    with col4:
        st.info("### 🧠 Interprétation Expert\n* **Ukraine (Verbes d'Action) :** 'Flee', 'Help', 'Defend'. Récit dynamique.\n* **Gaza (Verbes de Subir) :** 'Kill', 'Die', 'Remain'. Récit statique de fatalité.")

    st.subheader("Complexité du Récit")
    afficher_image("images/Fig6_Richesse_Lexicale.png", "Figure 6 : Richesse Lexicale (TTR)")

# --- PAGE 4 : SÉMANTIQUE ---
elif page == "🧠 2. Analyse Sémantique":
    st.title("🧠 Sémantique Vectorielle (Word2Vec)")
    st.markdown("Analyse des **contextes** et des **associations cachées**.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Le Double Standard Juridique")
        afficher_image("images/Fig4_Ngrams.png", "Figure 4 : N-Grams (Cooccurrences)")
        st.error("🚨 **Constat :** L'Ukraine est associée à 'WAR CRIME' (Droit). Gaza est associée à 'TERRORIST' (Sécurité).")

    with col2:
        st.subheader("Contexte des Acteurs")
        afficher_image("images/Fig5_Acteurs.png", "Figure 5 : Voisinage sémantique des leaders")
        st.success("✅ **Constat :** Zelensky = Président/Paix. Hamas = Terroriste/Attaque.")

# --- PAGE 5 : SENTIMENT ---
elif page == "⚖️ 3. Sentiment & Agence":
    st.title("⚖️ Sentiment & Structure de l'Agence")
    st.markdown("### L'Innovation du Projet : L'Analyse de la Passivité")
    st.write("Nous ne mesurons pas seulement l'émotion, mais **qui agit** et **qui subit**.")

    # Onglets pour séparer Victimes et Acteurs
    tab1, tab2 = st.tabs(["🥀 VICTIMES CIVILES", "🔫 ACTEURS ARMÉS"])

    with tab1:
        col1, col2 = st.columns([2, 1])
        with col1:
            afficher_image("images/Fig10_Tonalite_Ciblee.png", "Figure 10 : Passivité Grammaticale")
        with col2:
            st.markdown("### 🔍 Le Déni d'Agence")
            st.metric("Passivité Gaza", "8.0%", delta="Très élevé", delta_color="inverse")
            st.metric("Passivité Ukraine", "1.3%", delta="Normal")
            st.warning("""
            **Interprétation Linguistique :**
            Les Palestiniens sont décrits grammaticalement comme des **objets** (*"Women were killed"*). 
            Les Ukrainiens restent des **sujets** (*"People fled"*).
            """)

    with tab2:
        col1, col2 = st.columns([2, 1])
        with col1:
            # Si tu as une image séparée pour les acteurs, mets-la ici, sinon utilise la combinée
            # Ici je suppose que Fig10 contient tout ou que tu as Fig11
            afficher_image("images/Fig11_Tonalite_Acteurs.png", "Figure 11 : Polarité des Acteurs") 
            # Note: Si Fig11 n'existe pas, utilise Fig10 ou Fig5
        with col2:
            st.markdown("### ⚖️ La Fracture Morale")
            st.success("**Ukraine (+0.05) :** Héros, Défenseurs.")
            st.error("**Gaza (-0.004) :** Criminels, Agents du Chaos.")

# --- PAGE 6 : CONCLUSION ---
elif page == "🏁 Conclusion Globale":
    st.title("🏁 Bilan du Projet")
    
    st.balloons()
    
    st.markdown("""
    ### 🎯 Résultats Validés
    L'analyse NLP multi-niveaux confirme l'existence d'un **Double Standard Systémique** :
    
    | Niveau d'Analyse | 🇺🇦 UKRAINE (Épopée) | 🇵🇸 GAZA (Fatalité) |
    | :--- | :--- | :--- |
    | **Lexical** | Enfant, Famille, Aide | Hôpital, Terroriste, Tunnel |
    | **Sémantique** | Crime de Guerre (Juridique) | Opération Anti-Terroriste (Sécuritaire) |
    | **Syntaxique** | Sujet Actif (1.3% passif) | Objet Passif (8.0% passif) |
    
    ### 🏆 Valeur Ajoutée
    Notre approche originale par la **Voix Passive** a permis de révéler un biais invisible à l'analyse de sentiment classique : la déshumanisation par la grammaire.
    """)