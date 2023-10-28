from .utils import * 
from .aggregate import *
from pathlib import Path
from .search import *

def get_answers(questions: list, question_unknowns: Dict[str, list], textbook=None):

    if textbook is not None:
        pass

    answers = []
    for question in questions:
        unknowns_for_question = question_unknowns[question]
        rel_sources, rel_info = return_relevant_results(unknowns_for_question)   

        rel_sources_str = json.dumps(rel_sources)
        rel_info_str = json.dumps(rel_info)

        query_prompt = fill_prompt(
            Path("./web_searches/prompts/answer_question.prompt"),
            question=question,
            # TODO: Remember to replace this
            textbook="Not defined",
            sources=rel_sources_str,
            context=rel_info_str
        )

        print("Going to prompt GPT4 with the query prompt for ")
        answer = prompt_chatgpt(query_prompt)
        print(f"Got answer for {question}")
        print(answer)
        answers.append(answer)

    return answers