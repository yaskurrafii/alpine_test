from fastapi import FastAPI, Depends, HTTPException
from .schema import Create, Response
from .db import create_db, get_session
from .service import extract
from sqlmodel import Session

app = FastAPI()

create_db()


@app.post("/payload", response_model=Response)
def create_item(payload: Create, session=Depends(get_session)):
    res = extract(session, payload)
    return Response(output=res.output)


@app.get("/payload/{id}", response_class=Response)
def read_item(id: int, session: Session = Depends(get_session)):
    payload = session.get(payload, id)
    if not payload:
        raise HTTPException(status_code=404, detail="Project is None")
    return Response(output=payload.output)
