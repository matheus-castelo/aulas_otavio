# Capítulo 1
## Exercícios (12)

### 1. List Comprehensions
1. Escreva um código em Python que receba um inteiro positivo `n` e retorne a soma dos quadrados de todos os inteiros positivos menores do que `n`.
2. Escreva um código em Python que receba um inteiro positivo `n` e retorne a soma dos quadrados de todos os inteiros positivos pares menores do que `n`.

### 2. Tuples
1. Escreva uma função em Python que receba uma sequência de um ou mais números e retorne o menor e o maior número na forma de uma tupla de tamanho 2.
2. Escreva uma função em Python que receba uma sequência de números e determine se todos os números são diferentes entre si.

### 3. Problemas e Soluções
1. **Mensagem com f-strings**  
   - **Enunciado:** Escreva um programa que leia o nome e a idade de uma pessoa e exiba uma mensagem formatada usando f-strings.  
   - **Solução:** Leia os dados com `input()`, armazene-os em variáveis e use uma f-string para exibir a mensagem com as informações.

2. **Estatísticas de uma lista**  
   - **Enunciado:** Receba uma lista de números inteiros e exiba a soma, o maior e o menor valor, e a média dos números.  
   - **Solução:** Utilize funções como `sum()`, `max()` e `min()` e calcule a média dividindo a soma pelo tamanho da lista.

3. **Inverter string**  
   - **Enunciado:** Crie uma função que receba uma string e retorne a string invertida.  
   - **Solução:** Percorra a string de trás para frente ou utilize slicing para gerar a string invertida.

4. **Frequência de caracteres**  
   - **Enunciado:** Crie uma função que receba uma string e retorne um dicionário com a frequência de cada caractere.  
   - **Solução:** Inicialize um dicionário e incremente o contador correspondente para cada caractere da string.

5. **Classe Produto**  
   - **Enunciado:** Implemente uma classe com atributos para nome, preço e quantidade, métodos para calcular o valor do estoque e exibir as informações.  
   - **Solução:** Crie métodos para retornar o valor do estoque (`preço × quantidade`) e outro método para exibir os atributos de forma legível.

6. **Números pares menores que um valor**  
   - **Enunciado:** Leia um número inteiro positivo e exiba todos os números pares menores que ele.  
   - **Solução:** Use um laço `for` com passo 2 ou um teste condicional dentro do laço.

7. **Diferença simétrica entre listas**  
   - **Enunciado:** Implemente uma função que receba duas listas e retorne os elementos que estão apenas em uma delas.  
   - **Solução:** Converta as listas em conjuntos e utilize a operação de diferença simétrica.

8. **Leitura com tratamento de exceções**  
   - **Enunciado:** Leia números do usuário até que ele digite um valor inválido, exibindo uma mensagem amigável.  
   - **Solução:** Use um laço `while` com `try/except` para capturar exceções de conversão e interromper a execução quando a entrada for inválida.
