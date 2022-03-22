# SQL

TQL: Text Query Language
Pretende-se a implementa¸c˜ao de uma variante `a SQL (structured query language), mais simples, e que
funcione sobre ficheiros CSV (Comma Separated Value) armazenados numa pasta. Cada ficheiro CSV ´e
guardado em formato tabular, tal como descrito no enunciado B do primeiro trabalho pr´atico.
Considere-se que existem os seguintes ficheiros em determinada pasta:
 produtos.csv
ID,Descricao,Preco
B1,Bal~ao Decorativo (10),1.00
B2,Bal~ao da Minnie (5),1.50
Ax,Pipocas,1.00
 vendas.csv
ID,Qt
B1,100
B2,10
Note que cada ficheiro tem, como primeira linha, os nomes dos v´arios campos.
A linguagem TQL (Text Query Language) suportar´a os seguintes comandos:
Manuseamento de Tabelas
 LOAD TABLE produtos FROM "produtos.csv"; Carrega o ficheiro CSV indicado para mem´oria,
armazenando-o com o nome produtos.
 DISCARD TABLE produtos; Remove os dados da tabela produtos da mem´oria.
 SAVE TABLE produtos AS "produtos2.csv"; Guarda uma tabela de mem´oria para ficheiro.
 SHOW TABLE produtos; Lista uma tabela no ecr˜a.
Execu¸c˜ao de Queries
 SELECT * FROM produtos; Lista todas as linhas e colunas da tabela indicada.
 SELECT ID,Descricao FROM produtos; Lista todas as linhas, mas apenas as colunas indicadas.
 SELECT * FROM vendas WHERE Qt > 50; Lista todas as linhas que respondam a determinada condi¸c˜ao.
Sugere-se a possibilidade de permitir mais do que uma condi¸c˜ao, separadas por AND.
2
 Poder˜ao ser realizados diferentes tipos de compara¸c˜ao: igualdade (=), desigualdade (<>), bem como
as quatro compara¸c˜oes (<,>, <= and >=).
 Aos exemplos anteriores poder´a ainda ser adicionado o modificador LIMIT n para limitar o n´umero
de resultados apresentados ao valor n indicado.
Cria¸c˜ao de novas Tabelas
E poss´ıvel criar novas tabelas em mem´oria a partir de ´ queries e de outras tabelas:
 CREATE TABLE mais vendidos FROM SELECT * FROM vendas WHERE Qt > 50; Armazena numa nova
tabela o resultado do query, permitindo para que se possa mais tarde armazenar o resultado num
ficheiro.
 CREATE TABLE tudo FROM vendas JOIN produtos USING(ID); Para juntar tabelas pode-se criar
uma nova tabela. Ao contr´ario do SQL, a jun¸c˜ao de tabelas n˜ao ir´a permitir a sele¸c˜ao de colunas
ou linhas, obrigando sempre `a uni˜ao completa de duas tabelas.
Procedimentos
E poss´ıvel criar procedimentos. Os procedimentos s˜ao declarados usando o comando ´ PROCEDURE, e terminam com o comando END:
PROCEDURE atualizar_vendas DO
CREATE TABLE mais_vendidos FROM SELECT * FROM vendas WHERE Qt > 50;
CREATE TABLE tudo FROM vendas JOIN produtos USING(ID);
END
Os procedimentos podem ser executados usando o comando CALL, por exemplo, CALL atualizar vendas;.
A avalia¸c˜ao deste trabalho ter´a em conta:
 A qualidade do reconhecedor l´exico e da gram´atica implementados;
 A organiza¸c˜ao e qualidade do c´odigo Python desenvolvido;
 A estrutura da Arvore Abstrata de Sintaxe; ´
 A quantidade de operadores do TQL implementados;
Note-se que n˜ao ser˜ao considerados como avalia¸c˜ao positiva solu¸c˜oes que apenas aceitem os exemplos
descritos neste enunciado. A solu¸c˜ao deve ser pensada como gen´erica, com capacidade de adapta¸c˜ao.


*And e using nao funcionais
