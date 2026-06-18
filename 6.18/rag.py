from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama

from langchain_chroma import Chroma

# 1. 加载PDF
loader = PyMuPDFLoader("paper.pdf")
docs = loader.load()

print(f"读取到 {len(docs)} 页")

# 2. 切块
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(docs)

print(f"生成 {len(chunks)} 个文本块")

# 3. Embedding模型
embeddings = OllamaEmbeddings(
    model="mxbai-embed-large"
)

# 4. 建立向量库
vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings
)

print("向量库建立完成")

# 5. 检索
question = input("请输入问题：")

results = vector_db.similarity_search(
    question,
    k=3
)

context = "\n\n".join(
    [doc.page_content for doc in results]
)

# 6. 大模型
llm = ChatOllama(
    model="deepseek-r1:7b"
)

prompt = f"""
请根据下面内容回答问题。

内容：
{context}

问题：
{question}
"""

response = llm.invoke(prompt)

print("\n===== 回答 =====\n")
print(response.content)