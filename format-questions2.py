from string import Formatter
from typing import List, Union, Type
from pydantic import BaseModel
from pydantic import create_model
import os
import reasoner
import chatgpt
import openai
# os.environ["OPENAI_API_KEY"] = 
openai.api_key = "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"#open('openai_key.txt', 'r').read().strip('\n')

pdf_data = """
18.443 Problem Set 3 Spring 2015
Statistics for Applications
Due Date: 2/27/2015
prior to 3:00pm

Problems from John A. Rice, Third Edition. [Chapter.Section.Problem]

1. Problem 8.10.21.

2. Problem 8.10.45. A Random walk Model for Chromatin
Only parts (a) through (g). See R script file “Rproject3.script4.Chromatin.r” in Rproject3. You can edit this file for your answers; turn in hard-copy of an html file compiled by creating a “notebook” from the script (press the button on the script window that looks like a notebook). Circle/highlight your answers on the hard-copy.

3. Problem 8.10.51 Double Exponential (Laplace) Distribution

4. Problem 8.10.58 Gene Frequencies of Haptoglobin Type See R Script file “Rproject3.script1.multinomial.simulation.r” in Rproject3. You can edit this file for your answers; turn in hard-copy of an html file compiled by creating a “notebook” from the script (press the button on the script window that looks like a notebook). Circle/highlight your answers on the hard-copy.

1

MIT OpenCourseWare
http://ocw.mit.edu

18.443 Statistics for Applications
Spring 2015

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

"""

class FancyStructuredReasoner(reasoner.Reasoner):
    def __init__(self, system_prompt=None, model='gpt-4'):
        super().__init__(system_prompt, model)

    def extract_info(self, info_format, output_type: Union[BaseModel, Type]):
        """
        Extracts a piece of information in a specific format.
        This is done by using the function calling API to create a remember_{field_name} function and executing it.

        This function is useful when you want to extract the outcome of an internal monologue in a specific format.
        It doesn't work so well for reasoning, so stick to the paradigm of internal monologue -> extract_info.
        The format string is a python format string that determines the format of the stored information.

        Parameters:
        info_format (str):
            The format string that determines the format of the stored information.
        output_type (Union[BaseModel, Type]):
            The type of the field to be extracted.
            If a pydantic BaseModel is provided, the field is extracted as a pydantic model.
            If a python Type is provided, the field is extracted as an instance of that type.

        Returns:
        The value of the field remembered by the reasoner

        Examples:
        --------
        Extracting an integer:
        >>> reasoner.add_message('user', "My name's Bill, I'm a 42 y.o. male from New York.")
        >>> reasoner.extract_info("The user is {age} years old.", int)
        25

        Extracting an enum:
        >>> from enum import Enum
        >>> reasoner.add_message("assistant", "I have logically deduced that I am happy.")
        >>> reasoner.extract_info("I am {state}", Enum('MentalState', 'HAPPY SAD'))
        "HAPPY"

        Extracting a pydantic model:
        >>> from pydantic import BaseModel
        >>> class Person(BaseModel):
        ...     name: str
        ...     twitter_handle: str
        ...     is_based: bool = False
        >>> reasoner.add_message("user", "Add Ivan Yevenko (@ivan_yevenko) to the database, he's pretty based.")
        >>> reasoner.extract_info("Added {person} to the database.", Person)
        Person(name='Ivan Yevenko', twitter_handle='@ivan_yevenko', is_based=True)
        """
        formatter = Formatter()
        parsed = [x for x in formatter.parse(info_format) if x[1] is not None]
        assert len(parsed) == 1, "Only one format field is allowed."

        _, field_name, _, _ = parsed[0]

        use_pydantic = type(output_type) is type and issubclass(output_type, BaseModel)
        if use_pydantic:
            params = output_type.model_json_schema()
        else:
            SingleFieldModel = create_model("SingleFieldModel", **{field_name: (output_type, ...)})
            params = SingleFieldModel.model_json_schema()

        func_name = "remember_" + field_name
        json_schema = {
            "name": func_name,
            "description": f"This function stores a piece of information in the format: '{info_format}'.",
            "parameters": params
        }

        response = chatgpt.complete(messages=self.messages, model=self.model, functions=[json_schema], function_call={'name': func_name}, use_cache=True)
        if response['role'] != 'function':
            raise Exception(f"Expected a function call, but got: {response['content']}")

        value = response['args']
        if use_pydantic:
            value = output_type.model_construct(value)
        else:
            try:
                value = value[field_name]
            except KeyError:
                # Generated JSON schema is sometimes incorrect, so we try to extract the field anyway
                value = value.popitem()[1]

        info = info_format.format(**{field_name: value})
        self.add_message('function', f'Stored information: "{info}"', name=response['name'])
        return value
    

from pydantic import BaseModel
class Problem(BaseModel):
    assignment: int
    course_code: str

os.environ["OPENAI_API_KEY"] = open('openai_key.txt', 'r').read().strip('\n')
# reasoner = FancyStructuredReasoner(system_prompt="DO NOT OUTPUT ANY MORE TEXT AFTER ANSWERING THE PROMPT. BE A ROBOT.", model='gpt-3.5-turbo')
reasoner = FancyStructuredReasoner(system_prompt="DO NOT OUTPUT ANY MORE TEXT AFTER ANSWERING THE PROMPT. BE A ROBOT.", model='gpt-3.5-turbo')
# reasoner.add_message('user', pdf_data)
# print(reasoner.extract_info("The textbook name and author is {name_and_author}", str))
reasoner.add_message("user", "Please submit your solutions to assignment 5 from MIT opencourseware course code 3E.45")
print(reasoner.extract_info("the assignment number is {x}", int))
print(reasoner.extract_info("the course code is {x}", str))


# print(reasoner.extract_info("", List[str]))
# reasoner.add_message('user', """ONLY RETURN A STRING ARRAY OF EACH PROBLEM IN THIS FORMAT ["Chapter.Section.Problem"].""")