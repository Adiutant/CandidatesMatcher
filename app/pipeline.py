import os
from os.path import join, isfile
import pre_processing


def perform_pipeline(jobs_dir, cv):
    only_files = [jobs_dir + f for f in os.listdir(jobs_dir) if isfile(join(jobs_dir, f))]
    for file in only_files:
        with open(file) as f:
            lines = f.readlines()
            text = "".join(lines)
            pre_processing.PreProcessor(text)
