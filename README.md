# 🎯 RAG Workshop Series - Part 1: Vector Fundamentals

> **📚 This is Part 1 of a 3-part workshop series on Retrieval-Augmented Generation**
> - **Part 1** (You are here): Vector embeddings & visualization
> - [Part 2: RAG Basics](https://github.com/12mv2/workshop-rag-2-retrieval) - Stop LLM hallucinations with retrieval
> - [Part 3: Production Pipeline](https://github.com/12mv2/workshop-rag-3-production) - Semantic search at scale

---

## 🧠 What You'll Learn

**How do computers understand "similarity"?**

See how runner biomechanics becomes vectors that automatically cluster similar gaits together—no manual rules needed. 

**💡 Core Insight:** Similar data → Similar vectors → Automatic clustering

---

## 🚀 Quick Start

```bash
# 1. Clone and setup
git clone https://github.com/12mv2/workshop-rag-1-vectors.git
cd workshop-rag-1-vectors
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 2. Run the visualization
python app.py
```

**That's it!** A 3D plot appears showing how runners and animals cluster in vector space.

---

## 📊 What You'll See

### The Visualization

A 3D scatter plot with 9 entities as points in space: 

**🏃 Elite Distance Runners** (tight blue cluster):
- Eliud Kipchoge (marathon legend)
- Mo Farah (distance specialist)
- Kenenisa Bekele (10K/marathon)

**⚡ Sprinter** (nearby, distinct):
- Usain Bolt (explosive power)

**🐾 Animals** (scattered):
- Cheetah (speed demon)
- Horse (heel-heavy gait)
- Kangaroo (extreme hopper - way off on its own!)

**🎭 For Fun**:
- Baron Harkonnen (definitely not a runner 😅)

---

## 💡 The "Aha!" Moment

**Look at the clusters:**

✅ **Elite marathoners group together** - Similar gaits (cadence ~185, low heel strike, minimal bounce)  
✅ **Usain Bolt is nearby but separate** - Sprinters use different biomechanics  
✅ **Kangaroo is in its own universe** - Hopping is fundamentally different (extreme vertical oscillation)  
✅ **You didn't program these categories** - Similarity emerged from the math! 

**This is the foundation of RAG. ** Instead of manually coding rules, vectors capture relationships automatically.

---

## 🧠 How It Works

### The Data

Each entity has 3 biomechanics features: 

```python
Eliud Kipchoge:
  Cadence: 185 steps/min
  Heel Strike: 0.2 (0=toe, 1=heel)
  Vertical Oscillation: 6.2 cm

Kangaroo:
  Cadence: 70 hops/min
  Heel Strike: 0.0 (pure toe)
  Vertical Oscillation: 35.0 cm
```

### The Process

1. **Normalize to 0-1 scale** - Prevents big numbers from dominating
2. **Create 3D vectors** - [cadence, heel_strike, oscillation]
3. **Plot in space** - Similar gaits = nearby points

**Why normalization matters:**
- ❌ Without:  Cadence (185) drowns out heel strike (0.2)
- ✅ With: All features contribute equally

---

## 🎯 Why This Matters for RAG

RAG systems need to find relevant information quickly: 

```
User asks: "How do elite marathoners run?"
        ↓
Convert question to vector
        ↓
Find nearest neighbors (Kipchoge, Farah, Bekele)
        ↓
Feed context to LLM
        ↓
Get accurate, grounded answer
```

**You just learned step 1:** How data becomes searchable vectors! 

---

## 🔧 Optional: Pinecone Setup (For Part 3)

Part 3 uses Pinecone (cloud vector database). Set it up now to save time later: 

<details>
<summary><b>Click to expand Pinecone setup (5 minutes)</b></summary>

### Quick Setup

1. **Sign up:** Visit [pinecone.io](https://pinecone.io) → Create free account

2. **Create index:**
   - Click "Create Index"
   - Name: `runners-index`
   - Dimensions: `3`
   - Metric: `cosine`
   - Click "Create Index"

3. **Get API key:**
   - Click "API Keys" in sidebar
   - Copy your API key

4. **Add to `.env` file:**
   ```bash
   echo "PINECONE_API_KEY=your-key-here" >> .env
   echo "PINECONE_INDEX=runners-index" >> .env
   ```

✅ **Done!** You won't use it in Parts 1-2, but it'll be ready for Part 3.

**Don't want to set up now?** No problem - Part 1 works completely without it. 

</details>

---

## ➡️ What's Next? 

### Continue the Series

**[Part 2: RAG Basics →](https://github.com/12mv2/workshop-rag-2-retrieval)**  
Now that you understand vectors, learn how to use retrieval to stop LLM hallucinations.  Build your first RAG system. 

**[Part 3: Production Pipeline →](https://github.com/12mv2/workshop-rag-3-production)**  
Combine vector search + LLMs into a production-ready RAG system using Pinecone.

---

## 🔧 Troubleshooting

**No plot showing?**
```bash
# On WSL/Linux without display: 
export DISPLAY=:0
```

**Import errors?**
```bash
pip install -r requirements.txt
```

**Want to see the raw data?**
```bash
cat data/runners.json
```

---

## 🔬 Advanced (Optional)

<details>
<summary><b>Click to expand advanced options</b></summary>

### View Raw (Unnormalized) Vectors

```bash
python app.py --plot raw
```

See why normalization is necessary - cadence dominates everything!

### Custom Feature Weighting

```bash
# Make cadence 3x more important
python app.py --plot weighted --weights 3.0 1.0 0.1

# Make heel strike dominant
python app.py --plot weighted --weights 0.5 5.0 0.5
```

Different weights = different definitions of "similarity"!

### Add Your Own Data

Edit `data/runners.json`:

```json
{
  "name": "Your Name",
  "type": "human",
  "cadence": 175,
  "heel_strike":  0.3,
  "vertical_oscillation": 7.5,
  "description": "Your running style"
}
```

Then run `python app.py` to see where you cluster!

### Explore the Code

- `app.py` - Main visualization logic
- `data/runners.json` - The dataset
- `search/normalize.py` - Normalization utilities
- `db/vector_db.py` - Simple in-memory vector database

</details>

---

## 📜 License

MIT License - freely use, modify, and distribute. 

---

## 🌟 Ready for Part 2? 

⭐ **Star this repo** then continue to **[Part 2: RAG Basics →](https://github.com/12mv2/workshop-rag-2-retrieval)** to build your first RAG system!

Questions? Open an issue - contributions welcome!  🚀
