
import reasoner
import find_pdf_on_web
import os
import wget
import gpt4v_api

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
    print(text_extracted)
main()