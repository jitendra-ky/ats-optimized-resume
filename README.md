# ATS-Optimized-Resume

**ATS-Optimized-Resume** is a Streamlit application named **CareerCraft** that utilizes the capabilities of the Google Gemini model to analyze resumes against specific job descriptions. This tool helps job seekers optimize their resumes for Applicant Tracking Systems (ATS) by identifying keyword matches and providing personalized recommendations to enhance compatibility with the desired job roles.


Check out this [YouTube video](https://youtu.be/-C5RDNQNT1c?si=ywv73oXUJiBLDbwv)!


## Features

- **ATS Optimization**: Evaluate the resume's alignment with job descriptions.
- **Resume Analysis**: Identify key strengths and weaknesses in the resume content.
- **Tailored Profile Enhancement**: Receive customized recommendations to improve your resume.
- **Skill Enhancement Guidance**: Suggestions for adding or highlighting skills relevant to the job.
- **Streamlined Application Process**: Simplified and user-friendly interface for quick results.
- **Personalized Recommendations**: Insights and tips to increase your chances of getting noticed.

## Demo

Check out the live demo of the app: [CareerCraft](https://career-craft.azurewebsites.net/)

## Installation

### Prerequisites

- Python 3.x
- A Google Gemini API key (available through Google Cloud Platform)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/zsquare12/ats-optimized-resume.git
   cd ats-optimized-resume
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**

   Ensure you have a `.env` file in the root directory containing your Google Gemini API key:

   ```env
   GOOGLE_API_KEY=your-google-api-key
   ```

5. **Run the application:**

   ```bash
   streamlit run app.py
   ```

   The app will open in your web browser. You can paste the job description and upload your resume in PDF format to analyze it.

## Usage

1. Launch the app using the instructions above.
2. Paste the job description in the provided text area.
3. Upload your resume as a PDF.
4. Click the "Submit" button.
5. View the analysis results, which include a match percentage, missing keywords, and a profile summary.

## Deployment

The app is deployed on Streamlit Cloud and is accessible at [CareerCraft](https://career-craft.streamlit.app/). If you want to deploy it on your own server or cloud platform, ensure that you configure the `GOOGLE_API_KEY` environment variable and follow the same setup instructions.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for new features, feel free to create a pull request or open an issue in the repository.

## Acknowledgments

This project was developed during an internship at [SmartBridge](https://www.linkedin.com/company/smartbridge/mycompany/verification/). Special thanks to the mentors and the team for their support and guidance. 
