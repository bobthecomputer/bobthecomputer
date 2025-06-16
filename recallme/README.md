# RecallMe Demo

Ceci est une démonstration simplifiée de l'application **RecallMe**. L'idée est de montrer comment croiser une liste de rappels produits avec vos achats.

Le script `main.py` charge une liste factice de rappels et une liste d'achats depuis `purchases.csv`, puis affiche les produits concernés.

Dans un projet réel, on utiliserait l'API officielle RappelConso, mais cette démo utilise des données locales pour faciliter les tests.

## Utilisation

1. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
2. Lancer le script :
   ```bash
   python main.py
   ```

3. Ouvrir l'interface graphique (facultatif) :
   ```bash
   python -m recallme.gui
   ```

Cette interface utilise Tkinter pour afficher une fenêtre et énumérer les
produits rappelés détectés dans vos achats.

Vous devriez voir la liste des produits achetés faisant l'objet d'un rappel sanitaire.
