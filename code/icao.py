import csv
import os
import subprocess


AC_BY_ICAO = {}
AC_BY_TAIL = {}
AC_ROWS = []


def load_data():
    global AC_BY_ICAO, AC_BY_TAIL, AC_ROWS
    if len(AC_ROWS) > 0:
        return
    if not os.path.exists("./aircraft_db.csv"):
        subprocess.run(["unzip", "./aircraft_db.zip"])
    with open("aircraft_db.csv", "r", newline='') as fcsv:
        data = csv.reader(fcsv, delimiter=',')
        i = 0
        for row in data:
            row[1] = row[1].upper()
            AC_ROWS.append({
                "ICAO": row[0], 
                "Reg. ID": row[1],
                "Model": row[2],
                "Aircraft Type": row[3],
                "Operator": row[4]})
            AC_BY_ICAO[row[0]] = i
            AC_BY_TAIL[row[1]] = i
            i += 1


def get_icao_info(icao):
    global AC_BY_ICAO, AC_BY_TAIL, AC_ROWS
    load_data()
    try:
        idx = AC_BY_ICAO[icao.lower()]
    except KeyError:
        return {"ICAO": icao.lower(),
                "Reg. ID": "N/A",
                "Model": "N/A",
                "Aircraft Type": "N/A",
                "Operator": "N/A"}
    return AC_ROWS[idx]

