# introdução
Devido ao grande fluxo de entradas financeiras do final de ano, criei esta simples aplicação a fim de auxiliar a equipe da operação na tarefa de enviar os dados dos comprovantes bancários para o financeiro. O sistema consiste de uma simples interface Tkinter de inputs (post.py) que emite dados para um banco MongoDB permitindo a requisição desses dados à partir de qualquer outro computador. O arquivo read.py é apenas um simples exemplo de requisição do database.

# screenshot
![screenshot](screenshot.png)


# utilização (post.py)
O operador deve preencher os campos 'Origem', 'Valor', e 'Data (de entrada)', clicar em enviar comprovante e aguardar o aparecimento da mensagem confirmando o envio no canto inferior da interface.

# pacotes
Esta aplicação requer apenas dois módulos: (1) tkinter: possibilita a criação de uma interface gráfica; (2) pymongo: realiza as devidas conecções com o bando de dados MongoDB; (3) pandas: útil para organizar os dados após a requisição do database.
