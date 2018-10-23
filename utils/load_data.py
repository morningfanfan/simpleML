import numpy as np
from sqlalchemy import Column, Date, Float, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Line(Base):
    """
    a utility for adding random data to the database

    schema: 
    database (default: sqlite:///database/local.db)
    table name (default: stockdemo)
    row: id | open | high | low | close | output
    """
    __tablename__ = "stockdemo"
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
        X = np.random.random((1000, 4))
        y = np.random.random((1000, 1))

        for idx, i in enumerate(zip(X, y)):
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
