import pandas as pd

reviews = pd.read_csv("../content/winemag-data-130k-v2.csv.zip")

summary = pd.DataFrame({"count": reviews.groupby("country")["points"].count(), 
                        "points": reviews.groupby("country").points.mean().round(1)})

summary.to_csv("reviews-per-country.csv", index = True)