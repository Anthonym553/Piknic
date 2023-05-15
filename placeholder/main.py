if __name__ == "__main__":
    import uvicorn
    # Run the FastAPI server
    uvicorn.run("piknic.main_fastapi:app",
                host="0.0.0.0", port=9002, reload=True)
