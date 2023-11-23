import requests
from flask import Flask

clientid = "{Client_ID}"
secret = "{secret}"

app = Flask(__name__)


@app.route('/api/reddit/<string:query>/<string:method>', methods = ['GET'])
def reddit(query,method):
    authorize = requests.auth.HTTPBasicAuth(clientid,secret)

    data={
    'grant_type': 'password' ,
    'username': '{username}' ,
    'password': '{password}'}

    headers={'User-Agent' : 'MYAPI/0.0.1'}

    res = requests.post('https://www.reddit.com/api/v1/access_token',auth=authorize, data=data, headers=headers)

    result = res.json()
    token = result['access_token']

    headers['Authorization'] = f'bearer {token}'

    return requests.get('https://oauth.reddit.com/r/'+query+'/'+method,headers=headers).json()

if __name__ == '__main__':
    app.run(debug=True)