import numpy as np
from sqlalchemy import Column, Date, Float, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Line(Base):
    # Tell SQLAlchemy what the table name is and if there"s any table-specific arguments it should know about
    __tablename__ = "stockdemo2"
    id = Column(Integer, primary_key=True, nullable=False)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    output = Column(Float)


if __name__ == "__main__":

    # Create the database
    engine = create_engine("sqlite:///database/local.db")
    Base.metadata.create_all(engine)

    # Create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    try:
        X_train = np.random.random((1000, 4))
        y_train = np.random.random((1000, 1))

        for idx, i in enumerate(zip(X_train, y_train)):
            record = Line(**{
                "id": idx,
                "open": i[0][0],
                "high": i[0][1],
                "low": i[0][2],
                "close": i[0][3],
                "output": i[1][0]
            })
            s.add(record)  # Add all the records

        s.commit()  # Attempt to commit all the records
    except Exception as e:
        print(e)
        s.rollback()  # Rollback the changes on error
    finally:
        s.close()  # Close the connection
