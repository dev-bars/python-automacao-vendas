import pandas as pd

dados = pd.read_excel("clientes_agendamentos.xlsx") #Criei a variavel dados para ler o arquivo excel
dados["agendamento"] = pd.to_datetime(dados["agendamento"], format="%d/%m/%Y") #Converti a coluna agendamento para o tipo data do pandas

#Entrada de dados
dataInicial = input("Digite a data inicial (formato dd/mm/aaaa)")
dataFinal = input("Digite a data final (formato dd/mm/aaa)")

#Processamento de dados
dataInicial = pd.to_datetime(dataInicial, format="%d/%m/%Y") #Converti variavel dataInicial para o tipo data do pandas
dataFinal = pd.to_datetime(dataFinal, format="%d/%m/%Y") #Converti variavel dataFinal para o tipo data do pandas

intervalo = (dados["agendamento"] >= dataInicial) & (dados["agendamento"] <= dataFinal) #intervalo da variavel dados lida do excel com a data de intervalo inserida pelo usuario
resultado = dados[intervalo] #resultado é as datas dentro do intervalo

#Saída de dados
print(f"Agendamentos no período são: {resultado}")

#Exportação de dados
nomearArquivo = input("Digite o nome do arquivo a salvar: ")
nomearArquivo = nomearArquivo + ".xlsx"

resultado.to_excel(nomearArquivo, index=False)
print("Arquivo gerado com sucesso")


