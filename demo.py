#!/usr/bin/env python3
import json
import math
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def normalize_feature(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)

def normalize_vector(vec):
    mag = math.sqrt(sum(x**2 for x in vec))
    return [x/mag for x in vec] if mag > 0 else vec

# Load data (use path relative to this script)
script_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(script_dir, 'data/runners.json')) as f:
    data = json.load(f)

# Create vectors
vectors = {}
for entity in data:
    cad = normalize_feature(entity['cadence'], 50, 260)
    heel = entity['heel_strike']
    osc = normalize_feature(entity['vertical_oscillation'], 4, 35)
    vectors[entity['name']] = normalize_vector([cad, heel, osc])

# Plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

for name, vec in vectors.items():
    ax.scatter(*vec, s=150, edgecolors='black', linewidth=1.5)
    ax.text(vec[0], vec[1], vec[2], f'  {name}', fontsize=10)

ax.set_xlabel('Cadence (normalized)')
ax.set_ylabel('Heel Strike')
ax.set_zlabel('Vertical Oscillation (normalized)')
ax.set_title('Vector Embeddings: Runner Biomechanics')
plt.show()
