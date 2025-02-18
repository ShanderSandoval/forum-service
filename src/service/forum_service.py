from model.forum_model import Forum, Comment
from beanie import Document
from typing import Optional, List
import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


async def create_forum(data: dict) -> Optional[Document]:
    try:
        forum = Forum(**data)
        return await forum.insert()
    except Exception as e:
        logger.error(f"Error creating forum: {e}")
        return None


async def get_forums() -> List[Document]:
    try:
        return await Forum.find_all().to_list()
    except Exception as e:
        logger.error(f"Error retrieving forums: {e}")
        return []


async def get_forum_by_id(forum_id: str) -> Optional[Document]:
    try:
        forum = await Forum.get(forum_id)
        return forum
    except Exception as e:
        logger.error(f"Error retrieving forum with ID {forum_id}: {e}")
        return None


async def get_forums_by_project_element_id(project_element_id: str) -> List[Document]:
    try:
        forums = await Forum.find(Forum.projectElementId == project_element_id).to_list()
        return forums
    except Exception as e:
        logger.error(f"Error retrieving forums for projectElementId {project_element_id}: {e}")
        return []


async def add_comment(forum_id: str, comment_data: dict) -> Optional[Document]:
    try:
        forum = await Forum.get(forum_id)
        if not forum:
            logger.warning(f"Forum with ID {forum_id} not found.")
            return None

        comment = Comment(**comment_data)
        forum.comments.append(comment)
        await forum.replace()
        return forum
    except Exception as e:
        logger.error(f"Error adding comment to forum {forum_id}: {e}")
        return None


async def update_forum_body(forum_id: str, new_body: str) -> Optional[Document]:
    try:
        forum = await Forum.get(forum_id)
        if not forum:
            logger.warning(f"Forum with ID {forum_id} not found.")
            return None

        forum.body = new_body
        await forum.replace()
        return forum
    except Exception as e:
        logger.error(f"Error updating forum {forum_id}: {e}")
        return None


async def delete_comment(forum_id: str, comment_index: int) -> Optional[Document]:
    try:
        forum = await Forum.get(forum_id)
        if not forum:
            logger.warning(f"Forum with ID {forum_id} not found.")
            return None

        if 0 <= comment_index < len(forum.comments):
            forum.comments.pop(comment_index)
            await forum.replace()
            return forum
        else:
            logger.warning(f"Comment index {comment_index} out of range in forum {forum_id}.")
            return None
    except Exception as e:
        logger.error(f"Error deleting comment in forum {forum_id}: {e}")
        return None


async def delete_forum(forum_id: str) -> bool:
    try:
        forum = await Forum.get(forum_id)
        if not forum:
            logger.warning(f"Forum with ID {forum_id} not found.")
            return False

        await forum.delete()
        return True
    except Exception as e:
        logger.error(f"Error deleting forum {forum_id}: {e}")
        return False
