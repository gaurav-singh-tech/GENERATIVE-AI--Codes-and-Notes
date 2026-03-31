from huggingface_hub import InferenceClient
import os

client = InferenceClient(token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"))
models = client.list_models()
print(models)