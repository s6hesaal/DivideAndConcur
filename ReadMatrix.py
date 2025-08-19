import scipy.io
import scipy.sparse
from sklearn.preprocessing import normalize


def readMatFile(path, normaliseRows=True):
    mat_contents = scipy.io.loadmat(path, squeeze_me=True)
    data = mat_contents['Problem'].item()
    A = next(item for item in data if isinstance(item, scipy.sparse.spmatrix))

    if scipy.sparse.issparse(A):
        A = A.toarray()

    if normaliseRows:
        A = normalize(A, axis=1, norm="l2")

    return A

