import uvicorn  # type: ignore

if __name__ == "__main__":
    uvicorn.run(app="app.awsgi:app", host="0.0.0.0", port=8000, reload=True)
