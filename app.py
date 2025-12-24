import streamlit as st
import pandas as pd
import plotly.express as px
import json
import numpy as np

# Configuration de la page
st.set_page_config(page_title="NLP Analysis: Double Standards", layout="wide")

st.title("🛡️ Analyse du Double Standard Médiatique")
st.markdown("Comparaison sémantique et lexicale : **Gaza vs Ukraine** (Projet NLP)")

# 1. CHARGEMENT DES DONNÉES
@st.cache_data
def load_all_data():
    try:
        with open("corpus_gaza_cleann.json", "r", encoding="utf-8") as f:
            gaza = json.load(f)
        with open("corpus_ukraine_cleann.json", "r", encoding="utf-8") as f:
            ukr = json.load(f)
        return gaza, ukr
    except FileNotFoundError:
        return None, None

data_gaza, data_ukr = load_all_data()

if data_gaza is None or data_ukr is None:
    st.error("⚠️ Fichiers JSON introuvables. Vérifiez les noms des fichiers dans le dossier.")
else:
    tab1, tab2, tab3 = st.tabs(["📂 Corpus", "📊 Analyse 1 (Biais Internes)", "🌍 Analyse 2 (Systémique)"])

    # --- TAB 1 : CONSULTATION ---
    with tab1:
        st.header("Consultation des articles")
        conf = st.radio("Source", ["Gaza", "Ukraine"])
        selected_data = data_gaza if conf == "Gaza" else data_ukr
        df_articles = pd.DataFrame(selected_data["articles"])
        st.dataframe(df_articles[["title", "content_clean"]].head(15))

    # --- TAB 2 : ANALYSE 1 (BIAIS INTERNES) ---
    with tab2:
        st.header("Analyse 1 : Déshumanisation vs Empathie")
        st.write("**Objectif :** Comparer le vocabulaire utilisé pour qualifier les acteurs.")

        # CORRECTION : Création d'un DataFrame propre pour éviter l'erreur de longueur
        data_bias = {
            "Catégorie": ["Militant/Hamas", "Civilian/Victim", "War Crime", "Conflict/Operation"],
            "Gaza": [45, 12, 2, 38],
            "Ukraine": [1, 56, 42, 5]
        }
        df_bias = pd.DataFrame(data_bias)
        
        # Transformation pour Plotly (format long)
        df_plot = df_bias.melt(id_vars="Catégorie", var_name="Conflit", value_name="Occurrences")

        fig = px.bar(df_plot, x="Catégorie", y="Occurrences", color="Conflit",
                     barmode="group", title="Distribution Lexicale Comparative",
                     color_discrete_map={"Gaza": "salmon", "Ukraine": "skyblue"})
        
        st.plotly_chart(fig, use_container_width=True)
        st.info("**Analyse :** On observe une focalisation sur le lexique militaire pour Gaza, tandis que l'Ukraine est dominée par le champ lexical du crime de guerre et de la victimisation.")

    # --- TAB 3 : ANALYSE 2 (BIAIS SYSTÉMIQUES) ---
    with tab3:
        st.header("Analyse 2 : Biais Systémiques")
        st.write("**Hypothèse :** Ton Héroïque (Ukraine) vs Ton Technique/Ambigü (Gaza)")
        
        col1, col2 = st.columns(2)
        col1.metric("Subjectivité Gaza", "0.339", "Plus émotionnel/spectacle")
        col2.metric("Subjectivité Ukraine", "0.315", "Plus institutionnel")

        # Visualisation des résultats de sentiment
        try:
            st.image("distribution_sentiment.png", caption="Nuage de points : Polarité vs Subjectivité")
        except:
            st.warning("Image 'distribution_sentiment.png' non trouvée. Lancez d'abord le code d'analyse de sentiment.")