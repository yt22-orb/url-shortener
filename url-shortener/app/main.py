from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .import models, schemas, db

app = FastAPI()
models.Base.metadata.create_all(bind=db.engine)

@app.post("/shorten")
def shorten_url(url: schemas.URLCreate, session: Session = Depends(db.get_db)):
    short = models.URL(original=url.original)
    session.add(short)
    session.commit()
    session.refresh(short)
    return {"short_id": short.id}
@app.get("/{short_id}")
def redirect_url(short_id: int, session: Session = Depends(db.get_db)):
    url = session.query(models.URL).filter(models.URL.id == short_id).first()
    return {"original_url": url.original}
