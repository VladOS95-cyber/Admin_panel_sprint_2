import datetime
import uuid
from dataclasses import dataclass, field


@dataclass
class FilmWork:
    title: str
    description: str
    creation_date: datetime
    certificate: str
    file_path: str
    rating: float
    type: str
    created_at: datetime
    updated_at: datetime
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class Genre:
    name: str
    description: str
    created_at: datetime
    updated_at: datetime
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class GenreFilmWork:
    created_at: datetime
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    film_work_id: uuid.UUID = field(default_factory=uuid.uuid4)
    genre_id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class Person:
    full_name: str
    birth_date: str
    created_at: datetime
    updated_at: datetime
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class PersonFilmWork:
    role: str
    created_at: datetime
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    film_work_id: uuid.UUID = field(default_factory=uuid.uuid4)
    person_id: uuid.UUID = field(default_factory=uuid.uuid4)
