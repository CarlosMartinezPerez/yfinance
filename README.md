# ACOMPANHANDO AÇÕES DA BOLSA

## Projeto exemplo da sensacional Empowerdata (Vinícius, o didático)

### Testes iniciais

Na pasta do projeto, utilizando um terminal (git bash, por exemplo), crie um ambiente virtual:

$ conda create --name yfinance python=3.11.7 (versão do python no seu anaconda).

Ative o ambiente virtual:

$ source activate yfinance

Instale jupyter para facilitar os testes no VSCode:

$ pip install jupyter

Abra o VSCode a partir do terminal:

$ code .

No VSCode, crie o script de teste script.py

Com CTRL + ",", pesquise com send para encontrar a configuração abaixo, que deve ser ativada. Isso irá facilitar os testes. 

"jupyter.interactiveWindow.textEditor.executeSelection": true

Vá para a edição de script.py, certificando-se que o ambiente virtual criado está ativo no no VSCode: no canto inferior direito, escolha o virtual environment yfinance.

No script.py digite "import yfinance as yf" e pressione CTRL + Enter. Se tudo estiver bem, abrirá uma janela lateral  (do VSCode, não do quarto de dormir) com o teste dessa importação sem erro. Delete script.py

Crie uma pasta yfinance dentro da pasta do projeto. Dentro desta pasta edit  o script.py:

```
import yfinance as yf

def carregar_dados(ticker):
    df = yf.Ticker(ticker).history("1y")
    df.reset_index(inplace=True)
    df[ticker] = ticker.split(".")[0]
    return df


petrobras = carregar_dados("PETR4.SA")
bb = carregar_dados("BBAS3.SA")
vale = carregar_dados("VALE3.SA")

petrobras.tail()
vale.head()
bb.head()
```

Execute os testes de cada trecho com CTRL + Enter e veja a saída dos dataframes na janela lateral.

Os dados serão agora carregados para o Microsoft Power BI com esse script Python e haverá a criação de um dashboard para o acompanhamento de preços das ações de cada empresa. Altere os tickers com aqueles que correspondem às ações de sua carteira.

Para isso, abra o Microsoft Power BI Desktop e configure-o para utilizar o ambiente virtual yfinance seguindo por Arquivo, Opções e Configurações, Opções, Scripts do Python, Definir um diretório do Python, Procurar, selecione C:\Users\seu usuário\anaconda3\envs\yfinance. OK para fechar.

Crie seu dashboard usando sua criatividade ou assista a aula 4 do trinamento.

Referência: https://www.youtube.com/watch?v=sj_F5477lvQ&t=28s




