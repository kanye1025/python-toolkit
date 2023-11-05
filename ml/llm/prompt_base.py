from copy import deepcopy
import json


class PromptBase:
    def __init__(self):
        self.prompts = {}

    def create_prompt_by_name(self, prompt_name, replace_content):
        return self.create_prompt(self.prompts[prompt_name], replace_content)

    @classmethod
    def create_prompt(cls, prompt, replace_content):
        prompt = deepcopy(prompt)
        for k, v in replace_content.items():
            k = '{' + k + '}'
            prompt = prompt.replace(k, v)
        return prompt

    @classmethod
    def to_json_str(cls, obj):
        text = json.dumps(obj, ensure_ascii=False)
        return f"```json\n{text}\n```\n"