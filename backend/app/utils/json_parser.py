import json
import re


class JSONParser:

    @staticmethod
    def parse_json(text):

        try:
            return json.loads(text)

        except json.JSONDecodeError:

            cleaned_text = re.sub(
                r"```json|```",
                "",
                text
            ).strip()

            return json.loads(cleaned_text)