A little image processing project whereby I deploy a Streamlit app enabling the user to upload a photo, and that displays 
the compressed image through the kmeans clustering algorithm. 

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/clement-lelievre/streamlit_image_compression/app.py)

This app features colours that are not the default colors. To change the colours of the app elements (text, background etc.), you need to create a .streamlit/config.toml file where you would write the colours that differ from default settings.
Example:

[theme]
primaryColor="#4753f7"
backgroundColor="#131428"
textColor="#f2f2f4"

See doc here: https://docs.streamlit.io/library/advanced-features/theming