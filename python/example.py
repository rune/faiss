import numpy as np
d = 64
nb = 100
np.random.seed(1234)
xb = np.random.random((nb, d)).astype('float32')
xb[:, 0] += np.arange(nb) / 1000.

import faiss
_sub_index = faiss.IndexFlatL2(d)
index = faiss.IndexIDMap2(_sub_index)
print(index.is_trained)
index.add_with_ids(xb, np.arange(start=10, stop=10+nb)) # type: ignore
print(index.ntotal)

k = 4
D, I = index.search(xb[:5], k) # type: ignore

arr = []
ids = index.get_ids() # type: ignore
print(ids)
print(ids[0])