import array as arr

#a=arr.array('d', [1.2, 1.3, 2.3])
#print(a)


#Escreva uma função com protótipo int soma (Celula *ini);que recebe uma lista encadeada ini de números inteiros e devolve a soma dos números na lista. Suponha que a lista encadeada não tem cabeça de lista.
#num= [0,1,2,3,4,5]
#def soma(lista):
    #total = 0
    #for n in lista:
         #total += n
    #return total
#print(soma(num)) 
#Escreva uma função com protótipo int conta (apont p, int x);que recebe uma lista encadeada ini de números inteiros e um inteiro x, e devolve o número de vezes que x aparece na lista. Suponha que a lista encadeada não tem cabeça de lista.
listt=[1,2,3,'x',6,9,'x',8]

def buscar(lista):
     achado = 0
     for x in lista:
        if x =='x':
          achado += 1
     return achado

print(buscar(listt))

#Considere as declarações que recebe uma lista encadeada ini de números inteiros e devolve TRUE se a lista está em ordem crescente e FALSE caso contrário. Suponha que a lista encadeada não tem cabeça de lista.
#define FALSE 0
#define TRUE  1

def verificar(lista):
   for i in range(len(lista) - 1):
      if lista[i] > lista[i + 1]:
         return False
   return True