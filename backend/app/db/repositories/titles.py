from turtle import title
from typing import List, Sequence

from app.db.queries.queries import queries
from app.db.repositories.base import BaseRepository


class TitlesRepository(BaseRepository):
    async def get_all_titles(self) -> List[str]:
        titles_row = await queries.get_all_titles(self.connection)
        return [title[0] for title in titles_row]

    async def create_titles_that_dont_exist(self, *, titles: Sequence[str]) -> None:
        await queries.create_new_titles(self.connection, [{"title": title} for tag in titles])