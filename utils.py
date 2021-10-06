def save_image(file):
    '''saves locally the uploaded file'''
    with open(file.name,"wb") as f:
        f.write(file.getbuffer())
    return file.name