MAX_INPUT_LENGTH = 512
MAX_TARGET_LENGTH = 256
MODEL_NAME = "t5-base"
BATCH_SIZE = 2
NUM_EPOCHS = 3
LEARNING_RATE = 1e-3
GQA_LIST = ["decoder", "EncDecAttention"]
REVERSE_GQA_LIST = ["encoder", "decoder", "EncDecAttention"]
WANDB_API_KEY = "dccc66c538af2f9beb7dd2e8cbc9e468040afd23"
WANDB_PROJECT = "WGQA_T5_3b"
WANDB_ENTITY = "saisena"
VAL_BATCH_SIZE = 2
IF_RANDOM = False
TOKENIZE_BATCH_SIZE = 300
INTERVAL_STEPS = 24000
PERCENT_DATA = 100
SHORT_SIMILARITY_INTERVAL = 200
LONG_SIMILARITY_INTERVAL = 1000
