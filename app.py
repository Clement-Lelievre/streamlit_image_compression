import streamlit as st
from sklearn.cluster import KMeans
from utils import *
import matplotlib.image as mpimg


# utiliser colonnes: photo avant/après

st.set_page_config(
    page_title="Image compression through Kmeans", # => Quick reference - Streamlit
    page_icon="🚀",
    layout="centered", # wide
    initial_sidebar_state="expanded") # collapsed

st.title('Image compression with Machine Learning 🖼️')
nb_colors = st.sidebar.slider("Choose number of colours",min_value=1,max_value=30,value=2, step=1, help='The number of colours your image will contain')
img = st.file_uploader("Upload image", [".png", ".jpg"])
placeholder = st.empty()
if img:
    img = mpimg.imread(save_image(img))
    img_shape = img.shape
    X = img.reshape(img_shape[0] * img_shape[1], img_shape[2])
    kmeans = KMeans(n_clusters= nb_colors)
    with st.spinner(f'Clustering on {nb_colors} colors...'):
        kmeans.fit(X)
        centers = kmeans.cluster_centers_
        labels = kmeans.labels_
        X_compressed = centers[labels] # numpy vectorized way
        X_compressed = X_compressed.astype('uint8')
        img_compressed = X_compressed.reshape(img_shape[0], img_shape[1], img_shape[2])
        columns = st.columns(2)
        placeholder.markdown('#                 Comparison 👇🏻')
        before = columns[0].image(img, caption = 'Before')
        after = columns[1].image(img_compressed, caption = 'After')
