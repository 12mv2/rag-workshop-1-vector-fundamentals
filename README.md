# 🧠 30 Minute Vector Database

A beginner-friendly command-line demo that builds a vector database from scratch and compares runners and animals based on biomechanics features.

This project is designed to help you understand how vector embeddings work in a fun, fast, and visualizable way.

---

## 🏃‍♂️ Project Overview

Each entity (runner or creature) is represented by a vector of 3 features:

- **Cadence**: Steps per minute
- **Heel Strike**: A value from 0 (toe-first) to 1 (heel-first) 
- **Vertical Oscillation**: How much the torso moves up and down, in cm

We embed these features into 3D space and visualize how different runners cluster together.

---

## 🚀 Workshop Commands (In Order)

### 1. Setup
```bash
# Clone this repo
git clone https://github.com/12mv2/30min-vector-db.git
cd 30min-vector-db

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Explore the Data
```bash
# Look at our runner data
cat data/runners.json

# Or use Python to explore
python -c "import json; print(json.dumps(json.load(open('data/runners.json')), indent=2))"
```

### 3. Vector Visualization (Phase 1: Understanding Vectors)
```bash
# View raw vectors - see the actual feature values in 3D
python app.py --plot raw

# View normalized vectors - everything scaled to 0-1 range
python app.py --plot normalized
``` 

### 4. Feature Engineering (Phase 2: Weighting Features) 
```bash
# Apply custom weights to features
python app.py --plot weighted --weights 1.0 2.0 0.5

# Weight cadence heavily, de-emphasize vertical oscillation
python app.py --plot weighted --weights 3.0 1.0 0.1

# Make heel strike the dominant feature
python app.py --plot weighted --weights 0.5 5.0 0.5

# Equal weights (same as normalized)
python app.py --plot weighted --weights 1.0 1.0 1.0
```

### 5. Production Vector Database (Phase 3: Scaling Up)
```bash
# Set up environment variables for Pinecone
echo "PINECONE_API_KEY=your-key-here" > .env
echo "PINECONE_INDEX=runners-index" >> .env

# Upload vectors to Pinecone cloud database
python pinecone_upload.py

# Query the Pinecone database to find similar runners
python query_example.py
```

---

## 📁 Folder Structure

```
30min-vector-db/
├── data/
│   └── runners.json              # Input dataset
├── db/
│   └── vector_db.py              # Simple in-memory "database"
├── search/
│   └── normalize.py              # Feature scaling utilities
├── app.py                        # Main visualization tool
├── pinecone_upload.py            # Upload vectors to Pinecone
├── query_example.py             # Query Pinecone database
├── requirements.txt              # Python dependencies
├── .env                          # Environment variables (create this)
├── .gitignore
└── README.md
```

---

## 🎯 Workshop Learning Path

### Phase 1: Understanding Vectors (10 minutes)
**Goal**: See data as points in space
1. `python app.py --plot raw` - visualize actual feature values
2. `python app.py --plot normalized` - understand why normalization matters
3. **Key insight**: Baron Harkonnen vs elite runners are in completely different regions!

### Phase 2: Feature Engineering (10 minutes)  
**Goal**: Learn how weighting changes vector relationships
1. `python app.py --plot weighted --weights 3.0 1.0 0.1` - make cadence dominant
2. `python app.py --plot weighted --weights 0.5 5.0 0.5` - make heel strike dominant
3. **Key insight**: Different weights = different clustering patterns

### Phase 3: Production Scaling (10 minutes)
**Goal**: Move from toy example to production vector database
1. Set up Pinecone account and API keys
2. `python pinecone_upload.py` - upload vectors to cloud
3. `python query_example.py` - perform similarity search at scale
4. **Key insight**: Now you can search millions of vectors instantly!

---

## 🤖 Tech Stack

- **Core Demo**: Python 3.11 + matplotlib (visualization only)
- **Production**: Pinecone (cloud vector database)
- **Dependencies**: minimal (just what's needed)

---

## 🧪 Example Output

```bash
$ python app.py --plot normalized

=== NORMALIZED VECTORS (0-1 SCALE) ===
Eliud Kipchoge: ['0.650', '0.200', '0.025']
Baron Harkonnen: ['0.050', '0.900', '0.700'] 
Cheetah: ['1.000', '0.100', '0.100']
Shalane Flanagan: ['0.675', '0.300', '0.050']
Cow: ['0.000', '0.600', '0.450']

Plot displayed: Normalized Vectors (0-1 scale)
```

---

## 🧠 Key Learning Goals

- **Embeddings**: How to convert real-world features into vectors
- **Normalization**: Why feature scaling matters for fair comparison
- **Feature Weighting**: How to emphasize important characteristics  
- **Dimensionality**: Visualizing high-dimensional data
- **Production**: Scaling from toy examples to real vector databases

---

## 🔧 Troubleshooting

**Import errors?**
```bash
pip install -r requirements.txt
```

**Missing --weights argument?**
```bash
# This will error:
python app.py --plot weighted

# Do this instead:
python app.py --plot weighted --weights 1.0 1.0 1.0
```

**No plots showing?**
```bash
# On WSL/Linux without display
export DISPLAY=:0
# Or check your matplotlib backend
python -c "import matplotlib; print(matplotlib.get_backend())"
```

**Pinecone errors?**
- Check your API key in `.env`
- Verify your Pinecone index exists
- Ensure you're using the correct environment name

---

## 🗣️ License

MIT License — use this project for demos, learning, or expanding into real vector DB integrations later!