import pandas as pd
data = pd.read_csv("Attendance.csv")


if 'Email' in data.columns:
    emails = list(data['Email'])
    c = []

    for i in emails:

        if pd.isnull(i)==False:
            c.append(i)


    emails=c




