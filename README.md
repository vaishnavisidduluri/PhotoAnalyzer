 
 Basic Photo Analyzer

Basic Photo Analyzer is a Python-based tool that analyzes images for key quality metrics such as brightness, sharpness, contrast, and saturation. It provides suggestions to improve photo quality based on these analyses.

## Features

- Analyze uploaded images interactively via a Streamlit web interface.
- Calculates brightness, sharpness, contrast, and saturation using OpenCV.
- Provides actionable suggestions to improve image quality.
- User-friendly UI with options to select which metrics to analyze.

## Installation

1. Clone the repository:
   git clone https://github.com/vaishnavisidduluri/PhotoAnalyzer.git
   cd PhotoAnalyzer

2. Install dependencies:
   pip install -r requirements.txt

## Usage

Run the Streamlit app:
streamlit run app/main.py

Upload an image through the web interface to see the analysis results and suggestions.

## Project Structure

- `app/analysis.py`: Contains functions to analyze image metrics.
- `app/suggestions.py`: Generates suggestions based on analysis results.
- `app/main.py`: Streamlit app UI and integration of analysis and suggestions.
- `data/`: Folder to store sample images for testing (optional).
- `requirements.txt`: Python dependencies.

## Author

vaishnavisidduluri  
Email: vaishnavisidduluri@gmail.com
