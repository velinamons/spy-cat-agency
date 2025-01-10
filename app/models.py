from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from app.database import Base


class Cat(Base):
    __tablename__ = "cat"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    years_of_experience = Column(Integer, nullable=False)
    breed = Column(String, nullable=False)
    salary = Column(Float, nullable=False)

    mission = relationship("Mission", back_populates="cat", uselist=False)


class Mission(Base):
    __tablename__ = "mission"
    id = Column(Integer, primary_key=True, index=True)
    complete = Column(Boolean, default=False)
    cat_id = Column(Integer, ForeignKey("cat.id"), nullable=False)

    cat = relationship("Cat", back_populates="mission")

    targets = relationship("Target", back_populates="mission", cascade="all, delete-orphan")


class Target(Base):
    __tablename__ = "targets"
    id = Column(Integer, primary_key=True, index=True)
    mission_id = Column(Integer, ForeignKey("mission.id"), nullable=False)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    notes = Column(String, nullable=True)
    complete = Column(Boolean, default=False)

    mission = relationship("Mission", back_populates="targets")
