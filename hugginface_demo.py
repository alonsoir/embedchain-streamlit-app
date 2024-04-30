import os
from dotenv import load_dotenv
import shutil
from embedchain import App


def clean_home():
  # Obtén la ruta absoluta del directorio actual
  current_dir = os.path.dirname(os.path.abspath(__file__))
  # Construye la ruta relativa a la carpeta db
  db_path = os.path.join(current_dir, 'db')
  # Elimina la carpeta db y su contenido
  shutil.rmtree(db_path)
  print("db_path deleted.")



load_dotenv()
config = {
  'llm': {
    'provider': 'huggingface',
    'config': {
      'model': 'mistralai/Mistral-7B-Instruct-v0.2',
      'top_p': 0.5
    }
  },
  'embedder': {
    'provider': 'huggingface',
    'config': {
      'model': 'sentence-transformers/all-mpnet-base-v2'
    }
  }
}
app = App().from_config(config=config)
print("app initialized.")
app.add("https://www.forbes.com/profile/elon-musk")
print("url added to the app.")
app.add("https://en.wikipedia.org/wiki/Elon_Musk")
print("url added to the app.")
query = "What is the net worth of Elon Musk today?"
print(query)
response = app.query(query)
print(response)
# Answer: The net worth of Elon Musk today is $258.7 billion.
clean_home()

