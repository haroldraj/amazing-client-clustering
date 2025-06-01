"""User simulation UI"""
import streamlit as st
import joblib
import pandas as pd

# Chargement du modèle et du scaler
kmeans = joblib.load("models/kmeans_model_k6.pkl")
scaler = joblib.load("models/scaler.pkl")

# Dictionnaire de nommage des clusters
cluster_names = {
    0: "Acheteur engagé",
    1: "Visiteur passif",
    2: "Acheteur premium",
    3: "Explorateur non converti",
    4: "Client inactif",
    5: "Acheteur intensif"
}

# Interface Streamlit
st.title("Simulation de comportement d'achat")
st.markdown(
    "**Remplissez les caractéristiques d'un nouvel utilisateur pour prédire son profil client.**")

# Questions interactives
count_view = st.slider("Nombre de vues de produits", 0, 2000, 50)
count_cart = st.slider("Ajouts au panier", 0, 500, 5)
count_purchase = st.slider("Achats effectués", 0, 100, 1)
unique_sessions = st.slider("Sessions distinctes", 1, 50, 3)
active_days = st.slider("Nombre de jours actifs", 1, 200, 10)
recency_days = st.slider("Jours depuis la dernière activité", 0, 30, 5)
total_spent = st.number_input(
    "Total dépensé (€)", 0.0, 10000.0, 100.0, step=10.0)
avg_purchase_price = st.number_input(
    "Prix moyen par achat (€)", 0.0, 1000.0, 25.0, step=1.0)

# Encodage dans un DataFrame avec noms de colonnes
user_df = pd.DataFrame([{
    "count_view": count_view,
    "count_cart": count_cart,
    "count_purchase": count_purchase,
    "unique_sessions": unique_sessions,
    "active_days": active_days,
    "recency_days": recency_days,
    "total_spent": total_spent,
    "avg_purchase_price": avg_purchase_price
}])

# Normalisation
X_user_scaled = scaler.transform(user_df)

# Prédiction
cluster = kmeans.predict(X_user_scaled)[0]
category_name = cluster_names.get(cluster, "Non défini")

# Affichage
st.success(
    f"L'utilisateur simulé appartient à la catégorie : **{category_name}** (Cluster {cluster})")
