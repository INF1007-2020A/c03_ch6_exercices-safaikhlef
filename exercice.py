#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> bool:
    if values is None:
        # TODO: Demander les valeurs ici
        pass
    
     ma_liste = [] 
     while len(ma_liste) < 10:
         ma_liste.append(int(input("Veuillez entrer un nombre entier : ")))
      
        
     resultat = True
     index = 0
     while index < len(ma_liste) - 1:
         if ma_liste[index] > ma_liste[index+1]:
              resultat = False
              break
         index += 1  
     print(resultat)
        
        
       # print(ma_liste == sorted(ma_liste))
                
           
    return False


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: Demander les mots ici
        pass
    
    mot1 = 'ALEVIN'
    mot2 = 'NIVELA'
    mot1 = list(mot1)
    mot2 = liste(mot2)
    
    if len(mot1) == len(mot2):
        for lettre in mot1:
            if lettre in mot2:
                mot2.remove(lettre)
        if len(mot2) == 0:
            print('Anagramme')
        else:
            print('raté')
            
    #print(sorted(mot1) == sorted(mot2))

    return False


def contains_doubles(items: list) -> bool:
    print(set(liste))
    print(len(Liste) == len(set(liste)))


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return {}


def histogram(sentence: str) -> tuple:
    # TODO: Créer l'histogramme a l'aide d'un dictionnaire
    #       Afficher l'histogramme et les lettres les plus fréquentes
    #       Retourner l'histogramme et le tableau de lettres

    phrase = "Bonjour, c'est mercredi."
    
    phrase_set = set(phrase)
    resultat = {}
    for lettre in phrase_set:
        resultat[lettre] = phrase.count(lettre)
    
    #print(resultat)
    
   # resultat = {}
    #for lettre in phrase:
      #  if lettre not in resultat:
       #     resultat[lettre] = 0
       # else:
        #    resultat[lettre] += 1
    return {}, []


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données 
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    name, result = best_grades(grades)
    print(f"{name} a la meilleure moyenne: {result}")
    
    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
