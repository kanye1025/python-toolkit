import  numpy as np


def cosine(x1,x2):
	num = np.dot(x1.T , x2)
	denom = np.linalg.norm(x1) * np.linalg.norm(x2)
	cos = num / denom
	return cos


