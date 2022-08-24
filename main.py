import requests
from TwitterAPI import TwitterAPI  # type: ignore

from settings import Settings

settings = Settings()

twitter = TwitterAPI(
    settings.CONSUMER_KEY,
    settings.CONSUMER_SECRET,
    settings.ACCESS_TOKEN_KEY,
    settings.ACCESS_TOKEN_SECRET,
)


def get_current_weather(location: str) -> dict:
    """
    Args:
        location (str): name of the location to get the current weather for

    Returns:
        current_weather (dict): current weather-data for the location
    """

    url = settings.WEER_LIVE_BASE_URL
    params = {"key": settings.WEER_LIVE_API_KEY, "locatie": location}

    current_weather = requests.get(url=url, params=params).json()

    return current_weather


def compose_tweet() -> str:
    """
    Returns:
        str: tweet-text
    """
    current_weather = get_current_weather(settings.WEER_LIVE_LOCATION)
    data = current_weather["liveweer"][0]
    location = data.get("plaats")
    condition = data.get("samenv").lower()
    temperature = data.get("temp")

    tweet_text = f"In {location} momenteel {condition} en {temperature} graden. #{location}"

    return tweet_text


def send_tweet() -> str:
    """
    Sends a tweet with the current weather

    Returns:
        status_code

    """
    tweet_text = compose_tweet()

    result = twitter.request("statuses/update", {"status": tweet_text})

    return result.status_code


def app(event: str) -> str:
    # pylint: disable=unused-argument
    return send_tweet()
