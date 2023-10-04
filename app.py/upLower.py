txt = "Hello World"
#txt = txt.upper() Deixar grande
txt = txt.lower()#Lower deixar minusculo
print(txt)

#TROCAR LETRAS
txt1 = "Hello World"
txt1 = txt1.replace("H", "B")
print(txt1)

#OPERADOR DE ASSOCIAÇAO IN
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")
  
#OPERADOR DE COMPARACAO NAO E =
if 5 != 10:
  print("5 and 10 is not equal")
  
#OPERADOR OR = OU
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")
  
#OPERADOR IMPRIMIR SELECAO 1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#ALTERAR NOMES
fruits1 = ["apple", "banana", "cherry"]
fruits1[0] = "kiwi"
print(fruits)

#METODO ADICIONAR append vai final fila
fruits2 = ["apple", "banana", "cherry"]
fruits2.append("Orenge")
print(fruits2)

#ADICIONAR na posicao quer tipo 1
fruits3 = ["apple", "banana", "cherry"]
fruits3.insert(1,"lemon")
print(fruits3)

#REMOVER DA LISTA com remove
fruits4 = ["apple", "banana", "cherry"]
fruits4.remove("banana")
print(fruits4)


#INDEXACAO NEGATIVA ULTIMO FILA
fruits5 = ["apple", "banana", "cherry"]
print(fruits5[-2])

#INPRIMIR SELECAO
fruits6 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits6[2:5])

#IMPRIMIR QUANTIDADE LISTA
fruits7 = ["apple", "banana", "cherry"]
print(len(fruits7))

#IMPRIMIR 1 DA TUPLA OU LIST
fruits8 = ("apple", "banana", "cherry")
print(fruits8[1])

#IMPRIMIR QUNATIDADE TUPLA
fruits9 = ("apple", "banana", "cherry")
print(len(fruits9))

#ULTIMO DA LIST TUPLA
fruits10 = ("apple", "banana", "cherry")
print(fruits10[-1])

#ADICIONA LIST
fruits11 = {"apple", "banana", "cherry"}
fruits11.add("orange")
print(fruits11)

#ADICIONAR VARIOS
fruits12 = {"apple", "banana", "cherry"}
more_fruits12 = ["orange", "mango", "grapes"]
fruits12.update(more_fruits12)
print(fruits12)

#REMOVER DA LISTA COM discard
fruits13 = {"apple", "banana", "cherry"}
fruits13.discard("cherry")
print(fruits13)


#IMPRIMIR VALOR DO ITEM TIPO MODEL
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#ALTERAR CONFIGURAÇÃO NO CASO ANO
car2 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car2["year"] = 2020
#ADICIONA COR LISTA
car2["color"] = "red"
#REMOVER MODELO COM pop
car2.pop("model")
#ESVAZIAR DICIONARIO
car2.clear()
print(car2)

#CONDIÇÃO se MAIOR OU MENOR OU = += -= ==
g = 50
h = 10
if g > h:
    print("Hello World")
    
#!= NÃO É = A
e = 50
f = 10
if e != f:
  print("Hello World")
  
#== FUNÇÃO IF=se ELSE=senão
a = 50
c = 10
if a == c:
  print("Yes")
else:
  print("No")

#CASO CONTRARIO IF=SE ELIF=CASO CONTRARIO ELSE=SENAO  
d = 50
b = 10
if d == b:
  print("1")
elif d > b:
  print("2")
else:
  print("3")

#FUNCÃO SE INDEXAOCAO PULAR LINHA
  if 5 > 2:
      print("Five is greater than two!")
#FUNCAO SE INDEXACAO MESMA LINHA
if 6 > 2: print("Six is greater than two!")
  
#SINTAXE DE MÃO CURTA  
print("Yes") if 7 > 2 else print("No")

#WHILE = DESDE QUE SEJA INFERIOR 
#IRA IMPRIMIR UMA LISTA ATE NUMERO REFERIDO NO CASO 6
i = 1
while i < 6:
  print(i)
  i += 1

#WHILE PARA COM BREAK
m = 1
while m < 6:
  if m == 3:    
      break
  m += 1
  print(m)

#ENQUANTO + SENAO
n = 1
while n < 6:
  print(n)
  n += 1
else:
  print("i is no longer less than 6")
  
#LOOP DA LIST[] FOR X IN FRUITS14:
fruits14 = ["apple", "banana", "cherry"]
for x in fruits14:
  print(x)
  
#
fruits15 = ["apple", "banana", "cherry"]
for x in fruits15:
  if x == "banana":
    continue
  print(x)