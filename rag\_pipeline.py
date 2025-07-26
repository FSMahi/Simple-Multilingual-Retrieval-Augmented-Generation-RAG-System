!ollama pull gemma:2b

!ollama pull mistral

!pip install langchain-ollama langchain-google-genai

!pip install langchain_ollama langchain_google_genai langchain langchain-community langchain-core

from langchain_ollama import OllamaEmbeddings
from langchain.vectorstores import FAISS

# Initialize the Ollama embeddings
embedding_model = OllamaEmbeddings(model="nomic-embed-text")
from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser

# ✅ Define the summarization prompt in Bengali
prompt_text = """
তুমি একজন সহকারী, যার কাজ হলো নিচের টেবিল বা লেখার অংশের সংক্ষিপ্ত সারাংশ তৈরি করা।

শুধুমাত্র সারাংশ দাও, কোনো অতিরিক্ত মন্তব্য করো না।
"এইটা সারাংশ" বা এরকম কিছু দিয়ে শুরু করো না।

টেবিল বা লেখার অংশ: {element}
"""

# ✅ Create the prompt template
prompt = ChatPromptTemplate.from_template(prompt_text)

# ✅ Load Ollama model (change model name as needed)
model = ChatOllama(model="gemma:2b")

# ✅ Build the summarization chain
summarize_chain = {"element": lambda x: x} | prompt | model | StrOutputParser()

tables[0].to_dict()

# If not already defined:
texts = [chunk.text for chunk in chunks if hasattr(chunk, "text")]

text_summaries = summarize_chain.batch(
    [{"element": t} for t in texts],
    config={"max_concurrency": 3}
)
text_summaries


tables_html = [table.metadata.text_as_html for table in tables]

table_summaries = summarize_chain.batch(
    [{"element": html} for html in tables_html],
    config={"max_concurrency": 3}
)
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Bengali prompt template
prompt = PromptTemplate.from_template("""
তুমি একজন সহকারী, যার কাজ হলো নিচের চিত্র বা ডায়াগ্রাম থেকে নেওয়া টেক্সটের সংক্ষিপ্ত ও অর্থপূর্ণ সারাংশ প্রদান করা।

পাঠ্য:
{text}

অনুগ্রহ করে ২-৩ লাইনের মধ্যে সারাংশ লেখো, যাতে চিত্রের মূল বিষয়বস্তু বোঝা যায়।
""")

# Ollama model
model = ChatOllama(model="gemma:2b")

# Build the chain
summarize_chain = prompt | model | StrOutputParser()

