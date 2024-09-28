import os
from ex1_chf_vigenere import *
from ex2_dechf_vigenere import *

def VigenereMenu():

    EntreeUtilisateur : str
    Clef : str
    Chiffrement : bool

    os.system("cls")
    print("~ Chiffrement de Vigenere ~")
    print("1. Chiffrer quelque chose")
    print("2. Déchiffrer quelque chose")
    print("3. Afficher des tests de chiffrement")
    print("4. Afficher des tests de déchiffrement")
    print("5. Quitter\n")
    choice = input("Entrez votre choix: ")

    if choice == "1":
        os.system("cls")
        print("1. Chiffrer quelque chose")
        EntreeUtilisateur = input("Entrez le mot à chiffrer: ")
        Clef = input("Entrez la clé de chiffrement: ")
        print(chiffrementVigenere(EntreeUtilisateur, Clef))
        print()

    elif choice == "2":
        os.system("cls")
        print("2. Déchiffrer quelque chose")
        EntreeUtilisateur = input("Entrez le mot à déchiffrer: ")
        Clef = input("Entrez la clé de déchiffrement: ")
        print(DechiffrementVigenere(EntreeUtilisateur, Clef))
        print()

    elif choice == "3":
        os.system("cls")
        print("3. Afficher des tests de chiffrement")
        chiffrementVigenereTests()
        print()

    elif choice == "4":
        os.system("cls")
        print("4. Afficher des tests de déchiffrement")
        dechiffrementVigenereTests()
        print()

    elif choice == "5":
        print("A bientôt !\n")
        return 
    
    else:
        print("Choix invalide")
        VigenereMenu()

VigenereMenu()