# n8n Memory Chat System — Full Tutorial (Beginner → Working App)

Goal of this guide: take you from **zero n8n experience** to a **working chat app with memory**, matching every point in your homework.

---

## 1. What is n8n?

**Concept**
n8n is a **visual automation platform**. Instead of writing a Python script line by line, you connect **boxes (nodes)** on a canvas. Each node does one job: receive input, call an API, save to a database, etc. Connected together, they form a **workflow**.

**Why it exists**
- Building integrations (Slack → Database → Email → AI) normally means writing and maintaining glue code.
- n8n lets you build that glue **visually**, and still drop into JavaScript/Python code nodes when you need custom logic.
- For AI specifically, n8n has native **LangChain-style nodes**, so you can build agents with memory and tools without writing a RAG/agent framework yourself.

**How it works (core vocabulary)**

| Term | What it means | Example |
|---|---|---|
| **Workflow** | The whole canvas — a saved automation made of connected nodes | "Chat With Memory" workflow |
| **Node** | A single step/box that does one job | "OpenAI Chat Model" node |
| **Trigger** | A special node that starts the workflow | "Chat Trigger" (fires when a user sends a message) |
| **Credential** | Saved API key/login n8n reuses across nodes | Your OpenAI API key |
| **Sub-node** | A node that plugs *into* another node instead of running standalone (used for AI) | Memory node plugs into the AI Agent node |

**Big picture for your project:**

```
User message
   ↓
Chat Trigger (entry point, gives each user a session_id)
   ↓
AI Agent node  ←→  Chat Model (the actual LLM, e.g. OpenAI)
   ↓        ↖
   ↓         Memory node (reads/writes past messages using session_id)
Response back to user
```

---

## 2. Setting Up n8n

You have two options — pick one to start:

**Option A — n8n Cloud (fastest, recommended for homework)**
1. Go to n8n.io → sign up for a free trial account.
2. You land straight in the workflow editor. No installation needed.

**Option B — Self-hosted with Docker (if you want full local control)**
```bash
docker volume create n8n_data
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v n8n_data:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n
```
Then open `http://localhost:5678` in your browser.

Since you're doing Python/FastAPI already, self-hosting will feel familiar (it's just another local service on a port). But for a first homework, **Cloud is less friction** — go with that unless you specifically want the Docker practice.

---

## 3. Step-by-Step: Building the Chat Workflow

### Step 1 — Create a new workflow
- Click **"+ Add workflow"**.
- Rename it to something like `Memory Chat System`.

### Step 2 — Add the Chat Trigger node
- Click the **+** on the empty canvas → search **"Chat Trigger"** → add it.
- This node is special: it gives you a **built-in chat UI** to test with, and automatically generates a `sessionId` per conversation — this is exactly the "user input" node your homework asks for.
- In the node settings, you can toggle **"Public"** if you eventually want a shareable URL. For homework testing, keep it private/local.

### Step 3 — Add the AI Agent node
- Click **+** after the Chat Trigger → search **"AI Agent"** → add it.
- Set its mode to **"Tools Agent"** (the standard, most flexible option — used ~90% of the time).
- This node is the "brain." It doesn't work alone — it needs two things plugged into its bottom connectors:
  1. A **Chat Model** (the LLM itself)
  2. A **Memory** node

### Step 4 — Connect an AI Chat Model (OpenAI)
- On the AI Agent node, click the **Chat Model** connector (bottom of the node) → add **"OpenAI Chat Model"**.
- Create a credential: paste your OpenAI API key (from platform.openai.com → API keys).
- Pick a model, e.g. `gpt-4o-mini` (cheap/fast — good for testing).

> If you don't want to pay for OpenAI credits, you can swap this later for a local model via **Ollama Chat Model** node — same Agent, same Memory, just a different Chat Model credential. Good to know since you're already experimenting with local LLMs (GGUF/llama.cpp).

### Step 5 — Add a System Prompt
- In the AI Agent node, set the **System Message**, e.g.:
```
You are a helpful assistant. Use the conversation history to stay
consistent with earlier answers. If the user refers to something
they said before, recall it correctly.
```
This is what makes testing memory obvious later — the model will explicitly reference earlier messages.

---

## 4. Adding Memory (the core of your homework)

**Concept**
By default, an LLM call is **stateless** — every message is "the first message ever." Memory nodes solve this by storing previous turns and feeding them back into every new call.

**Why it exists**
Without memory: user says "My name is Sanjar" → next message "What's my name?" → model has no idea.
With memory: the Memory node stores that exchange and re-sends it as context automatically.

**How it works — pick ONE for your homework:**

### Option A — Simple Memory (fastest, in-workflow, good for homework demo)
- Click the **Memory** connector on the AI Agent node → add **"Simple Memory"**.
- Set:
  - **Session Key** → use the Chat Trigger's `sessionId` (this is what keeps each user's conversation separate)
  - **Context Window Length** → e.g. `10` (keeps the last 10 messages)
- ⚠️ Important limitation: Simple Memory is **volatile** — it's stored only in the running workflow, and is lost when n8n restarts. Perfect for a homework demo, **not** for real production.

### Option B — Postgres Chat Memory (persistent, matches your "database" requirement)
Since you already work with SQL, this is the more "complete app" version:
1. Add a **Postgres** node/credential (or use SQLite if you don't have a Postgres server — n8n also has a Postgres-compatible option via Supabase free tier if you need one quickly).
2. Add **"Postgres Chat Memory"** as the Memory sub-node instead of Simple Memory.
3. Configure:
   - **Session ID** → the Chat Trigger's `sessionId`
   - Table name (n8n auto-creates the schema needed)
4. Now chat history survives restarts — real persistence, not just RAM.

**Recommendation for your homework:** Build it with **Simple Memory first** (get it working end-to-end fast), then swap in **Postgres Chat Memory** to show you understood the "real" persistent version too. Same Agent, same Chat Trigger — you only swap one sub-node.

---

## 5. Testing the Memory (matches homework Step 5)

1. Click **"Chat"** at the bottom of the Chat Trigger node — this opens n8n's built-in test chat window.
2. Send: `Hi, my name is Sanjar and I'm building an ML app in FastAPI.`
3. Send a follow-up: `What's my name, and what am I building?`
4. ✅ If memory works: the agent answers correctly using both facts.
5. ❌ If it doesn't: check that the **Session Key/ID** field on the Memory node is actually pulling the Chat Trigger's `sessionId` (a common mistake is leaving it as a fixed static value instead of an expression referencing the session).

To simulate "different users," open the chat in a new private/incognito window — Chat Trigger gives it a new `sessionId`, and the two conversations should **not** mix.

---

## 6. Full Architecture Recap

```
[Chat Trigger]  --sessionId + message-->  [AI Agent]
                                              │  ├─ Chat Model  → OpenAI (gpt-4o-mini)
                                              │  └─ Memory      → Simple Memory / Postgres Chat Memory
                                              ▼
                                        Response → back to Chat Trigger UI
```

This maps 1:1 onto your homework checklist:

| Homework requirement | n8n implementation |
|---|---|
| Workflow / Nodes / Triggers | Whole canvas = workflow, each box = node, Chat Trigger = trigger |
| User input node | Chat Trigger |
| AI integration | AI Agent + OpenAI Chat Model |
| Memory | Simple Memory (or Postgres Chat Memory for persistence) |
| Context kept across messages | Session ID links memory to the right conversation |
| Testing | Built-in Chat window, multi-turn test |

---

## 7. Common Beginner Mistakes

- **Forgetting the Session Key expression** → every user shares one memory, or memory resets every message.
- **Using Simple Memory in a "production" deployed workflow with queue mode on** → n8n explicitly warns this breaks, since different workers might handle each request. Use Postgres/Redis Chat Memory for real deployments.
- **Vague system prompt** → agent ignores memory context. Be explicit: "use the conversation history."
- **Testing with only one message** → memory bugs only show up on the *second* message onward. Always test at least 2–3 turns.

---

## 8. Next Steps (beyond the homework, if you want to push further)

- Add a **Tool** (e.g., HTTP Request node) so the agent can call your own FastAPI `/predict` endpoint mid-conversation — connecting this n8n chat directly to your ML prediction app.
- Swap OpenAI for a **local GGUF model via Ollama**, matching your llama.cpp/quantization interests, with zero other changes to the workflow.
- Move Session IDs into a proper table (user_id ↔ session_id mapping) once you go from "demo" to "real app."
