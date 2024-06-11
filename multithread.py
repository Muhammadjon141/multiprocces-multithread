import csv
import time
import json
import threading
from datetime import datetime

def file_reader_txt():
    time.sleep(1)
    with open("data.txt", "r") as f:
        file = f.read()
        print(f"TXT file: {file}")
    
def file_reader_json(): 
    time.sleep(1)
    with open("json.json", encoding="utf-8") as json_file:
        data = json.load(json_file)
        for i,j in zip(data, data.values()):
            print(f"JSOn file: {i}:{j}")

def file_reader_csv():
    time.sleep(1)
    with open("csv.csv", mode = "r") as csv_file:
        data_csv = csv.reader(csv_file)
        for row in data_csv:
            print(f"CSV file: {row}")

def main():
    thread1 = threading.Thread(target=file_reader_txt)
    thread2 = threading.Thread(target=file_reader_json)
    thread3 = threading.Thread(target=file_reader_csv)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()


if __name__ == "__main__":
    datetim = datetime.now()
    print(datetime.now())
    main()
    print(datetime.now())
    print(datetime.now() - datetim, "sekund vaqt oldi")