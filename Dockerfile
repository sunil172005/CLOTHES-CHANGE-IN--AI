FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements_render.txt .
RUN pip install --no-cache-dir -r requirements_render.txt

COPY . .

# Expose the port that Gradio will run on
EXPOSE 10000

# Run the application
CMD ["python", "main.py"]