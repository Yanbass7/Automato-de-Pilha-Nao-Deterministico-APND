Autômato de Pilha Não-Determinístico (APND)

Descrição
Implemente um algoritmo que simule um APND. A entrada consiste da especificação de um APND
e de um conjunto de palavras. A saída consiste de uma lista indicando ‘S’ caso o APND reconheça a
palavra em questão e ‘N’ caso contrário. A palavra vazia (λ) será indicada pelo caractere *. O
trabalho deve ser acompanhado de um relatório especificado mais adiante.

Observações:
1. Leitura e entrada na entrada/saída padrão.
2. Qualquer divergência da saída com o formato especificado implicará em nota zero.
3. A implementação não pode fazer uso de recursão.
4. Critério de reconhecimento: pilha vazia e estado final.

Entrada
Na primeira linha, há uma lista de estados. Na segunda linha, há o alfabeto de entrada. Na terceira
linha, há o alfabeto de pilha. Na quarta linha, há o número total n de transições. Para cada uma das n
linhas seguintes, há uma quíntupla <a, b, c, d, e> onde ‘a’ é o estado de origem, ‘b’ é o caractere a
ser lido, ‘c’ é o símbolo a ser desempilhado, ‘d’ é o estado de destino e, por fim, ‘e’ é a palavra a ser
empilhada. Em seguida, há um caractere informando o estado inicial. Na próxima linha, há uma
lista de estados finais. Por fim, há uma lista de palavras de teste a ser reconhecida. Os itens da listas
serão separados por espaço em branco. A palavra vazia (λ) é representada por *.

Saída
Seu programa deve imprimir para cada palavra de teste ‘S’ se o APND reconhece a palavra ou ‘N’
caso contrário.

Exemplos

Entrada                Saída
0 1                      S
a b                      S 
A                        N 
3                        N
0 a * 0 A                N
0 * * 1 *
1 b A 1 *
0
1
* ab ba abb aab
