
from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import engine
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionResponse

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.post("/", response_model=TransactionResponse, status_code=201)
def create_transaction(data: TransactionCreate):
    with Session(engine) as session:
        transaction = Transaction(**data.model_dump())
        session.add(transaction)
        session.commit()
        session.refresh(transaction)
        return transaction


@router.get("/", response_model=list[TransactionResponse])
def list_transactions():
    with Session(engine) as session:
        return session.scalars(
            select(Transaction).order_by(Transaction.id.desc())
        ).all()


@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_transaction(transaction_id: int):
    with Session(engine) as session:
        transaction = session.get(Transaction, transaction_id)

        if transaction is None:
            raise HTTPException(status_code=404, detail="Transaction not found")

        return transaction
