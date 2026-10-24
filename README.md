# Student Exam Performance Prediction

An end-to-end machine-learning project that predicts a student’s mathematics score
from demographic information, lunch type, test preparation, reading score, and
writing score. The trained model is served through a small Flask application.

Author: Jenison J
Email: jenison717@gmail.com

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000` in a browser and select **Predict**.

## Project structure

- `app.py` — Flask web application.
- `src/components` — data ingestion, preprocessing, and model training.
- `src/pipeline/predict_pipeline.py` — inference pipeline used by Flask.
- `artifacts` — the trained model and preprocessing object used for inference.
- `notebook` — exploratory analysis and model-development notebooks.

The training workflow can be run with `python -m src.components.data_ingestion`.
