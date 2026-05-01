.PHONY: install test eval demo app health all

install:
	python -m pip install -r requirements.txt

test:
	pytest -q

eval:
	python scripts/evaluate_retrieval.py --output reports/retrieval_eval.json

demo:
	python scripts/generate_demo_outputs.py

app:
	python -m streamlit run app/streamlit_app.py

health:
	python scripts/project_health_check.py

all: test eval demo health
