import os
from os.path import join, isfile

import llm.bert_classifier


def perform_pipeline_without_llm_processing(jobs_file, cv_dir):
    bert_prompt = ""
    jobs_list = None
    jobs_titles = None
    classifier = llm.bert_classifier.BertClassifier()

    with open(jobs_file) as f:
        lines = f.readlines()
        jobs_raw = "".join(lines)
        jobs_list = jobs_raw.split("-------------------")
        f.close()

    only_files = [cv_dir + f for f in os.listdir(cv_dir) if isfile(join(cv_dir, f))]
    for file in only_files:
        match = "None"
        with open(file) as f:
            lines = f.readlines()
            text = "".join(lines)
            bert_prompt = text
            f.close()
        max_similarity = 0
        for job in jobs_list:
            similarity = classifier.embed_bert_cls(bert_prompt) @ classifier.embed_bert_cls(job).T
            if similarity > max_similarity and similarity > 0.70:
                match = job
        with open("result", 'a') as f:
            f.write(file + '\n' + match + '\n')
            f.close()
