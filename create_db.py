from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Float
from statistics import fmean
import os

Base = declarative_base()

class Record(Base):
    __tablename__ = "Record"

    id = Column(Integer, primary_key = True)
    first_name = Column(String(22), nullable = False)
    last_name = Column(String(22), nullable = False)

    general_appearance = Column(Integer, nullable = False)
    manner_of_speaking  = Column(Integer, nullable = False)
    physical_condition = Column(Integer, nullable = False)
    mental_alertness  = Column(Integer, nullable = False)
    self_confidence = Column(Integer, nullable = False)
    abilitity_to_present_ideas  = Column(Integer, nullable = False)
    communication_skills  = Column(Integer, nullable = False)
    student_performance_rating  = Column(Integer, nullable = False)
    mean_score = Column(Float, nullable = False)
    prediction = Column(String(22), nullable = False)

    def __init__(self, fn, ln, ga, mos, pc, ma, sc, atpi, cs, spr, pred):
        """ CONSTRUCTOR """

        self.first_name = fn
        self.last_name = ln

        self.general_appearance = ga
        self.manner_of_speaking  = mos
        self.physical_condition = pc
        self.mental_alertness  = ma
        self.self_confidence = sc
        self.abilitity_to_present_ideas  = atpi
        self.communication_skills  = cs
        self.student_performance_rating  = spr

        self.mean_score = fmean([ga,mos,pc,ma,sc,atpi,cs,spr])

        self.prediction = pred

    def __repr__(self):
        return (
            f"""
                _______________________________________________________________  
                   
                FIRST NAME = {self.first_name}
                LAST NAME = {self.last_name}

                    CATEGORY:                     SCORE:
                    1.) General Appearence ---------- {self.general_appearance}
                    2.) Manner of Speaking ---------- {self.manner_of_speaking}
                    3.) Physical Condition ---------- {self.physical_condition}
                    4.) Mental Alertness ------------ {self.mental_alertness}
                    5.) Self Confidence ------------- {self.self_confidence}
                    6.) Ability to Present Ideas ---- {self.abilitity_to_present_ideas}
                    7.) Communication Skills -------- {self.communication_skills}
                    8.) Student Performance Rating -- {self.student_performance_rating}

                    Mean Score ---------------------- {self.mean_score}
                    PREDICTION ---------------------- {self.prediction} 
                _______________________________________________________________  
            """
        )

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_string = 'sqlite:///' + os.path.join(BASE_DIR, 'records.db')

engine = create_engine(connection_string, echo = True)

Session = sessionmaker()
session = Session(bind = engine)

def create_all_table():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_all_table()

    


