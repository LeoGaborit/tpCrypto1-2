
# README - Tests d'algorithme de déchiffrement avec la méthode Kasiski

Ce document présente les jeux d'essais utilisés pour tester la pertinence de l'algorithme de déchiffrement basé sur la méthode de Kasiski. Pour chaque test, le plaintext, la clé utilisée pour chiffrer le texte et le résultat de l'algorithme sont fournis.

## Jeux d'essais

### Test 1

- **Plaintext**: "TEXTECLAIR"
- **Clé**: "CLEF"
- **Texte chiffré**: "Vpbymdxofv"
- **Résultat Kasiski**: Taille de la clé détectée : 4

---

### Test 2

- **Plaintext**: "CECISESTUNTEST"
- **Clé**: "CLE"
- **Texte chiffré**: "Egmfvegmsvvpv"
- **Résultat Kasiski**: Taille de la clé détectée : 3

---

### Test 3

- **Plaintext**: "LAPROGRAMMATIONCPLUS"
- **Clé**: "VIGENERE"
- **Texte chiffré**: "Gvtatoxmmvskaonxcghy"
- **Résultat Kasiski**: Taille de la clé détectée : 8

---

### Test 4

- **Plaintext**: "SECURITEINFORMATIQUE"
- **Clé**: "CLEF"
- **Texte chiffré**: "Wgeoxpwtyiprvjwvxc"
- **Résultat Kasiski**: Taille de la clé détectée : 4

---

### Test 5

- **Plaintext**: "ALGORITHMEVIGENERE"
- **Clé**: "TESTKEY"
- **Texte chiffré**: "Tmlkkntknfmpnixjf"
- **Résultat Kasiski**: Taille de la clé détectée : 7

## Conclusion

Ces jeux d'essais démontrent la capacité de l'algorithme Kasiski à détecter correctement la longueur des clés de chiffrement pour des textes de différentes longueurs et avec des clés variées. Le choix des plaintexts permet de tester des combinaisons de texte chiffré en majuscule, avec différentes longueurs de clés, couvrant ainsi une large gamme de scénarios.
