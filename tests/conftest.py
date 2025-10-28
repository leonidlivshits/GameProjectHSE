import sys
import os

HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, ".."))
SRC = os.path.join(ROOT, "src")


if SRC not in sys.path:
    sys.path.insert(0, SRC)