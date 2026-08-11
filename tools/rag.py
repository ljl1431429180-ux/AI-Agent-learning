from langchain_community.document_loaders import TextLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma

from langchain_ollama import OllamaEmbeddings



# 加载知识库

loader = TextLoader(
    "knowledge/products.txt",
    encoding="utf-8"
)


documents = loader.load()



# 文档切分

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)


docs = splitter.split_documents(documents)



# 创建Embedding

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)



# 创建向量数据库

vectorstore = Chroma.from_documents(
    docs,
    embeddings
)



# 创建搜索器

retriever = vectorstore.as_retriever(
    search_kwargs={
        "k":3
    }
)



def search_knowledge(query):

    results = retriever.invoke(query)


    content = ""


    for doc in results:

        content += doc.page_content + "\n"


    return content