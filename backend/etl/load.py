from typing import Any

from sqlalchemy.dialects.postgresql import insert

from database.connection import SessionLocal


BATCH_SIZE = 5000


def bulk_load(
    model,
    records: list[dict[str, Any]],
):
    """
    Bulk inserts records into PostgreSQL using batched
    INSERT ... ON CONFLICT DO NOTHING.

    Extra API fields are automatically ignored.
    """

    if not records:
        return

    db = SessionLocal()

    try:

        model_columns = {
            column.name
            for column in model.__table__.columns
        }

        pk_columns = [
            column.name
            for column in model.__table__.primary_key.columns
        ]

        # Process records in batches
        for start in range(0, len(records), BATCH_SIZE):

            batch = records[start:start + BATCH_SIZE]

            cleaned_batch = [
                {
                    k: v
                    for k, v in row.items()
                    if k in model_columns
                }
                for row in batch
            ]

            stmt = insert(model).values(cleaned_batch)

            stmt = stmt.on_conflict_do_nothing(
                index_elements=pk_columns
            )

            db.execute(stmt)

        db.commit()

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()