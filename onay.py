import tweepy

consumer_token = "Blsd1QrCtGXfNH838RcGabeWS"
consumer_secret = "6V3ZpSoM2X5IfmdATJmUZA7SnRuOLZ0OcNZZYYWtWixVJ3KjDX"

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print("Error! Failed to get request token.")

print(redirect_url)

verifier = input('Verifier:')

try:
    auth.get_access_token(verifier)
except tweepy.TweepError:
    print("Error! Failed to get access token.")

new_token = auth.access_token
new_secret = auth.access_token_secret
print(new_token)
print(new_secret)