import csv

with open("311-service-requests.csv") as f:
    read_csv = csv.reader(f)
    for friend_data in read_csv:
        print(friend_data)