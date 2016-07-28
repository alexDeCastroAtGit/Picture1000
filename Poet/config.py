import os

base_dir = os.path.abspath(os.path.dirname(__file__))
SAMPLE_LENGTH = 32

# TRAINING
MAX_EPOCHS = 30
NUM_STEPS = 16
NUM_LAYERS = 2
BATCH_SIZE = 32
KEEP_PROB = 0.5
HIDDEN_SIZE = 512
WORD_EMBEDDING_SIZE=64
THEME_EMBEDDING_SIZE=32
NUM_POEMS = -1 #1024
INIT_SCALE = 0.05
LEARNING_RATE = .01

# DEVELOPMENT TESTING:
# MAX_EPOCHS = 50
# NUM_STEPS = 8
# NUM_LAYERS = 2
# BATCH_SIZE = 2
# KEEP_PROB = 0.1
# HIDDEN_SIZE = 32
# NUM_POEMS = 5
# WORD_EMBEDDING_SIZE=16
# THEME_EMBEDDING_SIZE=16