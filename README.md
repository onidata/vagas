# Desafio

Usando Django/DRF desenvolva uma API que permita usuários gerenciar empréstimos.

## Crtérios de aceite
* Usuários devem ser capazes de inserir empréstimos e seus respectivos pagamentos
* Usuários devem ser capazer de visualizar seus empréstimos e pagamentos
* Usuários devem ser capazes de visualizar o saldo devedor de cada um dos seus empréstimos
    * Você pode decidir onde e como mostrar a informação
    * O saldo devedor deve considerar a taxa de juros do empréstimo e descontar o que já foi pago
* Usuários não podem ver ou editar empréstimos ou pagamentos de outros usuários
* A autenticação da API deve ser feita via token
* Os empréstimos devem conter no mínimo as informações abaixo:
    * Identificador - um identificador aleatório gerado automaticamente
    * Valor nominal - o valor emprestado pelo banco
    * Taxa de juros - a taxa de juros mensal do empréstimo
    * Endereço de IP - endereço de IP que cadastrou o empréstimo
    * Data de solicitação - a data em que o empréstimo foi solicitado
    * Banco - informações do banco que emprestou o dinheiro (pode ser um simples campo de texto)
    * Cliente - informações do cliente que pegou o empréstimo (pode ser um simples campo de texto)
* Os pagamentos devem conter no mínimo as informações abaixo:
    * Identificador do empréstimo
    * Data do pagamento
    * Valor do pagamento
* Testes
    * As funcionalidade principais devem estar com testes escritos
    * Você pode decidir quais testes agregam mais valor ao projeto

## Extra (opcional)
* Cálculo do saldo devedor usando [juros compostos](https://duckduckgo.com/?q=juros+compostos) [pro rata dia](https://duckduckgo.com/?q=pro+rata+dia).
* Expandir o modelo financeiro adicionando [IOF](https://duckduckgo.com/?q=imposto+sobre+operações+financeiras), seguro, etc...

## Informações adicionais
Você pode organizar a API e o banco de dados da maneira que achar que faz mais sentido. Além disso, sinta-se a vontade para adicionar ferramentas ou funcionalidades que ache relevante.

## O que vamos avaliar
1. O cumprimento de todos os requisitos obrigatórios
2. A forma que o código está organizado
3. A abordagem para testes das APIs
4. A simplicidade da solução
5. Aderência a [PEP 8](https://duckduckgo.com/?q=pep8)
6. A implementação de requisitos opcionais
7. A implementação de funcionalidades extras
