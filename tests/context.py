import sys
import os
import pytest
# add project to os path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class Context:
    sample_good_schema = []

    sample_bad_schema = []    

    sample_good_data = []

    sample_bad_data = []
