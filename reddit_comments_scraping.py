from datetime import datetime, timedelta

import pandas as pd
import praw
import re
import statistics
import csv

reddit = praw.Reddit(
    client_id="XrQYx-cueSWK4g",
    client_secret="NOEH8MAzS8aCWfcRfHA9zqjUalY",
    user_agent="fire_comments",
    username="datatribute",
    password="datatribute",
)

subreddit = reddit.subreddit("financialindependence")

submissions = subreddit.search(
    "Daily FI discussion thread", limit=100
)  # returns submission ids matching this, it's an object(iterator)

submission_list = list(submissions)  # list of string values for each daily id

submission_classes = []
for x in submission_list:
    submission_classes.append(reddit.submission(
        x))  # have to use reddit.submission to create a submission instance

submission_dicts = []
all_normalized_comments = []
replace_dict = {
    'k': '000',
    'K': '000',
    'M': '000000',
    'm': '000000',
    'million': '000000',
    'Million': '000000',
    ',': ''
}

for submissionx in submission_classes:
    submissionx.comments.replace_more(limit=None)
    sub_title = submissionx.title
    sub_date = submissionx.created_utc
    dt = datetime.fromtimestamp(sub_date).strftime("%Y-%m-%d %H:%M:%S")

    comment_list = []  #unique to each submission
    for comment in submissionx.comments.list():
        comment_list.append(comment.body.encode(
            "utf-8"))  #added this encode due to error previously

    comment_list_with_dollars_per_submission = []
    for x in comment_list:
        dollar_matches = re.findall(r"\$(\d+\S+)", x.decode("utf-8"))
        for x in dollar_matches:
            comment_list_with_dollars_per_submission.append(x)

    for key, value in replace_dict.items():
        comment_list_with_dollars_per_submission = [
            w.replace(key, value)
            for w in comment_list_with_dollars_per_submission
        ]

    normalized_dollars_per_submission = []
    for x in comment_list_with_dollars_per_submission:
        list_to_int = list(map(int, re.findall(r"\d+", x)))
        normalized_dollars_per_submission.append(max(list_to_int))

    comment_count = len(comment_list)
    comment_count_with_dollar = len(normalized_dollars_per_submission)
    average_amt = statistics.mean(normalized_dollars_per_submission)
    max_amt = max(normalized_dollars_per_submission)
    median_amt = statistics.median(normalized_dollars_per_submission)

    dictx = {
        "title": sub_title,
        "date": dt,
        "comment_count": comment_count,
        "comment_count_with_dollar": comment_count_with_dollar,
        #"comments": comment_list,
        "comments_normalized_dollar": normalized_dollars_per_submission,
        "max": max_amt,
        "median": median_amt,
        "average": average_amt
    }
    submission_dicts.append(dictx)

    for x in normalized_dollars_per_submission:
        all_normalized_comments.append(
            x
        )  #appending to list outside of each submission to get list for all submissions

#new_list = [w.replace('k', '000') for w in all_normalized_comments]

#print(submission_dicts[0]['average'])
#print(statistics.mean(all_normalized_comments))

csv_columns = [
    'title', 'date', 'comment_count', 'comment_count_with_dollar',
    'comments_normalized_dollar', 'max', 'median', 'average'
]
csv_file = "fire_comments.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in submission_dicts:
            writer.writerow(data)
except IOError:
    print("I/O error")
