from flask import Flask, request, jsonify
from flask_cors import CORS

app=Flask(__name__)

CORS(app)

from instagrapi import Client
client = Client()
@app.route("/instagram/<username>/<password>/<photoPath>/<photoCaption>", methods = ['GET'])

def instagramPost(username,password,photoPath,photoCaption):
    username =username
    password = password

    client.login(username, password)

    # This line might be the reason for error
    # kyonki hum raw string shayad nahi de pa rahe

    photo_path = photoPath

    post_caption = photoCaption

    media_id = client.photo_upload(photo_path, caption=post_caption).pk

    try:
        client.photo_publish(media_id)

    except:
        pass

    return(f'Media ID: {media_id}')
app.run()