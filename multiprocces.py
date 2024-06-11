import csv
import time
import json
import multiprocessing
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
    procces1 = multiprocessing.Process(target=file_reader_txt)
    procces2 = multiprocessing.Process(target=file_reader_json)
    procces3 = multiprocessing.Process(target=file_reader_csv)

    procces1.start()
    procces2.start()
    procces3.start()

    procces1.join()
    procces2.join()
    procces3.join()


if __name__ == "__main__":
    datetim = datetime.now()
    print(datetime.now())
    main()
    print(datetime.now())
    print(datetime.now() - datetim, "sekund vaqt oldi")