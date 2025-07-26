questions = {
    "অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?",
    "কাকে অনুপমের ভাগ্য দেবতা বলে উল্লেখ করা হয়েছে?",
    "বিয়ের সময় কল্যাণীর প্রকৃত বয়স কত ছিল?",
}
for question, expected in questions.items():
    # Step 1: Retrieve relevant context
    docs = retriever.get_relevant_documents(question)
    context = "\n".join([doc.page_content for doc in docs])

    # Step 2: Ask the question
    answer = qa_chain.invoke({"context": context, "question": question})

    # Step 3: Output
    print("🧑‍💻 প্রশ্ন:", question)
    print("✅ প্রত্যাশিত উত্তর:", expected)
    print("🤖 মডেল এর উত্তর:", answer.strip())
    print("-" * 60)
