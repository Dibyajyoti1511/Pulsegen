import pandas as pd

def build_trend_table(topic_date_pairs, target_date):
    df = pd.DataFrame(topic_date_pairs, columns=["topic", "date"])
    df["date"] = pd.to_datetime(df["date"])

    end_date = pd.to_datetime(target_date)
    start_date = end_date - pd.Timedelta(days=30)

    all_dates = pd.date_range(start=start_date, end=end_date)

    trend = pd.pivot_table(
        df,
        index="topic",
        columns="date",
        aggfunc="size",
        fill_value=0
    )

    trend = trend.reindex(all_dates, axis=1, fill_value=0)
    trend.columns = trend.columns.date

    return trend
