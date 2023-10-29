from fpdf import FPDF
import json
# import nltk

QUESTIONS_WITH_WIKI = [
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

ANSWERS = ['{\n  "answers": [\n    {\n      "section": "1",\n      "question": "For n ∈ N*, let Xn be a random variable such that P [ Xn = 1/n ] = 1 − 1/n^2 and P [Xn = n] = 1/n^2. Does Xn converge in probability? In L^2?",\n      "answer": "Xn converges in probability to 0. This is because for any ε > 0, P(|Xn - 0| > ε) = P(Xn = n) = 1/n^2, which goes to 0 as n goes to infinity. However, Xn does not converge in L^2. This is because E[Xn^2] = (1/n^2)*(1/n)^2 + (1/n^2)*n^2 = 1/n^2 + 1, which does not go to 0 as n goes to infinity."\n    },\n    {\n      "section": "2a",\n      "question": "Let (Xn)n∈N* be a sequence of i.i.d. Bernoulli random variables with  istribution of nX̄n?",\n      "answer": "The distribution of nX̄n is a binomial distribution with parameters n and p. This is because nX̄n is the sum of n i.i.d. Bernoulli random variables, each with parameter p."\n    },\n    {\n      "section": "2b",\n      "question": "Prove that X̄n converges to p in L^2?",\n      "answer": "By the law of large numbers, X̄n converges to p in probability. To show that X̄n also converges to p in L^2, we need to show that E[(X̄n - p)^2] goes to 0 as n goes to infinity. Since X̄n is the average of n i.i.d. Bernoulli random variables, Var(X̄n) = p(1-p)/n. Therefore, E[(X̄n - p)^2] = Var(X̄n) = p(1-p)/n, which goes to 0 as n goes to infinity."\n    },\n    {\n      "section": "3a",\n      "question": "For n ∈ N*, let Xn be a Poisson random variable with parameter 1/n. Prove that Xn → p almost surely.",\n      "answer": "This statement is incorrect. A Poisson random variable Xn with parameter 1/n converges to 0 almost surely, not p. This is because the expected value of Xn is 1/n, which goes to 0 as n goes to infinity."\n    },\n    {\n      "section": "3b",\n      "question": "Prove that nXn → 0 almost surely.",\n      "answer": "The expected value of nXn is n*(1/n) = 1, which does not go to 0 as n goes to infinity. Therefore, nXn does not converge to 0 almost surely."\n    }\n  ]\n}', '{\n  "answers": [\n    {\n      "section": "1",\n      "question": "If Xn → X a.s. and Yn → Y a.s., then Xn + Yn → X + Y a.s.",\n      "answer": "True. This is a property of almost sure convergence. If two sequences of random variables converge almost surely to their respective limits, then the sum of the sequences also converges almost surely to the sum of the limits."\n    },\n    {\n      "section": "2",\n      "question": "If Xn → X in probability and Yn → Y in probability, then Xn + Yn → X + Y in probability.",\n      "answer": "True. This is a property of convergence in probability. If two sequences of random variables converge in probability to their respective limits, then the sum of the sequences also converges in probability to the sum of the limits."\n    },\n    {\n      "section": "3",\n      "question": "If Xn(d) → X(d) and Yn(d) → Y(d), then Xn + Yn → X + Y in distribution.",\n      "answer": "False. Convergence in distribution does not generally preserve operations like addition. For example, consider Xn = Yn = 1/n with probability 1 and X = Y = 0. Then Xn and Yn converge to X and Y in distribution, but Xn + Yn = 2/n does not converge to X + Y = 0 in distribution."\n    },\n    {\n      "section": "4",\n      "question": "Consider a coin that shows Heads with some unknown probability p when it is tossed. After tossing this coin 100 times, Heads have shown up 43 times. The unknown parameter p is contained in the interval [.33, .53] with probability 95%.",\n      "answer": "False. The statement implies that there is a 95% probability that the true value of p lies within the interval [.33, .53]. However, the true value of p is a fixed but unknown quantity, and does not have a probability distribution. The interval [.33, .53] is a confidence interval for the estimate of p, which means that if we were to repeat the experiment many times, 95% of the calculated intervals would contain the true value of p."\n    }\n  ]\n}', '{\n  "answers": [\n    {\n      "section": "1",\n      "question": "Show that √n (X̄n − p) / √(p(1 − p)) converges in distribution to a standard Gaussian random variable Z.",\n      "answer": "This is a direct application of the Central Limit Theorem (CLT). The CLT states that the sum (or average) of a large number of independent and identically distributed random variables, each with finite mean and variance, will be approximately normally distributed. In this case, X1, . . . , Xn are i.i.d. Bernoulli random variables with mean p and variance p(1-p). Therefore, as n approaches infinity, the standardized sum (or average) √n (X̄n − p) / √(p(1 − p)) will converge in distribution to a standard Gaussian random variable Z."\n    },\n    {\n      "section": "2",\n      "question": "Prove that for all t > 0, P[|Z| ≤ t] = 2P[Z ≤ t] − 1.",\n      "answer": "This is due to the symmetry of the standard Gaussian distribution. Because Z is symmetric around 0, the probability that Z is less than or equal to t is the same as the probability that Z is greater than or equal to -t. Therefore, P[|Z| ≤ t] = P[Z ≤ t] + P[Z ≥ -t] = 2P[Z ≤ t] - 1."\n    },\n    {\n      "section": "3",\n      "question": "For t > 0, let It be the interval [ X̄n − t√p(1 − p)/√n , X̄n + t√p(1 − p)/√n ]. Using the previous questions, prove that P[It ⊃ p] → 2Φ(t) − 1, as n → ∞, where Φ is the cumulative distribution function of the standard Gaussian distribution.",\n      "answer": "From the previous questions, we know that √n (X̄n − p) / √(p(1 − p)) converges in distribution to Z and P[|Z| ≤ t] = 2P[Z ≤ t] − 1. Therefore, as n approaches infinity, the probability that p falls within the interval It is the same as the probability that |Z| ≤ t, which is 2Φ(t) − 1."\n    },\n    {\n      "section": "4",\n      "question": "In practice, we would like to be able to define an interval as small as possible, whose expression does not depend on the unknown value of p. Using the previous question, find the value of t such that the interval It contains p with probability going to 95% as n grows to infinity. Denote by t0 this value. Hint: The 97.5%-quantile of the standard Gaussian distribution is 1.96.",\n      "answer": "From the previous question, we know that P[It ⊃ p] → 2Φ(t) − 1. Setting this equal to 0.95 (the desired confidence level), we get 2Φ(t) − 1 = 0.95. Solving for Φ(t) gives Φ(t) = 0.975. Therefore, t0, the value of t that gives a 95% confidence level, is the 97.5%-quantile of the standard Gaussian distribution, which is 1.96."\n    }\n  ]\n}']
ANSWERS = [json.loads(answer) for answer in ANSWERS]

def do_ord(c):
    try:
        result = ord(c)
        if result >= 256:  # Skip characters that can't be represented in Latin-1
            return ''
    except TypeError:  # Skip characters that cause a TypeError when passed to ord()
        return ''
    return result

def generate_pdf(questions_with_wiki, answers):
    pdf = FPDF()
    pdf.add_page()

    title = questions_with_wiki[0]['assignment_title']

    title = title.encode('latin-1', 'replace').decode('latin-1')

    # Set font and add title
    pdf.set_font("Arial", 'B', 16)
    pdf.multi_cell(0, 10, title, 0, 1, 'C')  # 'C' for center alignment
    
    # Set font for content
    pdf.set_font("Arial", size=12)
    
    for answer_item in answers:
        for item in answer_item['answers']:
            section = item['section']
            question = item['question']
            answer = item['answer']

            question = question.encode('latin-1', 'replace').decode('latin-1')
            answer = answer.encode('latin-1', 'replace').decode('latin-1')
            
            # Display question
            pdf.set_fill_color(220, 220, 220)  # light gray background for questions
            pdf.multi_cell(0, 10, question, 0, 'L', 1)  # 'L' for left alignment, 1 for filling the cell with the fill color
            
            # Display answer
            pdf.multi_cell(0, 10, answer)
            pdf.ln(5)  # space between Q&A pairs
    
    pdf.output("answer.pdf")

generate_pdf(QUESTIONS_WITH_WIKI, ANSWERS)
