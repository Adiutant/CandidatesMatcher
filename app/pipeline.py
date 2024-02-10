import os
from os.path import join, isfile
import llm.llm_processing
import topics_data

def perform_pipeline(jobs_dir, cv):
    with open(cv) as f:
        lines = f.readlines()
        text = "".join(lines)
        prompt = llm.llm_processing.prompt_summarize(text)
        print("summarizing candidate CV")
        summary = llm.llm_processing.LlmProcessor(text, prompt).result
        print(summary)
        topics = topics_data.TopicsData(summary)
        topics.perform_pre_processing()
        print("tokenized topics")
        print("Опыт работы")
        print(topics.experience_processed)
        print("Образование")
        print(topics.education_processed)
        print("Навыки")
        print(topics.skills_processed)
        print("Дополнительно")
        print(topics.extra_processed)

    only_files = [jobs_dir + f for f in os.listdir(jobs_dir) if isfile(join(jobs_dir, f))]
    for file in only_files:
        with open(file) as f:
            lines = f.readlines()
            text = "".join(lines)
            prompt = llm.llm_processing.prompt_summarize_job(text)
            print("summarizing job description")
            summary = llm.llm_processing.LlmProcessor(text, prompt).result
            print(summary)
            print("NLP preprocessing pipeline")
            topics = topics_data.TopicsData(summary)
            topics.perform_pre_processing()
            print("tokenized topics")
            print("Опыт работы")
            print(topics.experience_processed)
            print("Образование")
            print(topics.education_processed)
            print("Навыки")
            print(topics.skills_processed)
            print("Дополнительно")
            print(topics.extra_processed)

