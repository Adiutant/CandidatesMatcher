import pipeline


def main(jobs_file, cv_dir):
    pipeline.perform_pipeline_without_llm_processing(jobs_file, cv_dir)


if __name__ == '__main__':
    print("Запуск только из __main__")
