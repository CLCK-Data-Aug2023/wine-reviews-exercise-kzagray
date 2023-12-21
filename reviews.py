import pandas as pd

#read the csv file
reviews = pd.read_csv("../content/winemag-data-130k-v2.csv.zip", index_col=0)

#group by number of reviews per country and average of point reviews per country into dataframe
summary = pd.DataFrame({"count": reviews.groupby("country"["points"].count(), 
                        "points": reviews.groupby("country").points.mean().round(1)})

#write summary to csv file
summary.to_csv("reviews-per-country.csv")