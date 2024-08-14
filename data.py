# Lista com os meses por extenso
meses_por_extenso = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Dias para extenso
numeros_por_extenso = {
    1: "primeiro", 2: "dois", 3: "três", 4: "quatro", 5: "cinco", 6: "seis",
    7: "sete", 8: "oito", 9: "nove", 10: "dez", 11: "onze", 12: "doze",
    13: "treze", 14: "quatorze", 15: "quinze", 16: "dezesseis",
    17: "dezessete", 18: "dezoito", 19: "dezenove", 20: "vinte",
    21: "vinte e um", 22: "vinte e dois", 23: "vinte e três",
    24: "vinte e quatro", 25: "vinte e cinco", 26: "vinte e seis",
    27: "vinte e sete", 28: "vinte e oito", 29: "vinte e nove",
    30: "trinta", 31: "trinta e um"
}


# Função para converter a parte do milhar do ano
def milhar_por_extenso(milhar):
    if milhar == 1:
        return "mil"
    else:
        return f"{numeros_por_extenso[milhar]} mil"


# Função para converter o ano para extenso
def ano_por_extenso(ano):
    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    centenas = ["", "cem", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos",
                "oitocentos", "novecentos"]

    milhar = milhar_por_extenso(int(ano[0]))
    centena = int(ano[1])
    dezena = int(ano[2])
    unidade = int(ano[3])

    if centena == 1 and dezena == 0 and unidade == 0:
        return f"{milhar} e {centenas[centena]}"

    return f"{milhar} {centenas[centena]} e {dezenas[dezena]} {unidades[unidade]}".strip()


def data_por_extenso(data):
    try:
        # Divide a data nos componentes dia, mês e ano
        dia, mes, ano = map(int, data.split('/'))

        # Validações básicas
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido!")
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido!")

        # Converte o dia para extenso
        dia_extenso = numeros_por_extenso[dia]

        # Converte o ano para extenso
        ano_extenso = ano_por_extenso(str(ano))

        # Retorna a data por extenso
        return f"{dia_extenso} de {meses_por_extenso[mes - 1]} de {ano_extenso}"
    except (ValueError, IndexError):
        return None


while True:
    # Solicita a data ao usuário
    data = input("Digite a data no formato DD/MM/AAAA: ")

    # Converte a data para a forma por extenso
    data_extenso = data_por_extenso(data)

    # Verifica se a data é válida
    if data_extenso:
        print("Data por extenso:", data_extenso)
        break
    else:
        print("Data inválida. Por favor, tente novamente.")