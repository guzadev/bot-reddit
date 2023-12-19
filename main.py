import praw

reddit = praw.Reddit(
    client_id='FVywa4t6XCNPcCMMTVXyGg',
    client_secret='TeSMoc4DLco6ZFjNdYLAI-HpmMEbdw',
    user_agent='botre'
) #creamos una instancia

subreddit = reddit.subreddit('pythonforengineers') #elegir el foro donde participara el bot


for publicacion in subreddit.hot(limit=5):
    print("Title: ", publicacion.title)
    print("Text: ", publicacion.selftext)
    print("Score: ", publicacion.score)
    print("---------------------------------\n")
    