# Utilise une image de base officielle de Python
FROM python:3.9

# Définit le répertoire de travail
WORKDIR /app

# Copie les fichiers de votre application dans le répertoire de travail
COPY . /app

# Installe les dépendances
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose le port utilisé par l'application
EXPOSE 8000

# Démarre le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
