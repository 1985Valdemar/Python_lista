import openpyxl

#carregando arquivo
book = openpyxl.load_workbook('Planilha de compras.xlsx')
#selecionando qual pagina quero abrir 
frutas_page = book ['Frutas']
#imprimindo os dados de cada linha
#Limitando onde inicia min2 e onde para max5


for rows in frutas_page.iter_rows(min_row=2, max_row=5):
    #alterar nome banana para futa 1 e salvar copia
    for cell in rows:
        #visualizar selecao separado por virgula
        #print(f'{rows[0].value},{rows[1].value},{rows[2].value}')
         if cell.value =='Uva':
            cell.value = 'Fruta1'


            
#salvar as alteraçao com versao 2
book.save('Planilha de compras V2.xlsx')