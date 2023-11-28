import requests
from flask import Flask

clientid = "{Client_ID}"
secret = "{secret}"

app = Flask(__name__)

#EVERY_DATA

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



#SIMPLIFIED DATA ONLY

@app.route('/api/reddit/<string:query>/<string:method>/simple', methods = ['GET'])
def redditsimple(query,method):
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

    reddit = requests.get('https://oauth.reddit.com/r/'+query+'/'+method,headers=headers).json()
    simpledata={}
    count = 0
    for i in reddit['data']['children']:
        pack={}
        title=i['data']['title']
        text=i['data']['selftext']
        url=i['data']['url']
        upvotes=i['data']['ups']
        pack['title']=title
        pack['text']=text
        pack['url']=url
        pack['upvotes']=upvotes
        simpledata[count]=pack
        count+=1
    return simpledata


if __name__ == '__main__':
    app.run(debug=True)