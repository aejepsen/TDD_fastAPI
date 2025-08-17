run:
	@uvicorn store.main:app --reload

test:
	pytest -v
