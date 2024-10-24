# README : Mise en Place de l'Environnement pour Exécuter le Code de Comparaison des Formats de Sérialisation

Ce guide vous aidera à mettre en place l'environnement nécessaire pour exécuter le code de comparaison des performances des formats de sérialisation **JSON**, **Avro** et **Protobuf**. Vous trouverez ci-dessous les étapes détaillées pour installer les dépendances, générer les fichiers nécessaires et exécuter le script.

## Table des Matières

1. [Pré-requis](#pré-requis)
2. [Installation de Python](#installation-de-python)
3. [Création d'un Environnement Virtuel](#création-dun-environnement-virtuel)
4. [Installation des Dépendances Python](#installation-des-dépendances-python)
5. [Installation du Compilateur Protobuf (`protoc`)](#installation-du-compilateur-protobuf-protoc)
6. [Création du Fichier `person.proto`](#création-du-fichier-personproto)
7. [Génération du Fichier `person_pb2.py`](#génération-du-fichier-person_pb2py)
8. [Téléchargement du Script Python](#téléchargement-du-script-python)
9. [Exécution du Script](#exécution-du-script)
10. [Résolution des Problèmes Courants](#résolution-des-problèmes-courants)
11. [Ressources Supplémentaires](#ressources-supplémentaires)

---

## Pré-requis

- Système d'exploitation : Windows, macOS ou Linux
- **Python 3.6** ou supérieur installé
- Accès à Internet pour installer les dépendances

---

## Installation de Python

### Vérifier si Python est déjà installé

Ouvrez un terminal (ou une invite de commandes sous Windows) et exécutez :

```bash
python --version
```

Ou

```bash
python3 --version
```

Si Python est installé, la version sera affichée.

### Installer Python

Si Python n'est pas installé, téléchargez-le depuis le site officiel :

- [Télécharger Python](https://www.python.org/downloads/)

Suivez les instructions d'installation pour votre système d'exploitation.

---

## Création d'un Environnement Virtuel

Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances du projet.

### Créer un environnement virtuel

Dans votre terminal, naviguez vers le répertoire où vous souhaitez placer le projet et exécutez :

```bash
python -m venv venv
```

Cela créera un environnement virtuel nommé `venv`.

### Activer l'environnement virtuel

- **Sous Windows :**

  ```bash
  venv\Scripts\activate
  ```

- **Sous macOS/Linux :**

  ```bash
  source venv/bin/activate
  ```

Vous devriez voir `(venv)` apparaître au début de votre invite de commande, indiquant que l'environnement virtuel est actif.

---

## Installation des Dépendances Python

Avec l'environnement virtuel activé, installez les bibliothèques nécessaires :

```bash
pip install protobuf fastavro
```

- **`protobuf`** : Pour travailler avec Protocol Buffers.
- **`fastavro`** : Pour une sérialisation/désérialisation Avro performante.

---

## Installation du Compilateur Protobuf (`protoc`)

Le compilateur `protoc` est nécessaire pour générer les fichiers Python à partir des fichiers `.proto`.

### Vérifier si `protoc` est installé

Exécutez :

```bash
protoc --version
```

Si une version est affichée, `protoc` est installé.

### Installer `protoc`

#### Sous Windows

1. Téléchargez le package binaire pour Windows depuis les [releases de Protocol Buffers](https://github.com/protocolbuffers/protobuf/releases).

   - Choisissez la version appropriée, par exemple `protoc-3.21.12-win64.zip`.

2. Décompressez le fichier ZIP dans un répertoire de votre choix, par exemple `C:\protoc`.

3. Ajoutez le chemin vers `protoc.exe` à la variable d'environnement `PATH`.

   - Recherchez "Variables d'environnement" dans le menu Démarrer.
   - Modifiez la variable `PATH` et ajoutez `C:\protoc\bin`.

#### Sous macOS/Linux

1. Utilisez `homebrew` (macOS) ou téléchargez le binaire directement.

   - **macOS avec Homebrew :**

     ```bash
     brew install protobuf
     ```

   - **Linux ou sans Homebrew :**

     Téléchargez le package binaire depuis les [releases de Protocol Buffers](https://github.com/protocolbuffers/protobuf/releases), par exemple `protoc-3.21.12-linux-x86_64.zip`.

     Décompressez le fichier et placez `protoc` dans `/usr/local/bin` :

     ```bash
     unzip protoc-3.21.12-linux-x86_64.zip -d protoc
     sudo mv protoc/bin/protoc /usr/local/bin/
     sudo mv protoc/include/* /usr/local/include/
     ```

2. Vérifiez l'installation en exécutant :

   ```bash
   protoc --version
   ```

---

## Création du Fichier `person.proto`

Créez un fichier nommé `person.proto` dans le répertoire de votre projet avec le contenu suivant :

```proto
syntax = "proto3";

message Person {
  string name = 1;
  int32 id = 2;
  bool active = 3;
  repeated string hobbies = 4;
}

message PersonList {
  repeated Person people = 1;
}
```

---

## Génération du Fichier `person_pb2.py`

Générez le fichier Python à partir du fichier `.proto` en exécutant :

```bash
protoc --python_out=. person.proto
```

- `--python_out=.` indique que le fichier généré `person_pb2.py` sera placé dans le répertoire courant.
- Assurez-vous que `person.proto` est dans le répertoire courant.

Vérifiez que `person_pb2.py` a été créé.

---

## Téléchargement du Script Python

Créez un fichier nommé `serialization_comparison.py` et copiez-y le code suivant :

```python
# Code complet du script fourni précédemment
# Assurez-vous d'inclure le code avec fastavro et les modifications pour optimiser les performances
```

**Note :** Remplacez le commentaire par le code complet que vous avez développé pour comparer les formats de sérialisation.

---

## Exécution du Script

Assurez-vous que votre environnement virtuel est activé, puis exécutez le script :

```bash
python serialization_comparison.py
```

Le script va :

- Générer les données
- Sérialiser et désérialiser avec chaque format (JSON, Protobuf, Avro)
- Mesurer et afficher les performances pour chaque format

---

## Résolution des Problèmes Courants

### Erreur `protoc: command not found`

- Assurez-vous que `protoc` est installé et que son chemin est ajouté à la variable d'environnement `PATH`.
- Vérifiez l'installation en exécutant `protoc --version`.

### Erreur `ModuleNotFoundError: No module named 'person_pb2'`

- Assurez-vous que `person_pb2.py` a été généré dans le même répertoire que votre script.
- Vérifiez que vous avez exécuté `protoc --python_out=. person.proto` dans le bon répertoire.

### Problèmes de Versions de Python

- Ce script nécessite Python 3.6 ou supérieur.
- Vérifiez votre version de Python avec `python --version`.
- Si plusieurs versions de Python sont installées, assurez-vous d'utiliser la bonne version et ajustez les commandes en conséquence (`python3` au lieu de `python`).

### Erreurs lors de l'Installation des Packages

- Assurez-vous que votre environnement virtuel est activé.
- Si vous rencontrez des erreurs de permissions, utilisez `pip install --user package_name` ou vérifiez les permissions de votre environnement.

### Problèmes de Mémoire

- Le script génère un grand volume de données et peut consommer beaucoup de mémoire.
- Si vous rencontrez des problèmes de mémoire insuffisante, réduisez le nombre de données générées en modifiant la ligne :

  ```python
  personnes = [generate_random_person() for _ in range(100000)]
  ```

  Par exemple, utilisez `10000` au lieu de `100000`.

---

## Ressources Supplémentaires

- **Documentation de Protobuf :** [https://developers.google.com/protocol-buffers/docs/pythontutorial](https://developers.google.com/protocol-buffers/docs/pythontutorial)
- **Documentation de fastavro :** [https://fastavro.readthedocs.io/en/latest/](https://fastavro.readthedocs.io/en/latest/)
- **Documentation de Python venv :** [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)
- **Guide sur les Environnements Virtuels :** [https://realpython.com/python-virtual-environments-a-primer/](https://realpython.com/python-virtual-environments-a-primer/) (en anglais)


---

**Note :** Ce guide est fourni à titre informatif et peut nécessiter des ajustements en fonction de votre environnement spécifique. N'hésitez pas à adapter les instructions pour répondre à vos besoins.
