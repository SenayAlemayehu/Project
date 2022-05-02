from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapper
from ..domain import model
from ..domain.model import Patient, Doctor, Order, Xray, Lab, PhysicalTheraphy

metadata = MetaData()
Base = declarative_base()

orders = Table(
    "orders",
    metadata,
    Column("order_number", Integer, primary_key=True, autoincrement=True),
    Column("medical_record_number", String(30), nullable=False),
    Column("patient_name", String(30), nullable=False),
    Column("doctor_name", String(30)),
    Column("need_xray", bool),
    Column("need_lab", bool),
    Column("need_physical_theraphy", bool),
    Column("order_notes", String(255)),
)

xrays = Table(
    "xrays",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("order_number", Integer, ForeignKey("orders.order_number")),
    Column("name", String(30)),
    Column("medical_record_number", String(30), nullable=False),
    Column("doctor_name", String(30)),
    Column("notes", String(255)),
)


def start_mappers():
    orders_mapper = mapper(model.Order, orders)
    xrays_mapper = mapper(model.Xray, xrays)
