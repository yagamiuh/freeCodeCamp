import numpy as np

def apply_method(f, matrix):
    f_axis1 = f(matrix, axis=0)
    f_axis2 = f(matrix, axis=1)
    f_all = f(matrix)
    return (list(f_axis1), list(f_axis2), f_all)

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    matrix = np.reshape(np.asarray(list), (3,3))
    
    mean_axis1, mean_axis2, mean_all = apply_method(np.mean, matrix)
    var_axis1, var_axis2, var_all = apply_method(np.var, matrix)
    std_axis1, std_axis2, std_all = apply_method(np.std, matrix)
    max_axis1, max_axis2, max_all = apply_method(np.amax, matrix)
    min_axis1, min_axis2, min_all = apply_method(np.amin, matrix)
    sum_axis1, sum_axis2, sum_all = apply_method(np.sum, matrix)

    calculations = {
        "mean": [mean_axis1, mean_axis2, mean_all],
        "variance": [var_axis1, var_axis2, var_all],
        "standard deviation": [std_axis1, std_axis2, std_all],
        "max": [max_axis1, max_axis2, max_all],
        "min": [min_axis1, min_axis2, min_all],
        "sum": [sum_axis1, sum_axis2, sum_all],
    }

    return calculations