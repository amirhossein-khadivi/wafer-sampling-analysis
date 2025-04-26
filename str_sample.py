import numpy as np
import matplotlib.pyplot as plt

def stratified_sampling(mask, center, sample_size, valid_coords, n_strata=3):
    """
    نمونه‌گیری طبقه‌ای از نقاط معتبر ویفر

    ورودی:
    - mask: ماتریس ماسک (0 و 1)
    - center: مرکز ویفر (tuple)
    - sample_size: تعداد کل نمونه‌ها
    - n_strata: تعداد طبقات شعاعی

    خروجی:
    - sample_stratified: آرایه نمونه‌های انتخاب‌شده (n×2)
    - strata_indices: لیبل هر نقطه نسبت به طبقه‌اش
    - valid_coords: نقاط معتبر (برای رسم)
    """
    radius = mask.shape[0] // 2
    valid_coords = np.array(np.where(mask == 1)).T
    prop = float(sample_size / mask.sum())

    distances = np.sqrt((valid_coords[:, 0] - center[0])**2 + (valid_coords[:, 1] - center[1])**2)
    strata_edges = np.linspace(0, radius, n_strata + 1)
    strata_indices = np.digitize(distances, strata_edges) - 1  # from 0

    sample_stratified = []
    for i in range(n_strata):
        stratum_coords = valid_coords[strata_indices == i]
        sample_per_stratum = int(len(stratum_coords) * prop)
        if len(stratum_coords) >= sample_per_stratum and sample_per_stratum > 0:
            sample = stratum_coords[np.random.choice(len(stratum_coords), sample_per_stratum, replace=False)]
            sample_stratified.append(sample)

    if len(sample_stratified) == 0:
        return np.empty((0, 2)), strata_indices, valid_coords

    sample_stratified = np.vstack(sample_stratified)
    return sample_stratified, strata_indices, valid_coords


def plot_stratified_samples(mask, center, sample_stratified, strata_indices, valid_coords, n_strata=3):
    """
    رسم ویفر با نمونه‌گیری طبقه‌ای

    پارامترها:
    - mask: ماسک
    - center: مرکز ویفر
    - sample_stratified: نمونه‌های انتخاب‌شده
    - strata_indices: لیبل هر نقطه معتبر
    - valid_coords: مختصات نقاط معتبر
    - n_strata: تعداد طبقات
    """
    wafer_size = mask.shape[0]
    fig, ax = plt.subplots(figsize=(8, 8))
    cmap = plt.cm.get_cmap("Blues")
    ax.pcolormesh(np.arange(wafer_size + 1), np.arange(wafer_size + 1), mask,
                  cmap=cmap, edgecolors='gray', linewidth=0.5, shading='auto')

    ax.plot(center[1] + 0.5, center[0] + 0.5, 'rx', markersize=10, label='Center')

    # رنگ برای طبقات مختلف
    colors = ['green', 'orange', 'purple', 'cyan', 'brown', 'pink']
    for i in range(n_strata):
        stratum_coords = valid_coords[strata_indices == i]
        ax.scatter(stratum_coords[:, 1] + 0.5, stratum_coords[:, 0] + 0.5,
                   color=colors[i % len(colors)], alpha=0.6, label=f'Stratum {i+1}', s=10)

    ax.scatter(sample_stratified[:, 1] + 0.5, sample_stratified[:, 0] + 0.5,
               color='red', label='Stratified Samples', s=30)

    ax.set_aspect('equal')
    ax.set_xlim(0, wafer_size)
    ax.set_ylim(0, wafer_size)
    ax.invert_yaxis()
    ax.set_xticks(np.arange(wafer_size + 1))
    ax.set_yticks(np.arange(wafer_size + 1))
    ax.grid(which='both', color='lightgray', linewidth=0.5)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_title(f"Stratified Sampling on Circular Wafer ({wafer_size}×{wafer_size})", fontsize=14)
    ax.legend(loc='upper right')
    plt.tight_layout()
    plt.show()
