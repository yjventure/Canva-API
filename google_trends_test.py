from pytrends.request import TrendReq
import pandas as pd
import datetime
import warnings

# Suppress warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def fetch_top_global_trend():
    # Initialize PyTrends
    pytrends = TrendReq()

    # Regions to check for global trends
    regions = ["united_states", "india", "australia", "united_kingdom", "japan"]

    global_trends = {}
    timestamp = datetime.datetime.now(datetime.timezone.utc)  # Use timezone-aware UTC
    print(f"Fetching trends at {timestamp} UTC...\n")

    # Fetch trends for each region
    for region in regions:
        trends = pytrends.trending_searches(pn=region)
        global_trends[region] = trends[0].tolist()  # Convert top trends to a list

        print(f"Top trends in {region.replace('_', ' ').title()}:")
        print(trends.head(), "\n")

    # Combine all trends
    all_trends = [trend for trends in global_trends.values() for trend in trends]
    unique_trends = list(set(all_trends))  # Remove duplicates

    # Calculate relevance (search volume) for each unique trend
    trend_scores = []
    for trend in unique_trends:
        try:
            pytrends.build_payload([trend], timeframe="now 1-H", geo="")  # Global search volume
            interest = pytrends.interest_over_time()
            if not interest.empty:
                total_volume = interest[trend].sum()  # Sum of search volume globally
                regional_presence = sum([trend in region_trends for region_trends in global_trends.values()])
                score = total_volume * regional_presence  # Combine volume and regional relevance
                trend_scores.append({"trend": trend, "score": score})
        except Exception as e:
            print(f"Error fetching data for trend '{trend}': {e}")

    # Sort trends by score
    sorted_trends = sorted(trend_scores, key=lambda x: x["score"], reverse=True)
    top_trend = sorted_trends[0] if sorted_trends else None

    # Display the top global trend
    if top_trend:
        print("\nTop Global Trend:")
        print(f"Trend: {top_trend['trend']}, Score: {top_trend['score']}")
    else:
        print("No global trend identified.")

    return top_trend


if __name__ == "__main__":
    fetch_top_global_trend()
