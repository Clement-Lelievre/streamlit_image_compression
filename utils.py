import streamlit as st
from sklearn.cluster import KMeans


@st.cache
def save_image(file):
    '''saves locally the uploaded file'''
    with open(file.name,"wb") as f:
        f.write(file.getbuffer())
    return file.name

@st.cache
def fit_kmeans_image(data, nb_colors):
    kmeans = KMeans(n_clusters= nb_colors)
    kmeans.fit(data)
    centers = kmeans.cluster_centers_
    labels = kmeans.labels_
    return centers, labels
