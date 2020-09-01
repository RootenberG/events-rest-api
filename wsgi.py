#!/user/bin/env python
import click
from pathlib import Path
import openpyxl


from app import create_app, db, models


app = create_app()

# flask cli context setup
@app.shell_context_processor
def get_context() -> dict:
    """Objects exposed here will be automatically available from the shell."""
    return dict(app=app, db=db, models=models)


@app.cli.command()
def create_db() -> None:
    """Create the configured database."""
    db.create_all()


@app.cli.command()
def store_into_db() -> None:
    """Store data from csv into db"""

    xlsx_file = Path("pydev_test_task_data2.xlsx")
    wb_obj = openpyxl.load_workbook(xlsx_file)
    wsheet = wb_obj.active

    for row in wsheet.iter_rows(min_row=2):  # skip 1st row
        asin, brand, id, source, stars, timestamp = [cell.value for cell in row]
        record = models.Event(
            asin=asin,
            brand=brand,
            event_id=id,
            source=source,
            stars=stars,
            timestamp=timestamp,
        )
        db.session.add(record)
        db.session.commit()


@app.cli.command()
@click.confirmation_option(prompt="Drop all database tables?")
def drop_db() -> None:
    """Drop the current database."""
    db.drop_all()


if __name__ == "__main__":
    app.run()
