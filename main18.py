'''import csv
import json
csv_list = []
with open("疫苗接种.csv","r",encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)
    for item in reader:
        csv_list.append(item)
with open("疫苗接种.json","w",encoding="utf-8-sig") as jsonfile:
    json.dump(csv_list,jsonfile,ensure_ascii=False,indent=2)
    '''
"""
import csv
import json
with open("疫苗接种.json","r",encoding="utf-8-sig") as jsonfile:
    json_list = json.load(jsonfile)
with open("rewrite.csv","w",encoding="utf-8-sig",newline="") as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=json_list[0].keys())
    writer.writeheader()
    writer.writerows(json_list)
"""