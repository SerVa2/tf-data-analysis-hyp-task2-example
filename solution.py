import pandas as pd
import numpy as np


from scipy.stats import chisquare
chat_id = 1633714108 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Статистика Хи-квадрат для двух выборок
    alpha = 0.08
    bins = 10 # количество интервалов
    _, bins = np.histogram(np.concatenate((x,y)), bins=bins)
    x_counts, _ = np.histogram(x, bins=bins)
    y_counts, _ = np.histogram(y, bins=bins)
    stat, p = chisquare(y_counts, f_exp=x_counts)
    return p < alpha
