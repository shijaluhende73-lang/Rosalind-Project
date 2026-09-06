def mendel_probability(k, m, n):
    total = k + m + n
    p_nn = (n / total) * ((n - 1) / (total - 1))
    p_nm = 2 * (n / total) * (m / (total - 1)) * 0.5
    p_mm = (m / total) * ((m - 1) / (total - 1)) * 0.25
    total_recessive = p_nn + p_nm + p_mm
    return 1 - total_recessive
print(mendel_probability(25 , 22, 23))