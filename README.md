# Workshop 1: Vector Fundamentals

**Learn:** How computers measure similarity using distance in vector space

## Quick Start
```bash
git clone https://github.com/12mv2/rag-workshop-1-vector-fundamentals.git
cd rag-workshop-1-vector-fundamentals
python demo.py
```

## What You'll Do

| **Phase** | **Action** | **Outcome** | **Time** |
|-----------|------------|-------------|----------|
| **Setup** | Run commands above | 3D plot opens automatically | 2 min |
| **See It** | Watch: Marathoners cluster (blue), Bolt nearby, Kangaroo isolated | Patterns emerged from math alone | 3 min |
| **Concept** | Similar numbers → Similar vectors → Automatic clustering | No manual rules needed | 5 min |
| **Your Turn** | Edit `data/runners.json`: Change "Cheetah" cadence from 250 to 180 | Watch it move closer to marathoners | 10 min |
| **Learned** | Similarity = distance in space (foundation of RAG) | ✅ You get vectors | 2 min |

## The Core Insight

Every runner has 3 numbers (cadence, heel strike, oscillation). Plot them as X, Y, Z coordinates. **Similar runners automatically cluster together** - no programming required, just math.

This is why RAG works: similar documents become similar vectors, and computers find them instantly.

<details>
<summary><strong>🔧 Advanced: Setup Pinecone for Workshop 3</strong></summary>

Get ahead - configure your production vector database now:

1. **Sign up:** [pinecone.io](https://pinecone.io) (free tier)
2. **Create index:**
   - Name: `runners-index`
   - Dimensions: `3`
   - Metric: `cosine`
3. **Save API key:**
   ```bash
   mkdir -p ~/.config/rag-workshop
   echo "YOUR_KEY_HERE" > ~/.config/rag-workshop/pinecone.key
   ```

This lets Workshop 3 start instantly (no setup time).

</details>

<details>
<summary><strong>📚 Understanding the Data</strong></summary>

**5 entities, 3 metrics each:**

| Name | Cadence | Heel Strike | Vert. Osc |
|------|---------|-------------|-----------|
| Eliud Kipchoge | 180 | 0.2 | 6.5 |
| Shalane Flanagan | 185 | 0.3 | 7.0 |
| Cheetah | 250 | 0.1 | 8.0 |
| Baron Harkonnen | 60 | 0.9 | 20.0 |
| Cow | 50 | 0.6 | 15.0 |

**Why these cluster:**
- **Elite runners** (Kipchoge, Flanagan): Similar cadence ~182, low heel strike, minimal bounce
- **Cheetah**: High cadence but efficient mechanics
- **Non-runners** (Baron, Cow): Extreme outliers

</details>

<details>
<summary><strong>💡 Want to modify and save your changes?</strong></summary>

Fork it first:
1. Click "Fork" on GitHub
2. Clone YOUR fork: `git clone https://github.com/YOUR_USERNAME/rag-workshop-1-vector-fundamentals.git`
3. Experiment freely
4. (Optional) Submit PR if you build something cool

</details>

---

**Next:** [Workshop 2 - Retrieval Basics](https://github.com/12mv2/rag-workshop-2-retrieval-basics) - Stop LLM hallucinations with grounded data

---

**Questions?** [GitHub Discussions](https://github.com/12mv2/rag-workshop-1-vector-fundamentals/discussions)
