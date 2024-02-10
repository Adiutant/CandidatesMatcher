from gigachat import GigaChat
import os


def prompt_summarize(text):
    topics = "опыт работы, образование, ключевые навыки, дополнительная информация "
    prompt = ("Разбей текст этого резюме на темы и напиши в каждой теме предложения из текста резюме соответствующие "
              "этим темам. не добавляй темы которые не указаны"
              f" Темы на которые надо разбить это {topics}  "
              f" {text}")
    return prompt


def prompt_summarize_job(text):
    topics = "опыт работы, образование, ключевые навыки, дополнительная информация"
    prompt = (
        "Разбей текст описания вакансии на темы и напиши в каждой теме предложения из текста вакансии соответствующие "
        "этим темам. не добавляй темы которые не указаны"
        f" Темы на которые надо разбить это {topics} "
        f" {text}")
    return prompt


class LlmProcessor:
    result = None

    def __init__(self, file_data, prompt):
        creds = os.getenv("GIGACHAT_API_KEY")
        if creds is None:
            print("Set env GIGACHAT_API_KEY to your api key")
            exit(1)
        with GigaChat(credentials=creds, verify_ssl_certs=False) as giga:
            response = giga.chat(prompt)
            self.result = response.choices[0].message.content
