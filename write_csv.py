import csv


# Запись переданных данных в csv файл
def write_csv(title, content):
    with open("data.csv", mode="w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        columns = len(title)
        length_content = len(content)
        writer.writerow([obj.text for obj in title])
        for i in range(0, length_content, columns):
            writer.writerow([obj.text for obj in content[i:i + columns]])