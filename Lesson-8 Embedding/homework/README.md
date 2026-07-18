# Lesson 8 — Embedding va RAG asoslari

## Maqsad

Embedding qanday ishlashini va RAG (Retrieval-Augmented Generation) pipeline'ini amalda tushunish.

---

# 1. Embedding

**Embedding** — matnni AI tushunadigan sonli vektorga (vector) aylantirish jarayoni.

Misol:

```text
"I love football"

↓

[-0.12, 0.45, ..., 0.81]
```

Embeddingning o'zi javob bermaydi. U faqat matnlarning ma'nosini sonlar orqali ifodalaydi.

---

# 2. Sentence Transformer

Pipeline:

```text
Sentence
    ↓
Tokenizer
    ↓
Transformer (BERT)
    ↓
Token Embeddings
    ↓
Mean Pooling
    ↓
Normalize
    ↓
Sentence Embedding
```

Natijada bitta gap uchun bitta embedding hosil bo'ladi.

---

# 3. Cosine Similarity

Ikki embedding qanchalik o'xshashligini hisoblaydi.

* 1.0 → Juda o'xshash
* 0.7–0.9 → O'xshash
* 0–0.3 → Deyarli aloqasi yo'q

Embeddinglar odatda cosine similarity orqali taqqoslanadi.

---

# 4. Semantic Search

Oddiy qidiruv so'zlarni qidiradi.

Semantic Search esa **ma'noni** qidiradi.

Pipeline:

```text
Question
      ↓
Embedding
      ↓
Cosine Similarity
      ↓
Top-K Documents
```

---

# 5. Document Loading

LangChain faylni `Document` obyektiga yuklaydi.

`Document` tarkibi:

* `page_content` → Matn
* `metadata` → Qo'shimcha ma'lumot (source, page va h.k.)

---

# 6. Chunking

Katta hujjatni kichik bo'laklarga ajratish.

Misol:

```text
PDF
    ↓
Chunk 1
Chunk 2
Chunk 3
...
```

Sabablari:

* Token limit
* Yaxshiroq semantic search
* LLMga faqat kerakli ma'lumotni yuborish

---

# 7. Chunk Overlap

Chunklar orasida umumiy qism qoldiriladi.

Misol:

```text
Chunk 1
0 — 1000

Chunk 2
800 — 1800
```

Bu context yo'qolib ketmasligi uchun ishlatiladi.

---

# 8. Vector Database

Har bir chunk embedding qilinadi va Vector DB'ga saqlanadi.

Masalan:

* ChromaDB
* FAISS

Vector DB embeddinglarni tez qidirish uchun ishlatiladi.

---

# 9. Retrieval

Foydalanuvchi savol beradi.

Pipeline:

```text
Question
      ↓
Embedding
      ↓
Vector DB
      ↓
Similarity Search
      ↓
Top-K Chunks
```

Bu bosqich **Retrieval** deyiladi.

---

# 10. RAG

RAG = **Retrieval + Generation**

To'liq pipeline:

```text
Document
      ↓
Text Loader
      ↓
Chunking
      ↓
Embedding
      ↓
Vector DB
      ↓

User Question
      ↓
Question Embedding
      ↓
Similarity Search
      ↓
Top-K Chunks
      ↓
LLM (Gemini / GPT)
      ↓
Final Answer
```

Muhim:

* Retrieval ma'lumotni topadi.
* LLM topilgan ma'lumot asosida javob yaratadi.

RAGning vazifasi — LLMga butun hujjatni emas, faqat kerakli qismlarni yuborish.

---

# Bugun o'rganilgan tushunchalar

* Embedding
* Sentence Transformer
* Cosine Similarity
* Semantic Search
* Document
* Chunking
* Chunk Overlap
* Vector Database
* Retrieval
* RAG Pipeline
