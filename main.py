import reasoner
import find_pdf_on_web
import os
import wget
import gpt4v_api
from agent import run_raw_assignment_parser_agent, run_unknown_source_agent, run_generate_answer_agent, add_wiki
import json
from generate_pdf import generate_pdf

def main():
    os.environ["OPENAI_API_KEY"] = open('openai_key.txt', 'r').read().strip('\n')
    input_text = "[X=18.650], [Y=1]"
    fsreasoner = reasoner.FancyStructuredReasoner(system_prompt="DO NOT OUTPUT ANY MORE TEXT AFTER ANSWERING THE PROMPT. BE A ROBOT.", model='gpt-3.5-turbo')
    fsreasoner.add_message("user", input_text)
    course_code = fsreasoner.extract_info("the course code is X={x}", str)
    assignment_num = fsreasoner.extract_info("the assignment number is Y={x}", str)
    information_to_find = "assignment page for MIT opencourseware course code " + str(course_code)

    print("information_to_find: ", information_to_find)
    pdf_url = find_pdf_on_web.look_for_information(assignment_num, course_code)

    print("url for assignment pdf: ", pdf_url)
    if os.path.exists("./problemset.pdf"):
        os.remove("./problemset.pdf")
    wget.download(pdf_url, "./problemset.pdf")
    text_extracted = gpt4v_api.extract_text_from_pdf("problemset.pdf")

    print("===== TEXT EXTRACTED =====")
    print(text_extracted)
    print("==========================")

    parsed_assignment = run_raw_assignment_parser_agent(text_extracted)

    print("===== PARSED ASSIGNMENT =====")
    print(parsed_assignment)
    print("=============================")
    
    questions = parsed_assignment['questions']

    # unknown_sources = run_unknown_source_agent(questions)

    # print("===== UNKNOWN SOURCES =====")
    # print(unknown_sources)
    # print("===========================")

    questions_wiki = [add_wiki(question) for question in questions]
    
    print("===== QUESTION WIKI =====")
    print(questions_wiki)
    print("=========================")

    answers = run_generate_answer_agent(questions_wiki)

    # answers = generated_answers['answers']

    print("===== ANSWERS =====")
    print(answers)
    print("===================")

    generate_pdf(questions_wiki, answers)

if __name__ == "__main__":
    main()



