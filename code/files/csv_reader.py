with open("code/files/people.csv") as file:
    for row in file:
        if row.startswith("#"):
            continue
        print(row.strip().split(","))