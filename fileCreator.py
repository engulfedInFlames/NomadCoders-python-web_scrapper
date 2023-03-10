def save_to_file(keyword, jobs):
    file = open(f"{keyword}.csv", "w")
    file.write("Title,Company,Region,Link\n")
    for job in jobs:
        file.write(f"{job['title']},{job['company']},{job['region']},{job['link']}\n")
    file.close()
