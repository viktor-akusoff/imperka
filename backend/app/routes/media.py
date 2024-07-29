from fastapi import APIRouter, HTTPException, Response, UploadFile, Request, status, Depends
from app.models.pyobj import ObjectId
from app.models.auth import User
from app.core.security import get_current_user
from app.core.database import db
import gridfs
from fastapi.responses import JSONResponse


fs = gridfs.GridFS(db) 

router = APIRouter(prefix="/media", tags=["Media"])

@router.get("/{media_id}")
async def get_media(media_id: str):
    try:
        grid_out = fs.get(ObjectId(media_id))
        media_type = grid_out.content_type
        contents = grid_out.read()

        return Response(content=contents, media_type=media_type)

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Media not found: {str(e)}")


@router.post("/upload")
async def upload_media(request: Request, media: UploadFile, user: User = Depends(get_current_user)):
    try:
        contents = await media.read()
        _id = fs.put(contents, filename=media.filename, content_type=media.content_type)
        return JSONResponse({"media_id": str(_id)}) 
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")