import numpy as np


def append_smote_modalities(train_graph_raw, train_seq, train_fp, parent_idx):
    """Append synthetic-sample modalities in the same order as SMOTE outputs."""
    synthetic_graph = [train_graph_raw[i] for i in parent_idx]
    synthetic_seq = [train_seq[i] for i in parent_idx]
    synthetic_fp = [train_fp[i] for i in parent_idx]

    train_graph = train_graph_raw + synthetic_graph
    train_seq = np.vstack([train_seq] + synthetic_seq)
    train_fp = np.vstack([train_fp] + synthetic_fp)
    return train_graph, train_seq, train_fp
