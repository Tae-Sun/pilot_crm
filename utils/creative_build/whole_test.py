from langchain_community.document_loaders.unstructured import UnstructuredFileLoader
from langchain_community.vectorstores.chroma import Chroma
from langchain_text_splitters import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings

from utils.creative_build.config import set_openai_environ

set_openai_environ()

splitter = CharacterTextSplitter.from_tiktoken_encoder(
    separator='----------' * 5,
    chunk_size=1000,
    chunk_overlap=100,
)
import os
path = os.path.abspath('./push_messages.txt')
loader = UnstructuredFileLoader(path)

docs = loader.load_and_split(text_splitter=splitter)

embeddings = OpenAIEmbeddings()

vectorstore = Chroma.from_documents(
    documents=docs, embedding=embeddings
)

results = vectorstore.similarity_search('피자 광고는 어떻게 해야할까?')

print(results)
