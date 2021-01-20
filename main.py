import math
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


def spreadsheets(wsheet):
    getsheet_table = wsheet.get_all_values()
    getsheet_table = getsheet_table[3:]
    to_update = []

    for row in getsheet_table:
        
        # Converting to int because the data comes as a string
        registration = row[0]
        name = row[1]
        absence = int (row[2]) 
        p1 = int (row[3])
        p2 = int (row[4])
        p3 = int (row[5])
        
        print(registration, name, absence, p1, p2, p3)

        naf = 0

        if absence > 15:
            situation = "Reprovado por Falta"
        else:
            m = (p1+p2+p3)/3
            m = math.ceil(m)
            print("m = ", m)
            if m < 50:
                situation = "Reprovado por Nota"
            elif m < 70:
                situation = "Exame Final"
                naf = 100 - m
                print("naf = ", naf)
            else:
                situation = "Aprovado"
            
        print("situation = ", situation)
        
        list_to_update = [situation, naf]
        to_update.append(list_to_update)
        

    # + 3 to offset the header
    number_rows = len(to_update) + 3

    range_gd = "G4:H" + str(numero_linhas)

    wsheet.update(range_gd, to_update)

            
if __name__ == "__main__":
    # Authenticate Google service account
    gp = gspread.service_account(filename='sheetid.json')

    gsheet = gp.open('Engenharia de Software - Desafio Gabriel Alves de Lima')
    wsheet = gsheet.worksheet("engenharia_de_software")
    spreadsheets(wsheet)
