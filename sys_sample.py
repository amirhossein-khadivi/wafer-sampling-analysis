import numpy as np
import matplotlib.pyplot as plt

def systematic_sampling(mask, sample_size, valid_coords):
    """
    نمونه‌گیری سیستماتیک از نقاط معتبر ماسک
    
    ورودی:
    - mask: آرایه ماسک (0 و 1)
    - sample_size: تعداد نمونه
    
    خروجی:
    - systematic_samples: آرایه نقاط انتخاب‌شده (n×2)
    """
    valid_coords = np.array(np.where(mask == 1)).T
    total_valid = len(valid_coords)
    interval = total_valid // sample_size
    start_idx = np.random.randint(0, interval)
    systematic_samples = valid_coords[start_idx::interval][:sample_size]
    return systematic_samples


def plot_systematic_samples(mask, center, samples, cmap_name="Blues"):
    """
    رسم ویفر و نقاط نمونه‌گیری سیستماتیک
    
    پارامترها:
    - mask: آرایه ماسک
    - center: مختصات مرکز
    - samples: آرایه نقاط نمونه‌گیری‌شده
    """
    wafer_size = mask.shape[0]
    fig, ax = plt.subplots(figsize=(8, 8))
    cmap = plt.cm.get_cmap(cmap_name)
    ax.pcolormesh(np.arange(wafer_size + 1), np.arange(wafer_size + 1), mask,
                  cmap=cmap, edgecolors='gray', linewidth=0.5, shading='auto')

    # مرکز ویفر
    ax.plot(center[1] + 0.5, center[0] + 0.5, 'rx', markersize=10, label='Center')

    # نمونه‌ها
    sample_x = samples[:, 1]
    sample_y = samples[:, 0]
    ax.scatter(sample_x + 0.5, sample_y + 0.5, color='yellow', label='Systematic Samples', s=20)

    ax.set_aspect('equal')
    ax.set_xlim(0, wafer_size)
    ax.set_ylim(0, wafer_size)
    ax.invert_yaxis()
    ax.set_xticks(np.arange(wafer_size + 1))
    ax.set_yticks(np.arange(wafer_size + 1))
    ax.grid(which='both', color='lightgray', linewidth=0.5)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_title(f"Circular Wafer {wafer_size}×{wafer_size} with Systematic Sampling", fontsize=14)
    ax.legend()
    plt.tight_layout()
    plt.show()
