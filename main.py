from formulario_utils import pode_adicionar, entrada_valida
from formulario_io import carregar_dados, salvar_dados
from tabulate import tabulate

campos = [
    'Nome','CPF/CNPJ','DtAniversario','TelResidencial','TelCelular','Email',
    'DataCadastroRevendedor','RuaResidencial','ComplementoResidencial',
    'CEPResidencial','ReferenciaResidencial','BairroResidencial',
    'CidadeResidencial','EstadoResidencial'
]
nome_arquivo = "form.csv"

df = carregar_dados(nome_arquivo, campos)

while True:
    dados = {campo: entrada_valida(campo) for campo in campos}
    if not pode_adicionar(df, dados["Nome"]):
        continue
    df = df._append(dados, ignore_index=True)
    print(tabulate(df, headers='keys', tablefmt='grid'))
    continuar = input("Adicionar outro? (s/n): ").strip().lower()
    if continuar != 's':
        break

salvar_dados(df)