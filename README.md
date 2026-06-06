# Uruchomienie projektu
1. Instalacja zależności:
```bash
pip install -r requirements.txt
```
2. Uruchomienie PostgreSQL i Metabase:
```bash
docker compose up -d
```
3. Wygenerowanie danych:
```bash
python src/generate_transactions.py
```
4. Załadowanie danych do PostgreSQL:
```bash
python src/load_to_postgres.py
```
5. Otwarcie Metabase:

W przeglądarce ```http://localhost:3000```

7. Dodanie połączenia PostgreSQL:
```
Host: postgres
Port: 5432
Database: ntpd
Username: bi
Password: bi
```
