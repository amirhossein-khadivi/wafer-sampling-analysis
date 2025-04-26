import numpy as np
import matplotlib.pyplot as plt

def sample_and_plot(mask, center, sample_size, wafer_size,cmap_name="Blues"):
    """
    انجام نمونه‌گیری تصادفی از ماسک و رسم آن روی ویفر
    
    پارامترها:
    - mask: آرایه ماسک ویفر (0 و 1)
    - center: مختصات مرکز (tuple)
    - sample_size: تعداد نقاط نمونه‌گیری‌شده
    - cmap_name: نام colormap برای رسم
    
    خروجی:
    - sample_random: آرایه نقاط انتخاب‌شده (n×2)
    """
    wafer_size = mask.shape[0]
    valid_coords = np.array(np.where(mask == 1)).T
    sample_indices = np.random.choice(len(valid_coords), sample_size, replace=False)
    sample_random = valid_coords[sample_indices]

    # رسم
    fig, ax = plt.subplots(figsize=(8, 8))
    cmap = plt.cm.get_cmap(cmap_name)
    ax.pcolormesh(np.arange(wafer_size + 1), np.arange(wafer_size + 1), mask, cmap=cmap,
                  edgecolors='gray', linewidth=0.5, shading='auto')

    ax.plot(center[1] + 0.5, center[0] + 0.5, 'rx', markersize=10, label='Center')

    sample_x = sample_random[:, 1]
    sample_y = sample_random[:, 0]
    ax.scatter(sample_x + 0.5, sample_y + 0.5, color='yellow', label='Random Samples', s=20)

    ax.set_aspect('equal')
    ax.set_xlim(0, wafer_size)
    ax.set_ylim(0, wafer_size)
    ax.invert_yaxis()
    ax.set_xticks(np.arange(wafer_size + 1))
    ax.set_yticks(np.arange(wafer_size + 1))
    ax.grid(which='both', color='lightgray', linewidth=0.5)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_title(f"Circular Wafer {wafer_size}×{wafer_size} with Random Sampling", fontsize=14)
    ax.legend()
    plt.tight_layout()
    plt.show()

    return sample_random, valid_coords
