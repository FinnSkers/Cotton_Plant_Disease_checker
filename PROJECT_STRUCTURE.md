# Project structure and deployment instructions for contributors and maintainers

## Project Structure

- app.py — Streamlit web interface for model inference
- requirements.txt — Python dependencies for deployment
- .streamlit/config.toml — Streamlit configuration (port, theme, etc.)
- .gitignore — Ignore unnecessary files in git
- src/ — (Optional) Place for reusable Python modules
- model_1_03333330.h5 — Pre-trained model file
- *.ipynb — Jupyter Notebooks for training and experiments

## Deployment

### Local
1. Install requirements:
   ```powershell
   pip install -r requirements.txt
   ```
2. Run the app:
   ```powershell
   streamlit run app.py
   ```

### Online (Hugging Face Spaces or Streamlit Cloud)
- Push all files to your GitHub repo.
- Connect your repo to the platform and select `app.py` as the entry point.

## Notes
- Update `class_names` in `app.py` to match your actual model classes.
- Place new models or data in appropriate folders and update paths as needed.
