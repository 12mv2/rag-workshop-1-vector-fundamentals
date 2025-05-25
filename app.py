import argparse
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from db.vector_db import VectorDB


def normalize_feature(value, min_val, max_val):
    """Normalize a feature to 0-1 range"""
    return (value - min_val) / (max_val - min_val)


def embed(runner, normalize=False, weights=None):
    cadence = runner["cadence"]
    heel_ratio = runner["heel_strike"]  # 0 = toe, 1 = full heel
    vert = runner["vertical_oscillation"]

    # Convert heel strike to angle
    heel_angle = heel_ratio * 90  # degrees

    if normalize:
        cadence = normalize_feature(cadence, 50, 250)
        heel_angle = normalize_feature(heel_angle, 0, 90)
        vert = normalize_feature(vert, 6, 20)

    vec = [cadence, heel_angle, vert]

    if weights:
        vec = [v * w for v, w in zip(vec, weights)]

    return vec


def plot_vectors(vectors, names, title, plot_type):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    xs = [vec[0] for vec in vectors]
    ys = [vec[1] for vec in vectors]
    zs = [vec[2] for vec in vectors]

    ax.scatter(xs, ys, zs, c='blue', marker='o', s=100)

    for i, name in enumerate(names):
        ax.text(xs[i], ys[i], zs[i], name, size=9, fontweight='bold')

    ax.set_xlabel('Cadence')
    ax.set_ylabel('Heel Strike Angle (degrees)')
    ax.set_zlabel('Vertical Oscillation (cm)')
    ax.set_title(title, fontsize=14, fontweight='bold')

    if plot_type == "raw":
        ax.set_xlim(0, 300)
        ax.set_ylim(0, 90)
        ax.set_zlim(0, 25)
    else:
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_zlim(0, 1)

    plt.tight_layout()
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="Vector Database Visualization")
    parser.add_argument("--plot", choices=["raw", "normalized", "weighted"], 
                       help="Type of plot to generate", required=True)
    parser.add_argument("--weights", nargs=3, type=float, 
                       help="Three weights for the vector dimensions (required for weighted)")
    args = parser.parse_args()

    # Validate weighted plot has weights
    if args.plot == "weighted" and not args.weights:
        print("Error: --weights required when using --plot weighted")
        print("Example: python app.py --plot weighted --weights 2.0 1.0 0.5")
        return

    db = VectorDB()
    data = db.get_all()
    names = [r["name"] for r in data]

    normalize = args.plot in ["normalized", "weighted"]
    weights = args.weights if args.plot == "weighted" else None
    vectors = [embed(r, normalize=normalize, weights=weights) for r in data]

    # Create title
    if args.plot == "raw":
        title = "Raw Vectors"
    elif args.plot == "normalized":
        title = "Normalized Vectors (0-1 scale)"
    elif args.plot == "weighted":
        title = f"Weighted Vectors (Weights: {args.weights})"

    # Print vectors to console
    print(f"\n=== {title.upper()} ===")
    for name, vec in zip(names, vectors):
        formatted_vec = [f"{v:.3f}" for v in vec]
        print(f"{name}: {formatted_vec}")

    # Show plot
    plot_vectors(vectors, names, title, args.plot)
    print(f"\nPlot displayed: {title}")


if __name__ == "__main__":
    main()