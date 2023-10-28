from dotenv import load_dotenv

load_dotenv()

import os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY, model_name='gpt-4')

"""Problem 1: Unsteady Potential Flow and Added Mass

a. Derive added mass around a sphere. Hint: if you print out the Added Mass Derivation handout, the math is all done for you, and you can hand that worksheet in. All you have to do is draw a picture on the page illustrating how to set up the integral (i.e. a picture of a sphere showing the coordinate system, F, \rho, dA, R, r, and \theta, and another picture showing how to calculate dA_i from dA.

b. In this derivation, are we integrating the static pressure or the dynamic pressure? What happens if we include the other pressure term as well?

c. The equation sheet says that the potential function for flow around a stationary sphere is \phi = -U \cos(\theta) \left( \frac{R^3}{r^2} \right), but the potential function given in the derivation is \phi = -U \cos(\theta) \left( \frac{R^3}{2r^2} \right). What is the difference between these two potential functions? What type of flow does this correspond to? Why would we not include that in the derivation? (Hint: think about the answer to part d.)

d. True or false, \phi = -U \cos(\theta) \left( \frac{R^3}{2r^2} \right) corresponds to flow around a moving sphere in quiescent fluid?

e. Derive added mass around a cylinder. Just draw a picture on the page illustrating how to set up the integral (i.e. a picture of a sphere showing the coordinate system, F, \rho, dA, R, r, and \theta, and another picture showing how to calculate dA_i from dA.

f. In this derivation, are we integrating the static pressure or the dynamic pressure? What happens if we include the other pressure term as well?

g. In class, we learned that the potential function for flow around a stationary cylinder is \phi = -U \cos(\theta) \left( \frac{R^2}{r} \right), but the potential function given in the derivation is \phi = -U \cos(\theta) \left( \frac{R^2}{r} \right). What is the difference between these two potential functions? What type of flow does this correspond to? Why would we not include that in the derivation? (Hint: think about the answer to part d.)

h. True or false, \phi = -U \cos(\theta) \left( \frac{R^2}{r} \right) corresponds to flow around a moving cylinder in quiescent fluid?

Problem 2: Pressure Distribution Around a Stationary Cylinder

a. The potential function for flow around a stationary cylinder is \phi = -U \cos(\theta) \left( \frac{R^2}{r} \right), where U is the free-stream velocity far away from the cylinder. Find the velocity field V(r,\theta) = \frac{\partial \phi}{\partial r} e_r + \frac{1}{r} \frac{\partial \phi}{\partial \theta} e_\theta.

b. Find the pressure at the surface of the cylinder, (r = R), using Bernoulli’s equation, making use of the fact that the pressure at the stagnation points (where V=0) is the stagnation pressure, p_st.

c. Show that the coefficient of pressure, c_p = \frac{P - P_\infty}{0.5 \rho U^2}, can be expressed in the form c_p = 1 - \frac{V^2}{U^2}.

d. Plot the coefficient of pressure using Matlab or Excel for 0 < \theta < 2\pi.

Problem 3: Added Mass

Calculate the added mass coefficients m_33 and m_44 for a circular cylinder of radius R = 1cm and length L = 1m whose axis is along the 1 axis.

Problem 4: Added Mass

In lab, we discussed how added mass affects the natural frequency of a cylinder bobbing up and down under water.

a. Write the equation for the natural frequency for this underwater spring-mass system.

b. What do you expect to happen if the cylinder has a square cross section?

Problem 5: Buoyancy and Added Mass

A buoy consists of a large sphere of radius, a, under a circular cylinder of radius, r. The added mass of the cylinder is negligible compared to that of the sphere.

a. Write the equation of motion for heave. (Note: there is a force that increases linearly with depth.)

b. What is the buoy’s natural frequency in heave.

Problem 6: Buoyancy and Added Mass

An offshore platform has the configuration shown:

The diameter of the uprights is 10 m, and that of the pontoons is 10 m. The length of the pontoons is 100 m. The added mass of the uprights is negligible compared to that of the pontoons.

a. Write the equation of motion for heave.

b. What is the platform’s natural frequency in heave.
"""

QUESTIONS_ASSIGNMENT1 = [
    {
        "assignment_title": """
2.016 Homework #3
Prof. A. Techet; Fall 2005
Issued: September 27, 2005
Due: October 4, 2005 """,
        "assignment_content": "",
        "question_no": "1",
        "question_title": "Unsteady Potential Flow and Added Mass",
        "question_content": """
a. Derive added mass around a sphere. Hint: if you print out the Added Mass Derivation handout, the math is all done for you, and you can hand that worksheet in. All you have to do is draw a picture on the page illustrating how to set up the integral (i.e. a picture of a sphere showing the coordinate system, F, \rho, dA, R, r, and \theta, and another picture showing how to calculate dA_i from dA.

b. In this derivation, are we integrating the static pressure or the dynamic pressure? What happens if we include the other pressure term as well?

c. The equation sheet says that the potential function for flow around a stationary sphere is \phi = -U \cos(\theta) \left( \frac{R^3}{r^2} \right), but the potential function given in the derivation is \phi = -U \cos(\theta) \left( \frac{R^3}{2r^2} \right). What is the difference between these two potential functions? What type of flow does this correspond to? Why would we not include that in the derivation? (Hint: think about the answer to part d.)

d. True or false, \phi = -U \cos(\theta) \left( \frac{R^3}{2r^2} \right) corresponds to flow around a moving sphere in quiescent fluid?

e. Derive added mass around a cylinder. Just draw a picture on the page illustrating how to set up the integral (i.e. a picture of a sphere showing the coordinate system, F, \rho, dA, R, r, and \theta, and another picture showing how to calculate dA_i from dA.

f. In this derivation, are we integrating the static pressure or the dynamic pressure? What happens if we include the other pressure term as well?

g. In class, we learned that the potential function for flow around a stationary cylinder is \phi = -U \cos(\theta) \left( \frac{R^2}{r} \right), but the potential function given in the derivation is \phi = -U \cos(\theta) \left( \frac{R^2}{r} \right). What is the difference between these two potential functions? What type of flow does this correspond to? Why would we not include that in the derivation? (Hint: think about the answer to part d.)

h. True or false, \phi = -U \cos(\theta) \left( \frac{R^2}{r} \right) corresponds to flow around a moving cylinder in quiescent fluid?""",
    },
    {
        "assignment_title": """
2.016 Homework #3
Prof. A. Techet; Fall 2005
Issued: September 27, 2005
Due: October 4, 2005 """,
        "assignment_content": "",
        "question_no": "2",
        "question_title": "Pressure Distribution Around a Stationary Cylinder",
        "question_content": """
a. The potential function for flow around a stationary cylinder is \phi = -U \cos(\theta) \left( \frac{R^2}{r} \right), where U is the free-stream velocity far away from the cylinder. Find the velocity field V(r,\theta) = \frac{\partial \phi}{\partial r} e_r + \frac{1}{r} \frac{\partial \phi}{\partial \theta} e_\theta.

b. Find the pressure at the surface of the cylinder, (r = R), using Bernoulli’s equation, making use of the fact that the pressure at the stagnation points (where V=0) is the stagnation pressure, p_st.

c. Show that the coefficient of pressure, c_p = \frac{P - P_\infty}{0.5 \rho U^2}, can be expressed in the form c_p = 1 - \frac{V^2}{U^2}.

d. Plot the coefficient of pressure using Matlab or Excel for 0 < \theta < 2\pi.""",
    },
    {
        "assignment_title": """
2.016 Homework #3
Prof. A. Techet; Fall 2005
Issued: September 27, 2005
Due: October 4, 2005 """,
        "assignment_content": "",
        "question_no": "3",
        "question_title": "Added Mass",
        "question_content": """
Calculate the added mass coefficients m_33 and m_44 for a circular cylinder of radius R = 1cm and length L = 1m whose axis is along the 1 axis.""",
    },
    {
        "assignment_title": """
2.016 Homework #3
Prof. A. Techet; Fall 2005
Issued: September 27, 2005
Due: October 4, 2005 """,
        "assignment_content": "",
        "question_no": "4",
        "question_title": "Added Mass",
        "question_content": """
In lab, we discussed how added mass affects the natural frequency of a cylinder bobbing up and down under water.

a. Write the equation for the natural frequency for this underwater spring-mass system.

b. What do you expect to happen if the cylinder has a square cross section?""",
    },
    {
        "assignment_title": """
2.016 Homework #3
Prof. A. Techet; Fall 2005
Issued: September 27, 2005
Due: October 4, 2005 """,
        "assignment_content": "",
        "question_no": "5",
        "question_title": "Buoyancy and Added Mass",
        "question_content": """
A buoy consists of a large sphere of radius, a, under a circular cylinder of radius, r. The added mass of the cylinder is negligible compared to that of the sphere.

a. Write the equation of motion for heave. (Note: there is a force that increases linearly with depth.)

b. What is the buoy’s natural frequency in heave.""",
    },
    {
        "assignment_title": """
2.016 Homework #3
Prof. A. Techet; Fall 2005
Issued: September 27, 2005
Due: October 4, 2005 """,
        "assignment_content": "",
        "question_no": "6",
        "question_title": "Buoyancy and Added Mass",
        "question_content": """
An offshore platform has the configuration shown:

The diameter of the uprights is 10 m, and that of the pontoons is 10 m. The length of the pontoons is 100 m. The added mass of the uprights is negligible compared to that of the pontoons.

a. Write the equation of motion for heave.

b. What is the platform’s natural frequency in heave.""",
    },
]

QUESTIONS_ASSIGNMENT2 = [
    {
        "assignment_title": """
18.443 Problem Set 3 Spring 2015
Statistics for Applications
Due Date: 2/27/2015
prior to 3:00pm""",
        "assignment_content": "Problems from John A. Rice, Third Edition. [Chapter.Section.Problem]",
        "question_no": "1",
        "question_title": "Problem 8.10.21.",
        "question_content": """
Problem 8.10.21.""",
    },
    {
        "assignment_title": """
18.443 Problem Set 3 Spring 2015
Statistics for Applications
Due Date: 2/27/2015
prior to 3:00pm""",
        "assignment_content": "Problems from John A. Rice, Third Edition. [Chapter.Section.Problem]",
        "question_no": "2",
        "question_title": "Problem 8.10.45. A Random walk Model for Chromatin",
        "question_content": """
Problem 8.10.45. A Random walk Model for Chromatin
Only parts (a) through (g). See R script file “Rproject3.script4.Chromatin.r” in Rproject3. You can edit this file for your answers; turn in hard-copy of an html file compiled by creating a “notebook” from the script (press the button on the script window that looks like a notebook). Circle/highlight your answers on the hard-copy.""",
    },
    {
        "assignment_title": """
18.443 Problem Set 3 Spring 2015
Statistics for Applications
Due Date: 2/27/2015
prior to 3:00pm""",
        "assignment_content": "Problems from John A. Rice, Third Edition. [Chapter.Section.Problem]",
        "question_no": "3",
        "question_title": "Problem 8.10.51 Double Exponential (Laplace) Distribution",
        "question_content": """
Problem 8.10.51 Double Exponential (Laplace) Distribution""",
    },
    {
        "assignment_title": """
18.443 Problem Set 3 Spring 2015
Statistics for Applications
Due Date: 2/27/2015
prior to 3:00pm""",
        "assignment_content": "Problems from John A. Rice, Third Edition. [Chapter.Section.Problem]",
        "question_no": "4",
        "question_title": "Problem 8.10.58 Gene Frequencies of Haptoglobin Type",
        "question_content": """
Problem 8.10.58 Gene Frequencies of Haptoglobin Type
See R script file “Rproject3.script1.multinomial.simulation.r” in Rproject3. You can edit this file for your answers; turn in hard-copy of an html file compiled by creating a “notebook” from the script (press the button on the script window that looks like a notebook). Circle/highlight your answers on the hard-copy.""",
    },
]

QUESTIONS_ASSIGNMENT2_WITH_WIKI = [
    {
        "assignment_title": """
18.443 Problem Set 3 Spring 2015
Statistics for Applications
Due Date: 2/27/2015
prior to 3:00pm""",
        "assignment_content": "Problems from John A. Rice, Third Edition. [Chapter.Section.Problem]",
        "question_no": "1",
        "question_title": "Problem 8.10.21.",
        "question_content": """
Problem 8.10.21.""",
        "wiki": """
In the previous lecture, we learned about basic probability distributions.

a. Derive the mean and variance for a binomial distribution.

b. How do these values change when the distribution is skewed?"""
    },
    {
        "assignment_title": """
18.443 Problem Set 3 Spring 2015
Statistics for Applications
Due Date: 2/27/2015
prior to 3:00pm""",
        "assignment_content": "Problems from John A. Rice, Third Edition. [Chapter.Section.Problem]",
        "question_no": "2",
        "question_title": "Problem 8.10.45. A Random walk Model for Chromatin",
        "question_content": """
Problem 8.10.45. A Random walk Model for Chromatin
Only parts (a) through (g).""",
        "wiki": """
In a recent paper, the structure of Chromatin was explored using fractal models.

a. Explain the basics of a fractal model.

b. How could you apply this model to understand the structure of Chromatin?"""
    },
    {
        "assignment_title": """
18.443 Problem Set 3 Spring 2015
Statistics for Applications
Due Date: 2/27/2015
prior to 3:00pm""",
        "assignment_content": "Problems from John A. Rice, Third Edition. [Chapter.Section.Problem]",
        "question_no": "3",
        "question_title": "Problem 8.10.51 Double Exponential (Laplace) Distribution",
        "question_content": """
Problem 8.10.51 Double Exponential (Laplace) Distribution""",
        "wiki": """
During the class discussion on the Laplace distribution, the concept of kurtosis was introduced.

a. Define kurtosis in statistical terms.

b. How does the kurtosis of a Laplace distribution differ from that of a normal distribution?"""
    },
    {
        "assignment_title": """
18.443 Problem Set 3 Spring 2015
Statistics for Applications
Due Date: 2/27/2015
prior to 3:00pm""",
        "assignment_content": "Problems from John A. Rice, Third Edition. [Chapter.Section.Problem]",
        "question_no": "4",
        "question_title": "Problem 8.10.58 Gene Frequencies of Haptoglobin Type",
        "question_content": """
Problem 8.10.58 Gene Frequencies of Haptoglobin Type""",
        "wiki": """
In the context of gene frequencies, the Hardy-Weinberg principle often comes into play.

a. State the Hardy-Weinberg principle.

b. Describe a situation where the principle would not hold for the Haptoglobin gene frequencies."""
    },
]

from langchain.prompts import ChatPromptTemplate
from langchain.prompts import HumanMessagePromptTemplate
from langchain.schema.messages import SystemMessage

RAW_ASSIGNMENT_PARSER_TEMPLATE = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                "You have received an assignment from MIT OpenCourseware. Please parse the assignment and output the assignment title, assignment content, and each question no, question title, and question content in the following format."
            )
        ),
        HumanMessagePromptTemplate.from_template("""
Assignment:
{assignment}
                                                 
Instruction:
- Given the assignment above, output the assignment title, assignment content, and each question no, question title, and question content in the output schema below.
- The assignment title and assignment content should be the same for all questions.
- Output in JSON.

Output Schema: (JSON)
{{
  "questions": [
    {{
      "assignment_title": "<assignment title>",
      "assignment_content": "<assignment content>",
      "question_no": "<numeric question number>",
      "question_title": "<question title>",
      "question_content": "<question content>"                                                                                        
    }},
    ... (more questions, if any)                                                                                          
  ]                                                 
}}"""),
    ]
)

UNKNOWN_SOURCES_TEMPLATE = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                "You have received an assignment from MIT OpenCourseware. Please identify any unknown sources or references and output them in the specified format."
            )
        ),
        HumanMessagePromptTemplate.from_template("""
Question:
{assignment_title}:

{assignment_content}

Question {question_no}: {question_title}

{question_content}

Instruction:
- Given the question above, output any unknown sources or references in the output schema below.
- Do not include any common words as a source or reference.
- Do not include any newlines in the output.
- Output in JSON.

Output Schema: (JSON)
{{
  "sources": [
    "<source name | section name>",
    ... (more source name - section name pairs; if no specific sections have been mentioned for a source name, just include the source name; if multiple specific sections have been mentioned for a source name, list each section name | section name as separate item in the list)
  ]
}}

Example Schema: (JSON)
{{
  "sources": [
    "John Doe, Third Edition. | Problem 2.3.4",
    "John Doe, Third Edition. | Problem 7.3.5",
    "MIT Autonomous Car Research Paper by Lex Fridman"
  ]
}}"""),
    ]
)

answer_gen_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                "You have received a new assignment question from MIT OpenCourseware and supplemental Wikipedia information that may help you answer the question. Please analyze the data and provide the most accurate and well-explained answer."
            )
        ),
        HumanMessagePromptTemplate.from_template("""
Question:
{assignment_title}:

{assignment_content}

Question {question_no}: {question_title}

{question_content}

Supplementary Wiki Information:
{wiki}

Instruction:
- After carefully analyzing the assignment question from MIT OpenCourseware and the supplemental wiki information, output the most accurate answer to the question.
- Output in JSON.

Output Schema: (JSON)
{{
  "answers": [
    {{
      "section": "<subsection id or "N/A">",
      "question": "<given subsection question or given question>",
      "answer": "<your answer>"
    }},
    ... (more subsection questions if any)
  ]
}}

Example Schema No.1: (example of multiple subsections in the given question) (JSON)
{{
  "answers": [
    {{
      "section": "a",
      "question": "<given subsection question for subsection a>",
      "answer": "<your answer>"
    }},
    {{
      "section": "b",
      "question": "<given subsection question for subsection b>",
      "answer": "<your answer>"
    }},
    ... (more subsection questions)
  ]
}}

Example Schema No.2: (example of no subsections in the given question) (JSON)
{{
  "answers": [
    {{
      "section": "N/A",
      "question": "<given question>",
      "answer": "<your answer>"
    }},
  ]
}}"""),
    ]
)

"""### Output Answers for Pipeline"""

print("===== Examples and functions all loaded... =====")

import json
import os
from datetime import datetime

def read_text_file(file_path):
    """
    Read a text file and return its content as a multi-line string.

    Parameters:
        file_path (str): The path to the text file to read.

    Returns:
        str: The content of the file as a multi-line string.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "The specified file could not be found."
    except IOError:
        return "An error occurred while reading the file."
    except UnicodeDecodeError:
        return "The file could not be decoded."

# Function to save answers as JSON files
def save_answers_to_folder(answers, folder_name):
    folder_path = f'./{folder_name}'
    os.makedirs(folder_path, exist_ok=True)  # Create the folder

    for i, answer in enumerate(answers):
        try:
            answer_obj = json.loads(answer)
            with open(f'{folder_path}/{folder_name}_item{i+1}.json', 'w') as f:
                json.dump(answer_obj, f)
        except:
            print("Error storing output as JSON, moving onto next output...")

def run_unknown_source_agent_test():
    # Loop to generate answers and save them to JSON files for the first set of questions
    answers1 = []
    for i, question in enumerate(QUESTIONS_ASSIGNMENT2):
        answer = llm(UNKNOWN_SOURCES_TEMPLATE.format_messages(
            assignment_title=question["assignment_title"],
            assignment_content=question["assignment_content"],
            question_no=question["question_no"],
            question_title=question["question_title"],
            question_content=question["question_content"],
        ))
        print(f"===== Unknown source agent no.{i} ran... =====")
        answers1.append(answer.content)

    current_time1 = datetime.now().strftime("%Y%m%d%H%M%S")
    folder_name1 = f'unknown_sources_{current_time1}'
    save_answers_to_folder(answers1, folder_name1)

    print(f"===== Outputs for the first set have been stored as JSON files in folder {folder_name1}. =====")

def run_generate_answer_agent_test():
    # Loop to generate answers and save them to JSON files for the second set of questions
    answers2 = []
    for i, question in enumerate(QUESTIONS_ASSIGNMENT2_WITH_WIKI):
        answer = llm(answer_gen_template.format_messages(
          assignment_title=question["assignment_title"],
          assignment_content=question["assignment_content"],
          question_no=question["question_no"],
          question_title=question["question_title"],
          question_content=question["question_content"],
          wiki=question["wiki"]
        ))
        print(f"===== Generate answer agent no.{i} ran... =====")
        answers2.append(answer.content)

    current_time2 = datetime.now().strftime("%Y%m%d%H%M%S")
    folder_name2 = f'answers_{current_time2}'
    save_answers_to_folder(answers2, folder_name2)

    print(f"===== Outputs for the second set have been stored as JSON files in folder {folder_name2}. =====")

def run_unknown_source_agent(questions_assignment):
    # Loop to generate answers and save them to JSON files for the first set of questions
    answers1 = []
    for i, question in enumerate(questions_assignment):
        answer = llm(UNKNOWN_SOURCES_TEMPLATE.format_messages(
            assignment_title=question["assignment_title"],
            assignment_content=question["assignment_content"],
            question_no=question["question_no"],
            question_title=question["question_title"],
            question_content=question["question_content"],
        ))
        print(f"===== Unknown source agent no.{i} ran... =====")
        answers1.append(json.loads(answer.content))
    
    return answers1

def run_generate_answer_agent(questions_assignment_with_wiki):
    # Loop to generate answers and save them to JSON files for the second set of questions
    answers2 = []
    for i, question in enumerate(questions_assignment_with_wiki):
        answer = llm(answer_gen_template.format_messages(
          assignment_title=question["assignment_title"],
          assignment_content=question["assignment_content"],
          question_no=question["question_no"],
          question_title=question["question_title"],
          question_content=question["question_content"],
          wiki=question["wiki"]
        ))
        print(f"===== Generate answer agent no.{i} ran... =====")
        answers2.append(answer.content)

    return answers2

if __name__ == "__main__":
    # Read the content from a text file located at 'example.txt'
    file_content = read_text_file("extracted_assignment.txt")

    # Print the content
    print(file_content)
    # run_unknown_source_agent_test()
    # run_generate_answer_agent_test()
