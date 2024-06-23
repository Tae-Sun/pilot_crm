import utils.creative_build.config

import httpx
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from utils.creative_build.config import AZURE_DEPLOYMENT, OPENAI_API_VERSION
from langchain_openai import AzureChatOpenAI

from utils.creative_build.rules import CopyWritingRules

from utils.creative_build.config import set_openai_environ


class AICRMLLMBase:
    def __init__(
            self,
            openai_api_version=OPENAI_API_VERSION, azure_deployment=AZURE_DEPLOYMENT
    ):
        self.model = AzureChatOpenAI(
            openai_api_version=openai_api_version,
            azure_deployment=azure_deployment,
            http_client=httpx.Client(verify=False)
        )


class CopyWritingAI(AICRMLLMBase):
    def generate(self, prompt_string):
        rules = CopyWritingRules.get_all_rules()

        messages = []
        reverse_keys = sorted(rules.keys(), reverse=True)
        for k in reverse_keys:
            messages.append(SystemMessage(
                content=rules[k]
            ))

        messages.append(HumanMessage(content=prompt_string))

        return self.model.invoke(messages)


if __name__ == '__main__':
    set_openai_environ()
    cwai = CopyWritingAI()
    print(cwai.generate('생일을 축하해주는 문구를 만들어줘'))