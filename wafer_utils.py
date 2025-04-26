import numpy as np
import matplotlib.pyplot as plt

def create_wafer_mask(wafer_size=33):
    """
    ساخت ماسک دایره‌ای ویفر
    خروجی: ماسک (numpy array) و مرکز (tuple)
    """
    radius = wafer_size // 2
    center = (radius, radius)
    
    x, y = np.ogrid[:wafer_size, :wafer_size]
    mask = ((x - center[0])**2 + (y - center[1])**2 <= radius**2).astype(float)
    
    return mask, center

def plot_wafer_mask(mask, center, cmap_name="Blues"):
    """
    رسم ویفر از روی ماسک و مرکز
    """
    wafer_size = mask.shape[0]
    x_edges = np.arange(wafer_size + 1)
    y_edges = np.arange(wafer_size + 1)

    fig, ax = plt.subplots(figsize=(8, 8))
    cmap = plt.cm.get_cmap(cmap_name)
    ax.pcolormesh(x_edges, y_edges, mask, cmap=cmap, edgecolors='gray', linewidth=0.5, shading='auto')

    ax.plot(center[1] + 0.5, center[0] + 0.5, 'rx', markersize=10, label='Center')

    ax.set_aspect('equal')
    ax.set_xlim(0, wafer_size)
    ax.set_ylim(0, wafer_size)
    ax.invert_yaxis()
    ax.set_xticks(np.arange(wafer_size + 1))
    ax.set_yticks(np.arange(wafer_size + 1))
    ax.grid(which='both', color='lightgray', linewidth=0.5)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_title(f"Circular Wafer {wafer_size}×{wafer_size}", fontsize=14)
    ax.legend()
    plt.tight_layout()
    plt.show()