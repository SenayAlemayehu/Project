from __future__ import annotations
from ast import Num

from dataclasses import dataclass
from datetime import date, datetime

from requests import session


@dataclass(frozen=True)
class Patient:
    medical_record_number = str
    name = str
    date_of_birth = date


@dataclass(frozen=True)
class Doctor:
    id = str
    name = str
    speciality = str


@dataclass(frozen=True)
class Xray:
    id = int
    order_number = int
    name = str
    medical_record_number = str
    doctor_name = str
    notes = str


@dataclass(frozen=True)
class Lab:
    id = int
    order_number = int
    name = str
    medical_record_number = str
    doctor_name = str
    notes = str


@dataclass(frozen=True)
class PhysicalTheraphy:
    id = int
    order_number = int
    name = str
    medical_record_number = str
    doctor_name = str
    notes = str


class Order:
    def __init__(
        self,
        num: str,
        mrn: str,
        Pname: str,
        Dname: str,
        xray: bool,
        lab: bool,
        PT: bool,
        notes: str,
    ):
        self.order_number = num
        self.medical_record_number = mrn
        self.patient_name = Pname
        self.doctor_name = Dname
        self.need_xray = xray
        self.need_lab = lab
        self.need_physical_theraphy = PT
        self.order_notes = notes

    def schedule(self, entry: Xray):
        if self.need_xray == True:
            for orders in Order:
                xray_row = entry(
                    order_number=Xray.order_number,
                    patient_name=Xray.name,
                    medical_record_number=Xray.medical_record_number,
                    doctor_name=Xray.doctor_name,
                    order_notes=Xray.notes,
                )
                session.add(xray_row)
            session.commit()
