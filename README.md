# BCG GenAI Financial Chatbot Simulation

This project was completed as part of the BCG GenAI Job Simulation on Forage. It demonstrates how AI and data analytics can be used to extract insights from company filings and provide interactive financial analysis through a chatbot interface.

## Project Overview

The goal of this project was to develop an AI-powered financial chatbot capable of analyzing data from 10-K and 10-Q reports of publicly traded companies. The chatbot interprets and explains financial data using natural language, simulating a consulting use case for BCG’s GenAI team.

## Key Features

	•	Data Extraction: Pulled 10-K data directly from the SEC EDGAR database for multiple companies.
	•	Data Cleaning & Transformation: Processed and organized datasets using pandas for structured analysis.
	•	Financial Analysis: Applied metrics such as:
	•	Mean
	•	Year-over-Year (YoY) change
	•	Coefficient of Variation (CV)
	•	Interactive Chatbot: Built with Streamlit and Ollama, allowing users to query company insights conversationally.

## Learnings & Insights

	•	Enhanced understanding of financial data analysis and interpretation.
	•	Learned to use aggregate functions effectively for trend analysis.
	•	Strengthened skills in Python, data manipulation, and AI application development.
	•	Gained experience in integrating GenAI models into a real-world financial context.

## Tech Stack

	•	Python
	•	Pandas
	•	Streamlit
	•	Ollama (Local LLM)
	•	SEC EDGAR API

## Example Output

Users can ask questions like:

“What was Microsoft’s average revenue over the past three years?”
“Which company had the highest volatility in net income?”

The chatbot responds with computed insights based on the processed data.
