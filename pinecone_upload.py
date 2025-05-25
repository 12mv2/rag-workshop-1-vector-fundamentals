import os
import json
import math
from pinecone import Pinecone
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- Configuration (replace with your actual values) ---
API_KEY = os.getenv("PINECONE_API_KEY", "your-pinecone-api-key-here")
INDEX_NAME = os.getenv("PINECONE_INDEX", "runners-index")

def normalize_feature(value, min_val, max_val):
    """Normalize a feature to 0-1 range"""
    return (value - min_val) / (max_val - min_val)

def normalize_vector(vector):
    """Normalize a vector to unit length (L2 normalization)"""
    magnitude = math.sqrt(sum(x**2 for x in vector))
    return [x / magnitude for x in vector] if magnitude > 0 else vector

def embed_runner(runner):
    """Convert runner data to normalized vector"""
    cadence = normalize_feature(runner["cadence"], 50, 250)
    heel_angle = normalize_feature(runner["heel_strike"] * 90, 0, 90)
    vert_osc = normalize_feature(runner["vertical_oscillation"], 6, 20)
    
    # Create vector and normalize to unit length
    vec = [cadence, heel_angle, vert_osc]
    return normalize_vector(vec)

# Initialize Pinecone (new v3+ syntax)
print(f"API Key: {API_KEY[:10]}...{API_KEY[-4:] if len(API_KEY) > 14 else 'MISSING'}")
print(f"Index Name: {INDEX_NAME}")

if API_KEY == "your-pinecone-api-key-here":
    print("❌ ERROR: You need to set your actual Pinecone API key!")
    print("Create a .env file with:")
    print("PINECONE_API_KEY=your-actual-key-here")
    print("PINECONE_INDEX=runners-index")
    exit(1)

pc = Pinecone(api_key=API_KEY)
index = pc.Index(INDEX_NAME)

# --- Load Data ---
with open("data/runners.json", "r") as f:
    data = json.load(f)

vectors_to_upsert = []

print("Processing runners:")
for runner in data:
    # Create normalized vector
    vector = embed_runner(runner)
    vectors_to_upsert.append((runner["name"], vector))
    print(f"  {runner['name']}: {[f'{v:.3f}' for v in vector]}")

# --- Upsert to Pinecone ---
index.upsert(vectors=vectors_to_upsert)
print(f"\n✅ Upserted {len(vectors_to_upsert)} vectors to Pinecone index '{INDEX_NAME}'.")