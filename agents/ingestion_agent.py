from google_play_scraper import reviews
import pandas as pd

def fetch_reviews(app_id, start_date):
    result, _ = reviews(
        app_id,
        lang="en",
        country="in",
        count=3000
    )

    df = pd.DataFrame(result)
    df["date"] = pd.to_datetime(df["at"]).dt.date
    df = df[df["date"] >= pd.to_datetime(start_date).date()]

    return df[["reviewId", "content", "date"]]
