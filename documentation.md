# Documentation Technique - Projet Météo Toulouse

## 1. Architecture Logicielle

Le projet adopte une architecture modulaire favorisant la séparation des responsabilités (SOC), la maintenabilité et l'extensibilité. Il s'appuie sur plusieurs **Design Patterns** éprouvés pour structurer le code.

### Vue d'ensemble des Modules

| Module | Rôle Principal |
| :--- | :--- |
| `appmeteo.main_objects` | Contient les objets métier (`Station`, `Record`) et le contrôleur principal (`MainProcessCommand`). |
| `appmeteo.data_extractor` | Gère la récupération des données depuis diverses sources (API, fichiers). Implemente le pattern **Strategy** pour l'extraction. |
| `appmeteo.data_structure` | Fournit des implémentations manuelles de structures de données (`LinkedList`, `Queue`). |
| `appmeteo.printing` | Gère la logique d'affichage, découplant la présentation des données de leur traitement (**Vue** dans un modèle MVC simplifié). |

---

## 2. Hiérarchie des Classes

### 2.1. Domaine Métier (Model)
Le cœur du domaine est représenté par les stations et les relevés météorologiques.

*   `Station` : Classe de base représentant une station météo (Nom, ID Capteur, Label API).
    *   `LinkedStation` (Hérite de `Station`) : Ajoute une référence `next_station` pour l'implémentation de la **Liste Chaînée**.
*   `Record` : Représente un relevé météo à un instant T (Température, Humidité, Pression, Heure), associé à une `Station`.

### 2.2. Contrôle et Flux (Command Pattern)
L'interaction utilisateur est gérée via le **Command Pattern**, permettant d'encapsuler les actions du menu sous forme d'objets.

*   `Command` (Classe Abstraite/Interface implicite) : Définit la méthode `execute()`.
    *   `TitlePrintingCommand` : Affiche le titre.
    *   `SelectMenuCommand` : Affiche le menu principal et retourne le choix utilisateur.
    *   `AllStationsPrintingCommand` : Affiche toutes les stations.
    *   `SelectSpecificStationCommand` : Permet la sélection et l'affichage de stations spécifiques.
    *   `LinkedStationsPrintingCommand` : Lance la démonstration de la liste chaînée.
    *   `QueueStationsPrintingCommand` : Lance la démonstration de la file.
*   `MainProcessCommand` (**Invoker**) : Initialise et stocke les commandes dans un dictionnaire (`map`), et orchestre la boucle principale de l'application.

### 2.3. Extraction de Données (Strategy Pattern)
L'accès aux données est abstrait via des interfaces.

*   `IDataExtractor` (Interface)
    *   `IAPIDataExtractor` (Interface pour API)
        *   `APIStations` : Implémentation concrète récupérant la liste des stations via `requests`.
        *   `APIStationExtractor` : Récupère les données temps réel pour une station donnée.

### 2.4. Affichage (Decorator Pattern / View)
L'affichage est délégué à des classes spécialisées.

*   `IPrinting` (Interface)
    *   `StationPrintingDecorator` : Utilise potentiellement le **Decorator Pattern** pour "décorer" une `Station` avec la capacité de s'afficher (en récupérant ses données temps réel).
    *   `RecordPrinting` : Affiche un objet `Record` formaté.

### 2.5. Structures de Données Personnalisées
Implémentation algorithmique de structures classiques.

*   `DataStructure` (Abstrait)
    *   `LinkedList` : Implémente une liste chaînée simple.
        *   **Complexité** : Insertion O(1) (si tête) ou O(n), Parcours O(n).
        *   Utilise `LinkedStation` comme noeuds.
    *   `Queue` : Implémente une file (FIFO).
        *   Utilise une liste Python standard (`list`) en interne.
        *   **Note technique** : L'opération `pop(0)` sur une liste Python est en O(n) (décalage des éléments). Pour une optimisation en production, `collections.deque` serait préférable (O(1)).

---

## 3. Implémentation Algorithmique

### Liste Chaînée (`LinkedList`)
La liste chaînée est construite dynamiquement à partir des données de configuration. Chaque noeud est une instance de `LinkedStation`.
*   **Intérêt** : Démonstration de la manipulation de références mémoire manuelles en Python.
*   **Utilisation** : Dans `OperateWithLinkedList`, la liste est parcourue séquentiellement (`station = station.next_station`) pour afficher les données.

### File (`Queue`)
La file est utilisée pour traiter les stations selon le principe **FIFO** (First In, First Out).
*   **Implémentation** : Wrapper autour d'une liste `list[]`.
*   **Opérations** :
    *   `add(station)` : Ajout en fin de liste (`append`).
    *   `get()` : Retrait en début de liste (`pop(0)`).
