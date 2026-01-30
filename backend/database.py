"""
Database: there is no database in Florisoft yet.
Data currently comes from:
  - Excel file (config.excel_path, e.g. dane_do_faktury.xlsx)
  - iFirma API (proformy)
  - In-memory / file outputs (PDF checklist)

To add persistence (users, sessions, app data) later you can:
  - Use SQLite: sqlalchemy + sqlite3, or dataset, or plain sqlite3
  - Use PostgreSQL if you deploy to a server
  - Keep API stateless and store only config/files as now
"""
