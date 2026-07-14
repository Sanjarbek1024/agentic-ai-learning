# Homework

I created this homework in a separate repository.

You can find the complete implementation here:

**Repository:** https://github.com/Sanjarbek1024/production-chat-api.git

---

## Project structure

```
main.py           # the actual chat loop
app/
  config.py       # loads .env
  database.py     # SQLAlchemy engine + session
  models.py       # User, ChatRoom, Message tables
  llm.py          # talks to Gemini
  crud.py         # database operations + chat logic
```