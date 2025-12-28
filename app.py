#!/usr/bin/env python3
"""
Vector Embeddings Visualization
Part 1 of RAG Workshop Series

Simple command:  python app.py
"""

import argparse
import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import os

# Add search module to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'search'))

from normalize import normalize_feature, normalize_vector


def load_data():
    """Load runner biomechanics data"""
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'runners. json')
    with open(data_path, 'r') as f:
        return json.load(f)


def create_vectors(data, mode='normalized', weights=None):
    """Convert biomechanics data to vectors"""
    vectors = {}
    
    for entity in data:
        name = entity['name']
        
        # Normalize to 0-1 scale
        cad_norm = normalize_feature(entity['cadence'], 50, 260)
        heel_norm = entity['heel_strike']
        osc_norm = normalize_feature(entity['vertical_oscillation'], 4, 35)
        
        if mode == 'raw':
            vec = [entity['cadence'], entity['heel_strike'], entity['vertical_oscillation']]
        elif mode == 'weighted' and weights:
            vec = [cad_norm * weights[0], heel_norm * weights[1], osc_norm * weights[2]]
            vec = normalize_vector(vec)
        else:  # normalized (default)
            vec = normalize_vector([cad_norm, heel_norm, osc_norm])
        
        vectors[name] = vec
    
    return vectors


def visualize(vectors, data, title="Vector Embeddings:  Runner Biomechanics"):
    """Create 3D visualization"""
    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create type mapping
    type_map = {e['name']: e['type'] for e in data}
    
    # Separate by type
    humans = [(name, vec) for name, vec in vectors. items() if type_map.get(name) == 'human']
    animals = [(name, vec) for name, vec in vectors.items() if type_map.get(name) == 'animal']
    others = [(name, vec) for name, vec in vectors.items() if type_map.get(name) == 'other']
    
    # Plot each group
    legend_added = {'human': False, 'animal': False, 'other': False}
    
    for name, vec in humans: 
        label = '🏃 Humans' if not legend_added['human'] else ''
        ax.scatter(*vec, c='#2E86DE', marker='o', s=150, label=label, edgecolors='black', linewidth=1. 5)
        ax.text(vec[0], vec[1], vec[2], f'  {name}', fontsize=9, fontweight='bold')
        legend_added['human'] = True
    
    for name, vec in animals:
        label = '🐾 Animals' if not legend_added['animal'] else ''
        ax.scatter(*vec, c='#10AC84', marker='^', s=150, label=label, edgecolors='black', linewidth=1.5)
        ax.text(vec[0], vec[1], vec[2], f'  {name}', fontsize=9, fontweight='bold')
        legend_added['animal'] = True
    
    for name, vec in others: 
        label = '🎭 Other' if not legend_added['other'] else ''
        ax.scatter(*vec, c='#EE5A6F', marker='s', s=150, label=label, edgecolors='black', linewidth=1.5)
        ax.text(vec[0], vec[1], vec[2], f'  {name}', fontsize=9, fontweight='bold')
        legend_added['other'] = True
    
    # Labels and styling
    ax.set_xlabel('Cadence (normalized)', fontweight='bold', fontsize=11)
    ax.set_ylabel('Heel Strike', fontweight='bold', fontsize=11)
    ax.set_zlabel('Vertical Oscillation (normalized)', fontweight='bold', fontsize=11)
    ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
    ax.legend(fontsize=11, loc='upper left')
    
    # Set viewing angle
    ax.view_init(elev=20, azim=45)
    
    plt.tight_layout()
    plt.show()


def print_vectors(vectors, mode):
    """Print vector values to console"""
    print(f"\n{'='*70}")
    print(f"VECTOR EMBEDDINGS ({mode.upper()} MODE)")
    print(f"{'='*70}\n")
    
    for name, vec in vectors.items():
        print(f"{name: 20s}:  [{vec[0]: 7.3f}, {vec[1]:7.3f}, {vec[2]:7.3f}]")
    
    print(f"\n{'='*70}")
    print("💡 KEY INSIGHT: Similar vectors = Similar biomechanics")
    print("   Look for clusters in the 3D visualization!")
    print(f"{'='*70}\n")


def main():
    parser = argparse.ArgumentParser(
        description='Visualize vector embeddings of runner biomechanics',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python app.py                          # Default:  normalized vectors (RECOMMENDED)
  python app.py --plot raw               # View raw (unnormalized) data
  python app.py --plot weighted --weights 3.0 1.0 0.1  # Custom weighting
        """
    )
    
    parser.add_argument('--plot', choices=['raw', 'normalized', 'weighted'], 
                        default='normalized',
                        help='Visualization mode (default: normalized)')
    parser.add_argument('--weights', nargs=3, type=float, metavar=('CADENCE', 'HEEL', 'OSC'),
                        help='Custom feature weights for weighted mode')
    
    args = parser.parse_args()
    
    # Validate weights for weighted mode
    if args.plot == 'weighted' and not args.weights:
        print("❌ Error: --weights required for weighted mode")
        print("\nExample:")
        print("  python app. py --plot weighted --weights 1.0 1.0 1.0")
        print("\nTIP: Use default mode for the workshop:")
        print("  python app. py")
        return
    
    # Load data
    print("\n🔄 Loading runner biomechanics data...")
    data = load_data()
    print(f"✅ Loaded {len(data)} entities")
    
    # Create vectors
    print(f"🔄 Creating {args.plot} vectors...")
    vectors = create_vectors(data, mode=args.plot, weights=args.weights)
    
    # Print vectors
    print_vectors(vectors, args.plot)
    
    # Visualize
    title_map = {
        'raw': 'Raw Vectors (Unnormalized)',
        'normalized': 'Normalized Vectors:  Runner Biomechanics Clustering',
        'weighted': f'Weighted Vectors (weights: {args.weights})'
    }
    
    print("🎨 Opening 3D visualization...")
    print("   (Close the plot window to exit)\n")
    
    visualize(vectors, data, title=title_map[args.plot])
    
    print("\n✅ Workshop Part 1 Complete!")
    print(f"{'='*70}")
    print("📚 What you learned:")
    print("   ✅ Similar data creates similar vectors")
    print("   ✅ Normalization makes features comparable")
    print("   ✅ Vectors enable automatic clustering")
    print(f"\n➡️  Next: Part 2 - Learn how to use vectors with LLMs")
    print("   https://github.com/12mv2/workshop-rag-2-retrieval")
    print(f"{'='*70}\n")


if __name__ == '__main__':
    main()
