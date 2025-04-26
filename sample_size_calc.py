import math
from scipy.stats import norm

def calculate_sample_size(confidence_level=0.95, p=0.5, E=0.05):
    """
    محاسبه حجم نمونه مورد نیاز برای تخمین نسبت (p)
    
    پارامترها:
    - confidence_level: سطح اطمینان (مثلاً 0.95)
    - p: نسبت مورد انتظار (مثلاً 0.2)
    - E: خطای مجاز (مثلاً 0.05)
    
    خروجی:
    - sample_size: حجم نمونه به صورت عدد صحیح
    """
    alpha = 1 - confidence_level
    z_score = norm.ppf(1 - alpha / 2)
    n = (z_score**2 * p * (1 - p)) / (E**2)
    sample_size = math.ceil(n)
    return sample_size
