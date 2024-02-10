import regex as re
import pre_processing


def extract_info_by_title(text, title):
    pattern = rf"{title}:\n((.|\n)*?)(?=\n\n|\Z)"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        return None


class TopicsData:
    experience = None
    education = None
    skills = None
    extra = None

    experience_processed = None
    education_processed = None
    skills_processed = None
    extra_processed = None

    def __init__(self, raw_summary):
        self.experience = extract_info_by_title(raw_summary, "Опыт работы")
        self.education = extract_info_by_title(raw_summary, "Образование")
        self.skills = extract_info_by_title(raw_summary, "Ключевые навыки")
        self.extra = extract_info_by_title(raw_summary, "Дополнительная информация")

    def perform_pre_processing(self):
        self.experience_processed = pre_processing.PreProcessor(self.experience).tokens
        self.education_processed = pre_processing.PreProcessor(self.education).tokens
        self.skills_processed = pre_processing.PreProcessor(self.skills).tokens
        self.extra_processed = pre_processing.PreProcessor(self.extra).tokens

