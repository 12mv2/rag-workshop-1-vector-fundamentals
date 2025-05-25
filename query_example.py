import os
import math
from pinecone import Pinecone

# --- Configuration ---
API_KEY = os.getenv("PINECONE_API_KEY", "your-pinecone-api-key-here")
INDEX_NAME = os.getenv("PINECONE_INDEX", "runners-index")

def normalize_feature(value, min_val, max_val):
    """Normalize a feature to 0-1 range"""
    return (value - min_val) / (max_val - min_val)

def normalize_vector(vector):
    """Normalize a vector to unit length (L2 normalization)"""
    magnitude = math.sqrt(sum(x**2 for x in vector))
    return [x / magnitude for x in vector] if magnitude > 0 else vector

def create_query_vector(cadence, heel_strike_ratio, vertical_osc):
    """Create a query vector from runner characteristics"""
    cadence_norm = normalize_feature(cadence, 50, 250)
    heel_angle_norm = normalize_feature(heel_strike_ratio * 90, 0, 90)
    vert_osc_norm = normalize_feature(vertical_osc, 6, 20)
    
    vec = [cadence_norm, heel_angle_norm, vert_osc_norm]
    return normalize_vector(vec)

# Initialize Pinecone (new v3+ syntax)
pc = Pinecone(api_key=API_KEY)
index = pc.Index(INDEX_NAME)

# --- Create query for a Usain Bolt-like sprinter ---
print("Searching for runners similar to:")
print("  Cadence: 260 steps/min")
print("  Heel Strike: 0.2 (mostly toe-first)")
print("  Vertical Oscillation: 4.8 cm")

query_vector = create_query_vector(
    cadence=260,
    heel_strike_ratio=0.2,
    vertical_osc=4.8
)

print(f"  Query vector: {[f'{v:.3f}' for v in query_vector]}")

# --- Query the index ---
results = index.query(
    vector=query_vector,
    top_k=5,
    include_metadata=False
)

# --- Display results ---
print(f"\n🔍 Top {len(results['matches'])} most similar runners:")
for i, match in enumerate(results['matches'], 1):
    print(f"  {i}. {match['id']}: similarity score = {match['score']:.4f}")

print(f"\n💡 Higher scores mean more similar running styles!")