from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.pipeline.Stage3_modelEval import ModelEvalutionPipeline
from src.pipeline.Stage1_dataINg import DataIngestionPipeline
from src.pipeline.Stage2_data_tranformation import DataTransformationPipeline

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, url: str = None):
    result = None
    error = None
    if url:
        try:
            Data_Ingestion_Pipeline = DataIngestionPipeline()
            Data_Ingestion_Pipeline.initateDataINgestion(url=url)

            Data_Transformation_Pipeline = DataTransformationPipeline()
            Data_Transformation_Pipeline.initateDataTransformation()

            Data_Evalution_Pipeline = ModelEvalutionPipeline()
            result = Data_Evalution_Pipeline.initateModelEvalution()
        except Exception as e:
            error = str(e)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result,
        "error": error
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
