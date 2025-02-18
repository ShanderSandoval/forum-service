from fastapi import APIRouter, HTTPException, Body
from pydantic import ValidationError

from service import forum_service


class ForumController:
    router = APIRouter(prefix="/forumService", tags=["forum"])

    @staticmethod
    @router.post("/createForum")
    async def create_forum(forum_data: dict = Body(...)):
        try:
            forum = await forum_service.create_forum(forum_data)
            if not forum:
                raise HTTPException(status_code=500, detail="Error creating the forum.")
            return forum
        except ValidationError as ve:
            raise HTTPException(status_code=422, detail=ve.errors())
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    @router.get("/getForums")
    async def get_forums():
        try:
            forums = await forum_service.get_forums()
            return forums
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    @router.get("/getForum/{forum_id}")
    async def get_forum(forum_id: str):
        try:
            forum = await forum_service.get_forum_by_id(forum_id)
            if not forum:
                raise HTTPException(status_code=404, detail="Forum not found.")
            return forum
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    @router.get("/getForumsByProject/{project_element_id}")
    async def get_forums_by_project(project_element_id: str):
        try:
            forums = await forum_service.get_forums_by_project_element_id(project_element_id)
            if not forums:
                raise HTTPException(status_code=404, detail="No forums found for the given projectElementId.")
            return forums
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    @router.put("/updateForumBody/{forum_id}")
    async def update_forum_body(forum_id: str, new_body: str = Body(...)):
        try:
            updated_forum = await forum_service.update_forum_body(forum_id, new_body)
            if not updated_forum:
                raise HTTPException(status_code=404, detail="Forum not found or not updated.")
            return updated_forum
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    @router.post("/addComment/{forum_id}")
    async def add_comment(forum_id: str, comment_data: dict = Body(...)):
        try:
            updated_forum = await forum_service.add_comment(forum_id, comment_data)
            if not updated_forum:
                raise HTTPException(status_code=404, detail="Forum not found or comment not added.")
            return updated_forum
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    @router.delete("/deleteComment/{forum_id}/{comment_index}")
    async def delete_comment(forum_id: str, comment_index: int):
        try:
            updated_forum = await forum_service.delete_comment(forum_id, comment_index)
            if not updated_forum:
                raise HTTPException(status_code=404, detail="Forum not found or comment not deleted.")
            return updated_forum
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    @router.delete("/deleteForum/{forum_id}")
    async def delete_forum(forum_id: str):
        try:
            success = await forum_service.delete_forum(forum_id)
            if not success:
                raise HTTPException(status_code=404, detail="Forum not found or not deleted.")
            return {"message": "Forum successfully deleted."}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
