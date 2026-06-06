"""
Project configuration.
"""
import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

DATA_DIR        = os.path.join(PROJECT_ROOT, "data")
RAW_DIR         = os.path.join(DATA_DIR, "raw")
EXTERNAL_DIR    = os.path.join(DATA_DIR, "external")
PROCESSED_DIR   = os.path.join(DATA_DIR, "processed")
OLD_DATA_DIR    = os.path.join(RAW_DIR, "old")
ANODATA_DIR     = os.path.join(RAW_DIR, "anodata")
ANTIVIRAL_DIR   = os.path.join(RAW_DIR, "antiviral")
SUPP_DATA_DIR   = os.path.join(EXTERNAL_DIR, "supp_data")
PEPTIPEDIA_DIR  = os.path.join(EXTERNAL_DIR, "Peptide_bioactivity-DB-main")

MODEL_DIR           = os.path.join(PROJECT_ROOT, "models")
CHECKPOINT_DIR      = MODEL_DIR
BEST_MODEL_PATH     = os.path.join(MODEL_DIR, "best_model.pth")

# ── Classification (6 classes) ──
NUM_CLASSES = 6
CATEGORY_NAMES = [
    "AntiCancer",        # 0
    "AntiFungal",        # 1
    "AntiGramPos",       # 2
    "AntiGramNeg",       # 3
    "AntiViral",         # 4
    "AntiHypertensive",  # 5
]

# ── ESM ──
ESM_MODEL       = "facebook/esm2_t30_150M_UR50D"
ESM_DIM         = 640
ESM_BATCH_SIZE  = 64

# ── Graph ──
NODE_DIM   = 78
MAX_ATOMS  = 100

# ── Sequence encoding ──
SEQ_MAX_LEN = 100
FP_DIM      = 2048

# ── Training ──
BATCH_SIZE       = 32
EPOCHS           = 50
LR               = 5e-4
WEIGHT_DECAY     = 5e-4
NUM_WORKERS      = 4
PATIENCE         = 15
FOCAL_LOSS_GAMMA = 2.0
SMOTE_MIN_SAMPLES = 5000
SMOTE_TARGET     = 10000
MAX_PER_CLASS    = 15000
VAL_RATIO        = 0.2
TEST_RATIO       = 0.1
BALANCED_SAMPLER   = True
CLASS_WEIGHT_TYPE  = "median"

# ── Model ──
USE_MULTI_MODAL  = True

# ── Self-training ──
PSEUDO_LABEL_THRESHOLD = 0.85

# ── Infer ──
INFER_BATCH_SIZE = 64
