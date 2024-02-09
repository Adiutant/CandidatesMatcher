import pipeline


def main(jobs_dir, cv_file):
    pipeline.perform_pipeline(jobs_dir, cv_file)


if __name__ == '__main__':
    print("Запуск только из __main__")
