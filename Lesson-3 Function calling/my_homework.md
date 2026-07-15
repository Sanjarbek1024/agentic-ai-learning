## AI SQL Agent (Function Calling + Database)

I created this homework in a separate repository.
You can find the complete implementation here:

Repository: https://github.com/Sanjarbek1024/ai-db-agent

The project demonstrates:

* Gemini API function calling to convert natural language questions into SQL
* A dedicated security layer (`sql_guard.py`) that only allows SELECT queries on whitelisted tables
* SQLite database with a sample marketplace dataset (categories, sellers, listings)
* FastAPI backend with a Jinja2 + AJAX frontend
* Read-only database connection as a second layer of protection against unsafe queries