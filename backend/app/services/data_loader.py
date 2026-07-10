from fastapi import APIRouter, UploadFile, File
import pandas as pd

from app.services.data_loader import save_upload

router = APIRouter()


@router.post("/api/upload")
async def upload(file: UploadFile = File(...)):
    contents = await file.read()

    dataset_id, file_path = save_upload(contents, file.filename)

    if file.filename.endswith(".csv"):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)

    return {
        "dataset_id": dataset_id,
        "filename": file.filename,
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": list(df.columns),
    }