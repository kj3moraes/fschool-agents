from utils import * 
from aggregate import *
from search import *
from pathlib import Path

def get_answers(questions: List):

    # num_questions = len(questions)

    # all_unknowns = []
    # for i, question in enumerate(questions):
    #     with open(f"unknown_sources_20231028183019/unknown_sources_q{i}", "r+") as f:
    #         unknown = json.load(f)
    #         all_unknowns.append(unknown) 

    # q_ctx_from_textbook = {}
    # if textbook is not None:
    #     for question in questions:
    #         q_unknowns = question_unknowns[question]
    #         print(q_unknowns)

    questions = [
        ' <excerpt>\n21. Suppose that X 1, X 2, . . . , X n are i.i.d. with density function\n\nf (x|θ) = e−(x−θ ),\n\nx ≥ θ\n\nand f (x|θ) = 0 otherwise.\na. Find the method of moments estimate of θ.\nb. Find the mle of θ . (Hint: Be careful, and don’t differentiate before thinking.\n\nFor what values of θ is the likelihood positive?)\n\nc. Find a sufficient statistic for θ.\n\n<excerpt>',
        ' A Random Walk Model for Chromatin. A human chromosome is a very large\nmolecule, about 2 or 3 centimeters long, containing 100 million base pairs (Mbp).\nThe cell nucleus, where the chromosome is contained, is in contrast only about a \nthousandth of a centimeter in diameter. The chromosome is packed in a series of\ncoils, called chromatin, in association with special proteins (histones), forming\na string of microscopic beads. It is a mixture of DNA and protein. In the G0/G1\nphase of the cell cycle, between mitosis and the onset of DNA replication, the\nmitotic chromosomes diffuse into the interphase nucleus. At this stage, a number\nof important processes related to chromosome function take place. For exam-\nple, DNA is made accessible for transcription and is duplicated, and repairs are\nmade of DNA strand breaks. By the time of the next mitosis, the chromosomes\nhave been duplicated. The complexity of these and other processes raises many\nquestions about the large-scale',
        ' 51. The double exponential distribution is\n\nf (x|θ ) = 1\n2\n\ne−|x−θ |,\n\n−∞ < x < ∞\n\nFor an i.i.d. sample of size n = 2m + 1, show that the mle of θ is the median\nof the sample. (The observation such that half of the rest of the observations are \n\n\x0c325\n\nChapter 8 Estimation of Parameters and Fitting of Probability Distributions\n\nsmaller and half are larger.) [Hint: The function g(x) = |x| is not differentiable.\nDraw a picture for a small value of n to try to understand what is going on.]', 
        ' Type\n\nCount\n\nStarchy green\nStarchy white\nSugary green\nSugary white\n\n1997\n906\n904\n32'
    ]
    
    concepts_for_q = []
    for question in questions:
        query_prompt = fill_prompt(
            Path("web_searches/prompts/extract_n2k.prompt"),
            prompt=question
        )

        answer = prompt_chatgpt(query_prompt)
        concepts_for_q.append(json.loads(answer))
        print(f"Generated concepts for the question={question}") 

    print(concepts_for_q)

    return [" ".join(concept_for_q) for concept_for_q in concepts_for_q]

#     for question in questions:
#         # unknowns_for_question = question_unknowns[question]

#         total_rel_sources = ""
#         total_rel_info = ""
#         for concepts in concepts_for_q:
#             rel_sources, rel_info = return_relevant_results(concepts)   

#             rel_sources_str = json.dumps(rel_sources)
#             total_rel_sources += "\n\n\n" + rel_sources_str
#             rel_info_str = json.dumps(rel_info)
#             total_rel_info = json.dumps(rel_info_str)

#         query_prompt = fill_prompt(
#             Path("./web_searches/prompts/answer_question.prompt"),
#             question=question,
#             # TODO: Remember to replace this
#             sources=total_rel_sources,
#             context=total_rel_info
#         )

#         print("Going to prompt GPT4 with the query prompt")
#         answer = prompt_chatgpt(query_prompt)
#         print(f"Got answer for {question}")
#         print(answer)
#         answers.append(answer)
#     return answers


# ans = get_answers([])

with open("MY_ANWERS.json", "w+") as f:
    json.dump(ans, f, indent=4)