import pandas as pd
import numpy as np

from scipy.stats import ks_2samp, chisquare

chat_id = 1633714108 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Критерий Колмогорова-Смирнова для двух выборок
    alpha = 0.08
    stat, p = ks_2samp(x, y)
    return p < alpha
