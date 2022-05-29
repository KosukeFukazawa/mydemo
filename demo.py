import numpy as np

a = "なんじ、ぶんがくとかがくのちからをしんじよ"
b = "じょうほうぶんせきしてかいぜんあくしょん"
output = ""

# Initialize
lcs_mat = np.zeros((len(a)+1, len(b)+1), dtype=int)

# Create lcs matrix
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            lcs_mat[i+1,j+1] = lcs_mat[i,j] + 1
        else:
            lcs_mat[i+1,j+1] = max(lcs_mat[i+1,j], lcs_mat[i,j+1])

# Inverse order
i, j = len(a), len(b)

while i > 0 and j > 0: 
    while lcs_mat[i,j] == lcs_mat[i,j-1]:
        j = j - 1
    while lcs_mat[i,j] == lcs_mat[i-1,j]:
        i = i - 1
    output += a[i-1]
    i = i - 1
    j = j - 1
print(output[::-1])