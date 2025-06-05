from .base_command import BaseCommannd
from models.user import User
from errors.errors import InvalidCredentialsErrors
from utils.http import get_transactions_data



class GetTransactions(BaseCommannd):
    def __init__(self, user_id, account_id, link_id):
        self.user_id = user_id
        self.account_id = account_id
        self.link = link_id 

    def execute(self):
        user = User.query.filter_by(id=self.user_id).first()
        if not user:
            raise InvalidCredentialsErrors()

        transactions = get_transactions_data(self.account_id, self.link)['results']

        ingresos = sum(tx["amount"] for tx in transactions if tx["type"] == "INFLOW")
        egresos = sum(tx["amount"] for tx in transactions if tx["type"] == "OUTFLOW")
        kpi_balance = ingresos - egresos

        resumen = []
        for tx in transactions:
            resumen.append({
                "id": tx["id"],
                "tipo": tx["type"],
                "descripcion": tx["description"],
                "monto": tx["amount"],
                "fecha": tx["value_date"],
                "categoria": tx.get("category", "Sin categoría"),
                "estado": tx.get("status", ""),
                "comercio": tx.get("merchant", {}).get("name", "Desconocido"),
                "logo": tx.get("merchant", {}).get("logo", ""),
            })

        return {
            "ingresos": round(ingresos, 1),
            "egresos": round(egresos, 1),
            "kpi_balance": round(kpi_balance, 1),
            "transacciones": resumen
        }