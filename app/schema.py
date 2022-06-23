from typing import Optional

import strawberry
from fastapi_sqlalchemy import db
from sqlalchemy import text
from strawberry.scalars import JSON

from app.models import MemberModel


@strawberry.input
class Filters:
    custom_field: Optional[str] = None
    custom_value: Optional[int] = None


@strawberry.type
class Member:
    beatle_id: int
    name: str
    age: int
    custom_information: JSON

    @classmethod
    def marshal(cls, model: MemberModel) -> "Member":
        return Member(beatle_id=strawberry.ID(model.beatle_id),
                      name=model.name,
                      age=model.age,
                      custom_information=model.custom_information)


@strawberry.type
class Query:

    @strawberry.field(name="members")
    def resolve_members(self, custom_information_filter: Filters = None) -> list[Member]:
        if custom_information_filter:
            field = custom_information_filter.custom_field
            value = custom_information_filter.custom_value
            members = db.session \
                .query(MemberModel)\
                .filter(text(f"CAST(custom_information->'{field}' AS INTEGER) = {value}"))\
                .all()
        else:
            members = db.session.query(MemberModel).all()
        return [Member.marshal(m) for m in members]


schema = strawberry.Schema(Query)
