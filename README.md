# solidScraping


Esta <i>scrip</i> tem como objetivo raspar um site que armazena informações sobre leiloeiros do estado do Rio Grande do Sul.

### Processo de Desenvovimento
A primeira etapa foi analisar o código HTML do site e perceber seus padrões. A priori tive dificuldades, pois neste site onde renderizado os dados se segue um padrão desconhecido a mim de HTML.
Notei que os blocos em que contém os dados dos leiloeiros são divididos em elementos < hr>, o mesmo representa uma linha visual na página renderizada. Comecei a trabalhar em conseguir separar cada bloco entre os < hr> utilizando a função split("") do python.
Colocada uma referência, a mesma cria uma lista utilizando os caracteres da função passada como o separador, dividindo então os blocos que preciso trabalhar.
Como o código HTML não utiliza-se de elementos mais semânticos ou o uso de ids, para conseguir extrair os dados necessários fiz o fatiamento pegando os pontos de referência presente no código.
Exemplo: para capturar o telefone, ele sempre era seguido pela string “Telefone : ”, aṕos o número do contato, tinha um elemento marcador no fim, no qual coloquei o “menor que” para referência do fim da substring o qual eu precisava.
            Telefone : xx xxxxxx < br>
A mesma lógica foi utilizada nas outras informações, exceto pela data. Nela utilizei a função search, o qual passando uma expressão regular de formato de data, consegui capturar a mesma.

<hr>

## Referências
Documentação Python <br>
Documentação beautifulsoup<br>
Documentação re<br>
Stack OverFlow<br>
Skytowner<br>
Chatgpt
<hr>
