import praw
import pdb
import re
import os

reddit = praw.Reddit(
    client_id='FVywa4t6XCNPcCMMTVXyGg',
    client_secret='TeSMoc4DLco6ZFjNdYLAI-HpmMEbdw',
    username='AuthorAdvanced5236',
    password= os.environ['password'],
    user_agent='botre'
)

if not os.path.isfile('publicaciones_respondidas.txt'):
    publicaciones_respondidas = []
else:
    with open('publicaciones_respondidas.txt', 'r') as f:
        publicaciones_respondidas = f.read()
        publicaciones_respondidas = publicaciones_respondidas.split('\n')
        publicaciones_respondidas = list(filter(None, publicaciones_respondidas))

subreddit = reddit.subreddit('pythonforengineers')

for publicacion in subreddit.hot(limit=5):

    if publicacion.id not in publicaciones_respondidas:

        if re.search('mArviN', publicacion.title, re.IGNORECASE):
            publicacion.reply('Hola bot')
            print(f'El bot respondio a: {publicacion.title}')
            publicaciones_respondidas.append(publicacion.id)

with open('publicaciones_respondidas.txt', 'w') as f:
    for publicacion_id in publicaciones_respondidas:
        f.write(publicacion_id + '\n')
            
            
        