# solidScraping


>Esta <i>scrip</i> tem como objetivo raspar um site que armazena informações sobre leiloeiros do estado do Rio Grande do Sul e armazenar as informações obtidas em um db de forma organizada.

### Processo de Desenvovimento
>A primeira etapa foi analisar o código <i>HTML</i> do site e perceber seus padrões. A priori tive dificuldades neste site, onde os dados são renderizados, a mim não pareceu seguir um padrão como o uso de id e classes.
Notei que os blocos em que contém os dados dos leiloeiros são divididos em elementos < hr>, o mesmo representa uma linha visual na página renderizada. Comecei a trabalhar em conseguir separar cada bloco entre os < hr> utilizando a função split("</ hr>") do python.
>Colocada uma referência, a mesma cria uma lista utilizando os caracteres da função passada como o separador, dividindo então os blocos que preciso trabalhar.
Como o código <i>HTML</i> não utiliza-se de elementos mais semânticos ou o uso de ids, para conseguir extrair os dados necessários fiz o fatiamento pegando os pontos de referência presente no código.
Exemplo: O telefone ele sempre é seguido pela string “Telefone : ”, e aṕos o número do contato, tinha um elemento marcador no fim, geralmente um < br>. Então precisava apenas ultilizar estes pontos de referência para poder retirar a <i>substring</i> entre estes pontos:

- Exemplo do Html

```html
{
    Telefone : xx xxxxxx <br>
    
}
```
- Como ficou o fatiamento em Python

```Python
{
if 'Telefone : ' in bloco:
    inicio = bloco.find('Telefone : ')
    fim = bloco.find('<br/>', inicio)
    telefone = bloco[inicio + 10:fim].strip()
}
output: xx xxxxxx
```
>A mesma lógica foi utilizada nas outras informações, exceto pela data. Nela utilizei a função search, o qual passando uma expressão regular de formato de data, consegui capturar a mesma.

<hr>

## Referências

* Documentação Python
* Documentação beautifulsoup
* Documentação re
* Stack OverFlow
* Skytowner
* Chatgpt
<hr>
