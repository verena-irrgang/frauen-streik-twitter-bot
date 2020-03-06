import tweepy
import random

# Authenticate to Twitter
auth = tweepy.OAuthHandler("lbSzdoujUXmkxPww7WkacwzJ2", "UsfVUJvtH0WkXIh0VJDo2JEznOSH2selaC8MOCR3oJu84nImOq")
auth.set_access_token("1226904845069799424-ZadJmf4LWl3xNhwWdLOANj0V8ZVvz5", "49JDyY0TtzK83QqixL0vcsdOCNvmxWCEjmMN6dzFpvkBF")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        
        forderungenliste = ["Wir fordern die Gewerkschaften auf, zum Streik aufzurufen!",
        "Wir fordern das Recht auf politischen Streik!","Benachteiligung bei sozialer Absicherung stoppen!",
        "Recht auf körperliche und geschlechtliche Selbstbestimmung!","Asylsuchende unterstützen, nicht gefährden!",
        "Sexualisierte und geschlechtsspezifische Gewalt effektiv bekämpfen!",
        "Unsere Gesellschaft braucht KiTas!","Keine Ausgrenzung aufgrund von Behinderung!",
        "Gegen erzwungene Schöhnheitsnormen! "]
        retweet= random.choice(forderungenliste)

        api.update_status(
                status="@"+tweet.user.screen_name+retweet,
                in_reply_to_status_id=tweet.id
            )
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")




tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
hashtags = ["Frauen*streik", "Frauen*kampftag", "Frauenstreik","FemStreik","Frauenkampftag","ichstreike8M","istrike8M"]
hashtags2 = ["FemStreik"]
stream.filter(track=hashtags2, languages=["de"])

for tweet in api.search(q="Weltfrauentag", lang="de", rpp=10):
    print("***************")
    print(f"{tweet.user.name}:{tweet.text}")
    forderungenliste = ["Wir fordern die Gewerkschaften auf, zum Streik aufzurufen!",
        "Wir fordern das Recht auf politischen Streik!","Benachteiligung bei sozialer Absicherung stoppen!",
        "Recht auf körperliche und geschlechtliche Selbstbestimmung!","Asylsuchende unterstützen, nicht gefährden!",
        "Sexualisierte und geschlechtsspezifische Gewalt effektiv bekämpfen!",
        "Unsere Gesellschaft braucht KiTas!","Keine Ausgrenzung aufgrund von Behinderung!",
        "Gegen erzwungene Schöhnheitsnormen! "]
    retweet= random.choice(forderungenliste)
    api.update_status(
            status="@"+tweet.user.screen_name+retweet,
            in_reply_to_status_id=tweet.id
        )
    print(f"{tweet.user.name}:{tweet.text}")
