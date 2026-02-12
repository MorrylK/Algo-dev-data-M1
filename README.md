# TP - APPLICATION MÉTÉO
### Par KOUEMO TIENTCHEU Yvan Morryl

## CONFIG
- Python `3.12`

## EXÉCUTION
- Création d'un environnement virtuel: `python -m venv myEnv`
- Activation de l'environnement virtuel:
    - sous windows: `myEnv\scripts\activate`
    - sous linux/macos: `source myEnv/bin/activate`
- Installation des librairies: `pip install -r requirements.txt`
- Lancement de l'application: `python -m appmeteo`

## EXÉCUTION AVEC DOCKER
- Construire le conteneur : `docker-compose build`
- Lancer avec docker compose : `docker-compose run --rm appmeteo`

## LINTER
- Test avec PyLint: `pylint appmeteo/`

## TESTS UNITAIRES
- Lancer les tests: `python -m pytest tests`
- Obtenir le test coverage: `python -m pytest --cov=appmeteo`