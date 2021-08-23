source activate
export ENV=dev

uvicorn src:api --reload
