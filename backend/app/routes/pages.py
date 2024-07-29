import pymongo
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query

from app.core import security
from app.core.database import db
from app.models.auth import User
from app.models.pages import Page, PreviewPage, MenuPage


pages_collection = db['pages']

router = APIRouter(prefix="/pages", tags=["Pages"], redirect_slashes=False)

def get_page_by_slug(slug: str):
    page = pages_collection.find_one({"slug": slug})
    if not page:
        raise HTTPException(status_code=404, detail="Page not found")
    return page

def serialize_page(page: dict):
    page["_id"] = str(page["_id"])
    return page

@router.post("/", response_model=Page, status_code=status.HTTP_201_CREATED)
async def create_page(page: Page, current_user: User = Depends(security.get_current_user)):
    
    page_data = page.model_dump()
    try:
        page = get_page_by_slug(page_data['slug'])
    except HTTPException:
        page = None
    if page is not None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Choose another slug!"
        )
    result = pages_collection.insert_one(page_data)
    created_page = pages_collection.find_one({"_id": result.inserted_id})
    return serialize_page(created_page)


@router.get("", response_model=List[PreviewPage])
async def get_all_pages(hashtags: Optional[List[str]] = Query(None)):
    query = {}
    if hashtags:
        query["hashtags"] = {"$all": hashtags} 
    pages = list(pages_collection.find(query).sort([("order", pymongo.ASCENDING)]))
    return [PreviewPage(**serialize_page(page)) for page in pages]


@router.get("/menu", response_model=List[MenuPage])
async def get_menu_pages():
    query = {"is_in_menu": True}
    pages = list(pages_collection.find(query).sort([("order", pymongo.ASCENDING)]))
    return [MenuPage(**serialize_page(page)) for page in pages]


@router.get("/{slug}", response_model=Page)
async def get_page(slug: str):
    page = get_page_by_slug(slug)
    return serialize_page(page)


@router.put("/{slug}", response_model=Page)
async def update_page(slug: str, updated_page: Page, current_user: User = Depends(security.get_current_user)):
    existing_page = get_page_by_slug(slug) 
    updated_data = updated_page.model_dump(exclude_unset=True)  

    result = pages_collection.update_one({"_id": existing_page["_id"]}, {"$set": updated_data})
    if result.matched_count >= 1:
        updated_page = pages_collection.find_one({"_id": existing_page["_id"]})
        return serialize_page(updated_page)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Page not found or not updated")


@router.delete("/{slug}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_page(slug: str, current_user: User = Depends(security.get_current_user)):
    result = pages_collection.delete_one({"slug": slug})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Page not found")