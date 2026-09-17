import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    # Your code here
    indices = np.arange(n_samples)
    if shuffle:
        np.random.shuffle(indices)
    
    result = []
    for i in range(0, n_samples, n_samples // k):
        step = min(n_samples - i, n_samples // k)
        fold = indices[i : i + step]
        result.append(
            (
                list(np.concatenate((indices[:i], indices[i + step:]), axis=0)), 
                list(fold)
            )
        )
    
    return result