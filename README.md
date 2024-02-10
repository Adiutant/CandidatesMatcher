# CandidatesMatcher
There is a possible hackathon solution for matching candidates CV and Job descriptions 

# Возможный пайплайн
И резюме и описание вакансии, скорее всего, будут представлены в формате rtf и скорее всего в формате hh. Для чтения попробуем python-docx
Изначально следует суммаризовать тексты по тематическим топикам, чтобы дальнейшее сравнение происходило в рамках векторизованных топиков а не всего текста.
Если не разбивать на топики, то детерминированные алгоритмы, выполняющие классификацию с помощью метрики расстояния между векторами будет работать неэффективно, так как тексты могут быть похожи, но иметь разный порядок топиков,
что увеличит расстояние.
а еще это сходу можно тогда обернуть в json (к слову о втором задании)
Затем следует токенизировать топики (привести к списку слов) 
провести стемминг (алгоритмический стемминг)
векторизовать
затем использовать метод, например k-means для нахождения кандидатов соответствующих вакансиям. 
Как вторую итерацию можно попробовать LLM модели для классификации
