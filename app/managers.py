import sqlite3

from app.models import Actors


class ActorsManager:
    def __init__(self):
        self._connection = sqlite3.connect("library_db.db3")
        self.table_name = "actors"

    def create(self, first_name_: str, last_name_: str):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?,?)",
            (first_name_, last_name_)
        )
        self._connection.commit()

    def all(self):
        actors_cursor = self._connection.execute(
            f"SELECT id, first_name, last_name FROM {self.table_name}"
        )
        return [Actors(*row) for row in actors_cursor]

    def update(self, id_to_update, new_first_name, new_last_name):
        self._connection.execute(
            f"UPDATE {self.table_name}"
            f"SET first_name = ?, last_name = ?"
            f"WHERE id = ?",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self):
        pass
