from gigachat import GigaChat
import os


def prompt_summarize(text):
    topics = "опыт работы, образование, ключевые навыки, дополнительная информация"
    prompt = ("Разбей текст этого резюме на темы и напиши в каждой теме предложения из текста резюме соответствующие "
              "этим темам."
              f" Темы на которые надо разбить это {topics}"
              f" {text}")
    return prompt


class LlmProcessor:
    def __init__(self, file_data):
        prompt = prompt_summarize(file_data)
        creds = os.environ.get('GIGACHAT_API_KEY')
        with GigaChat(credentials=creds, verify_ssl_certs=False) as giga:
            response = giga.chat(prompt)
            print(response.choices[0].message.content)
