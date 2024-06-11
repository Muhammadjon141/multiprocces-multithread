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

def file_reader_txt1():
    time.sleep(1)
    with open("data1.txt", "r") as f1:
        file1 = f1.read()
        print(f"TXT file1: {file1}")

def file_reader_txt2():
    time.sleep(1)
    with open("data2.txt", "r") as f2:
        file2 = f2.read()
        print(f"TXT file2: {file2}")

def file_reader_json(): 
    time.sleep(1)
    with open("json.json", encoding="utf-8") as json_file:
        data = json.load(json_file)
        for i,j in zip(data, data.values()):
            print(f"JSOn file: {i}:{j}")

def file_reader_json1(): 
    time.sleep(1)
    with open("json1.json", encoding="utf-8") as json_file1:
        data1 = json.load(json_file1)
        for k,l in zip(data1, data1.values()):
            print(f"JSOn file1: {k}:{l}")

def file_reader_json2(): 
    time.sleep(1)
    with open("json2.json", encoding="utf-8") as json_file2:
        data2 = json.load(json_file2)
        for f,g in zip(data2, data2.values()):
            print(f"JSOn file2: {f}:{g}")

def file_reader_csv():
    time.sleep(1)
    with open("csv.csv", mode = "r") as csv_file:
        data_csv = csv.reader(csv_file)
        for row in data_csv:
            print(f"CSV file: {row}")

def file_reader_csv1():
    time.sleep(1)
    with open("csv1.csv", mode = "r") as csv_file1:
        data_csv1 = csv.reader(csv_file1)
        for row in data_csv1:
            print(f"CSV file: {row}")

def file_reader_csv2():
    time.sleep(1)
    with open("csv2.csv", mode = "r") as csv_file2:
        data_csv2 = csv.reader(csv_file2)
        for row in data_csv2:
            print(f"CSV file: {row}")


def main():
    thread1 = threading.Thread(target=file_reader_txt)
    thread2 = threading.Thread(target=file_reader_json)
    thread3 = threading.Thread(target=file_reader_csv)
    thread4 = threading.Thread(target=file_reader_csv1)
    thread5 = threading.Thread(target=file_reader_csv2)
    thread6 = threading.Thread(target=file_reader_json1)
    thread7 = threading.Thread(target=file_reader_json2)
    thread8 = threading.Thread(target=file_reader_txt1)
    thread9 = threading.Thread(target=file_reader_txt2)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()


if __name__ == "__main__":
    datetim = datetime.now()
    print(datetime.now())
    main()
    print(datetime.now())
    print(datetime.now() - datetim, "sekund vaqt oldi")
