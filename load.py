import uuid
from langchain.schema.document import Document

# Use this id key to maintain parent-child relationship
id_key = "doc_id"

# ✅ Add summarized TEXT chunks
doc_ids = [str(uuid.uuid4()) for _ in texts]
summary_texts = [
    Document(page_content=summary, metadata={id_key: doc_ids[i]})
    for i, summary in enumerate(text_summaries)
]

retriever.vectorstore.add_documents(summary_texts)
retriever.docstore.mset(list(zip(doc_ids, texts)))  # `texts` = parent chunks (original)

# ✅ Add summarized TABLE chunks (if `tables` and `table_summaries` exist)
if tables and table_summaries:
    table_ids = [str(uuid.uuid4()) for _ in tables]
    summary_tables = [
        Document(page_content=summary, metadata={id_key: table_ids[i]})
        for i, summary in enumerate(table_summaries)
    ]

    retriever.vectorstore.add_documents(summary_tables)
    retriever.docstore.mset(list(zip(table_ids, tables)))  # `tables` can be text or HTML

# ✅ Add summarized IMAGE descriptions (if using OCR → text → summary)
if images and image_summaries:
    img_ids = [str(uuid.uuid4()) for _ in images]
    summary_img = [
        Document(page_content=summary, metadata={id_key: img_ids[i]})
        for i, summary in enumerate(image_summaries)
    ]

    retriever.vectorstore.add_documents(summary_img)
    retriever.docstore.mset(list(zip(img_ids, images)))  # `images` are OCR’d texts or descriptions


query = "রবীন্দ্রনাথ ঠাকুর কোন লেখায় উল্লেখ আছে?"
docs = retriever.get_relevant_documents(query)
for d in docs:
    print("🔍 Retrieved:", d.page_content)



