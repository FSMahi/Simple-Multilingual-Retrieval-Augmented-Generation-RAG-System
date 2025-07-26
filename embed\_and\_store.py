import uuid
from langchain.vectorstores import Chroma
from langchain.storage import InMemoryStore
from langchain.schema.document import Document
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.retrievers.multi_vector import MultiVectorRetriever
embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# Vectorstore to index the child chunks
vectorstore = Chroma(
    collection_name="multi_modal_rag",
    embedding_function=embedding_function
)

# In-memory document store for parent docs
store = InMemoryStore()
id_key = "doc_id"

# Multi-vector retriever
retriever = MultiVectorRetriever(
    vectorstore=vectorstore,
    docstore=store,
    id_key=id_key,
)
# Example parent doc
parent_doc_id = str(uuid.uuid4())
parent_doc = Document(page_content="এই নথিতে বাংলা সাহিত্য নিয়ে আলোচনা করা হয়েছে।", metadata={id_key: parent_doc_id})

# Chunk the parent doc (simulate 2 chunks)
child_chunks = [
    Document(page_content="বাংলা সাহিত্যের সূচনা মধ্যযুগে।", metadata={id_key: parent_doc_id}),
    Document(page_content="রবীন্দ্রনাথ বাংলা সাহিত্যের একজন অগ্রগামী কবি।", metadata={id_key: parent_doc_id}),
]

# Store in vector DB and doc store
vectorstore.add_documents(child_chunks)
store.mset([(parent_doc_id, parent_doc)])
retrieved_docs = retriever.get_relevant_documents("রবীন্দ্রনাথ সম্পর্কে তথ্য দিন")

