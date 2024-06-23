# LLM
# ------------------------------------------------------------------------------
import os

AZURE_OPENAI_ENDPOINT = 'https://dev-aicrm.openai.azure.com/'
AZURE_OPENAI_API_KEY = '92fa6fca25004b618c1fbed8ab1bceb9'
AZURE_DEPLOYMENT = 'g35t16k_0613_10k'
OPENAI_API_VERSION = '2024-02-15-preview'


def set_openai_environ():
    os.environ['AZURE_OPENAI_API_KEY'] = AZURE_OPENAI_API_KEY
    os.environ['AZURE_OPENAI_ENDPOINT'] = AZURE_OPENAI_ENDPOINT
    os.environ['AZURE_DEPLOYMENT'] = AZURE_DEPLOYMENT
    os.environ['OPENAI_API_VERSION'] = OPENAI_API_VERSION
