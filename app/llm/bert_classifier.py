import torch
from transformers import BertTokenizer, AutoModel, AutoTokenizer, BertForSequenceClassification


class BertClassifier:
    def __init__(self):
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.auto_tokenizer = AutoTokenizer.from_pretrained("cointegrated/rubert-tiny2")
        self.auto_model = AutoModel.from_pretrained("cointegrated/rubert-tiny2")
        self.max_len = 512

    # sentence similarity https://huggingface.co/cointegrated/rubert-tiny2
    # embeding @ embeding.T = similarity
    def embed_bert_cls(self, text):
        t = self.auto_tokenizer(text, padding=True, truncation=True, return_tensors='pt')
        with torch.no_grad():
            model_output = self.auto_model(**{k: v.to(self.auto_model.device) for k, v in t.items()})
        embeddings = model_output.last_hidden_state[:, 0, :]
        embeddings = torch.nn.functional.normalize(embeddings)
        return embeddings[0].cpu().numpy()