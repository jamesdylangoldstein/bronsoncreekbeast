import inspect
import re
from stravalib.client import Client
import sys
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

leader_list = []

def main():
    global leader_list

    client = Client()
    authorize_url = client.authorization_url(client_id=16694, redirect_uri='http://localhost:8282/authorized')

    access_token = '1a424f23c2b57360dab45e720a9a45bd0868f299'

    client.access_token = access_token
    rex = client.get_athlete(168768)
    abdul = client.get_athlete(9954274)
    addison = client.get_athlete(3070847)
    jd = client.get_athlete(2903427)

    leaders = client.get_segment_leaderboard(7769406)
    for leader in leaders:
        name = (str(leader.athlete_name))
        leader_list.append(name)
    print(leader_list)

@app.route('/', methods=['GET', 'POST'])
def index():
    global leader_list

    return render_template('index.html', leader_list=leader_list)


main()
