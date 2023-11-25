# Simplified_APIs
_**Simplified APIs so that they do not require OAUTHS.**_

_**Note:**_ _Create a Pull Request if you want to add more APIs and help this initiative._
<br>_**Another Note:**_ _If you are going to use this to create your own API, clone this and deploy in Render._

## 1) Reddit

_**Regular:**_

_API:_ `https://dekabilanapi.onrender.com/api/reddit/{subreddit}/{type:hot/new}`

_Usage:_ `https://dekabilanapi.onrender.com/api/reddit/news/hot`



_**Simplified:**_

_API:_ `https://dekabilanapi.onrender.com/api/reddit/{subreddit}/{type:hot/new}/simple`

_Usage:_ `https://dekabilanapi.onrender.com/api/reddit/news/hot/simple`

_Returns_:

```
{
    "0": {
        "text": "",
        "title": "🤔",
        "upvotes": 2748,
        "url": "https://i.redd.it/9vkxfm5vpe2c1.jpg"
    },
    "1": {
        "text": "",
        "title": "me irl",
        "upvotes": 780,
        "url": "https://i.redd.it/urhbyh96rf2c1.png"
    },
    "2": {
        "text": "",
        "title": "In light of the new 'Onix is spelled with a Y' Mandela Effect",
        "upvotes": 1040,
        "url": "https://i.redd.it/jwqyu9vgpe2c1.jpg"
    }
  }
```
