import streamlit as st
from streamlit_extras import add_vertical_space as avs
import os
from dotenv import load_dotenv
import google.generativeai as genai
import PyPDF2
from PIL import Image

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(prompt):
    response = model.generate_content(prompt)
    return response.text

def input_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ''
    for page_num in range(len(reader.pages)) :
        page = reader. pages[page_num]
        text += str(page.extract_text)
    return text

def analyse_resume(resume_txt, job_description):
    prompt=f"""
    As an experienced ATS (Applicant Tracking System), proficient in the technical domain encompassing
    Software Engineering, Data Science, Data Analysis, Big Data Engineering, Web Developer, Mobile App
    Developer, Devops Engineer, Machine Learning Engineer, Cybersecurity Analyst, Cloud Solutions Architect,
    Database Administrator, Network Engineer, AI Engineer, Systems Analyst, Full Stack Developer, UI/UX
    Designer, IT Project Manager, and additional specialized areas, your objective is to meticulously assess
    resumes against provided job descriptions. In a fiercely competitive job market, your expertise is crucial
    in offering top-notch guidance for resume enhancement. Assign precise matching percentages based on the JD
    (Job Description) and meticulously identify any missing keywords with utmost accuracy.
    resume : {resume_txt}
    description: {job_description}

    I want the response in the following structure:
    The first line indicates the percentage match with the job description (JD).
    The second line presents a list of missing keywords.
    The third section provides a profile summary.
    Mention the title for all the three sections.
    while generating the response put some space to separate all the three sections.
    """
    return get_gemini_response(prompt)


# set page config
st.set_page_config(
    page_title="Resume ATS Tracker",
    page_icon="🧊",
    layout="wide",
)
st.title("🧊 CareerCraft")

avs.add_vertical_space(4)

# ATS tracking application
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("<h1 style='text-align: center;'>Embark on Your Career Adventure</h1>", unsafe_allow_html=True)
    jd = st.text_area("Paste the Job Description")
    uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")
    submit = st.button("Submit")

    if submit:
        if uploaded_file is not None:
            text = input_pdf_text(uploaded_file)
            response = analyse_resume(text, jd)
            st.subheader(response)
        else:
            st.error("Please upload the resume")

with col2:
    st.image('https://cdn.dribbble.com/userupload/12500996/file/original-b458fe398a6d7f4e9999ce66ec856ff9.gif', use_column_width=True)

avs.add_vertical_space(10)



# here is the introduction
col1, col2 = st.columns([3, 2])
with col1:
    st.header("Navigate the Job Market with Confidence!")
    st.markdown("""<p style='text-align: justify;'>
        Introducing CareerCraft, an ATS-Optimized Resume Analyzer your ultimate solution for optimizing
        job applications and accelerating career growth. Our innovative platform leverages advanced ATS
        technology to provide job seekers with valuable insights into their resumes' compatibility with
        job descriptions. From resume optimization and skill enhancement to career progression guidance,
        CareerCraft empowers users to stand out in today's competitive job market. Streamline your job
        application process, enhance your skills, and navigate your career path with confidence. Join
        CareerCraft today and unlock new opportunities for professional success!</p>""", 
        unsafe_allow_html=True
    )


with col2:
    img2 = Image.open("images/icon2.png")
    st.image(
        img2,
        use_column_width=True,
    )

avs.add_vertical_space(10)

# here are the offerings
col1, col2 = st.columns([3, 2])
with col1:
    st.header("Wind Energy Offerings")
    st.write('ATS Optimization')
    st.write('Resume Analysis')
    st.write('Tailored Profile Enhancement')
    st.write('Skill Enhancement Guidance')
    st.write('Streamlined Application Process')
    st.write('Personalized Recommendations')
with col2:
    img1 = Image.open("images/icon1.png")
    st.image(img1, use_column_width=True)



# FAQ section
faqs = """
Question: How does CareerCraft analyze resumes and job descriptions?
Answer: CareerCraft uses advanced algorithms to analyze resumes and job descriptions, identifying key keywords and assessing compatibility between the two.
Question: Can CareerCraft suggest improvements for my resume?
Answer: Yes, CareerCraft provides personalized recommendations to optimize your resume for specific job openings, including suggestions for missing keywords and alignment with desired job roles.
Question: Is CareerCraft suitable for both entry-level and experienced professionals?
Answer: Absolutely! CareerCraft caters to job seekers at all career stages, offering tailored insights and guidance to enhance their resume and advance their careers.
"""
que, ans = [], []
for line in faqs.split("\n"):
    if line.startswith("Question:"):
        que.append(line)
    elif line.startswith("Answer:"):
        ans.append(line)
col1, col2 = st.columns((2,3))
with col2:
    st.markdown("<h1 style='text-align: center;'>FAQs</h1>", unsafe_allow_html=True)
    for i in range(len(que)):
        st.write(f"{que[i]}")
        st.write(f'''{ans[i]}''')
        avs.add_vertical_space(3)

    


with col1:
    img3 = Image.open("images/icon3.png")
    st.image(img3, use_column_width=True)
    