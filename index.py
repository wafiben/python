""" defintion d'une fontion """

def addition(a, b):
    return a + b

result = addition(5, 3);

print(result);

""" Demander un input  """
nom = input("quel votre nom ");

print("Bonjour " , nom);

""" décalaration d'une variable """

nom ="soua";
prenonom = "Sonia";

print("Bonjour " , nom, prenonom);

""" structure conditionnelle """

age = 25;

if (age >= 18):
    print("vous êtes majeur");
else:
    print("vous êtes mineur");

n = 5;

if (n % 2 == 0):   
    print("le nombre est pair");
else:    print("le nombre est impair");

""" calcul de la moyenne de 3 nombres; """

a = 10;
b = 20;
c = 5;

def moyenne(x,y,z) : return (x + y + z) / 3;
result = moyenne(a, b, c);

print("la moyenne est : ", result);

""" max d'une fonction """
def max(a, b):
    if a > b:
        return a;
    else:
        return b;

print(max(40, -5));

""" calculer le carré d'un nombre """

def carre(x):
    return x * x;


result = carre(2);

print("le carré de 5 est : ", result);

x = 10;
y = 20;
z= 30;

def som(a,b):
    return a + b;

def carre(a):
    return a* a;

