# Homework: IELTS Reflection Agent with LangGraph

## Assignment

Build a Reflection Agent using LangGraph that generates, evaluates, and improves an IELTS Writing Task 2 essay through an iterative workflow.

## Objectives

- Learn LangGraph fundamentals
- Build a multi-node workflow
- Implement a reflection loop
- Use structured output for evaluation
- Prevent infinite loops with a maximum retry limit

## Workflow

```text
START
  │
Writer
  │
Checker
  │
 ├── PASS ──► END
 │
 └── FAIL ──► Writer
```

## Technologies

- LangGraph
- LangChain
- Google Gemini
- Pydantic
- Python

## What I Implemented

- Writer node for IELTS essay generation
- Checker node for essay evaluation
- Router node for workflow control
- Conditional edges
- Reflection loop
- Structured output using Pydantic
- CLI application with live progress
- Maximum attempt limit

## Repository

Project source code:

https://github.com/Sanjarbek1024/LangGraph-learning