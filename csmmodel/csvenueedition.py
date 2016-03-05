import sqlalchemy
from csmmodel.base import Base
import csmmodel.cspublication


class CsVenueEdition(Base):
    __tablename__ = 'csvenueseditions'

    abbr = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    venue = sqlalchemy.Column(sqlalchemy.String,
                              sqlalchemy.ForeignKey('csvenues.abbr'))
    ordinal = sqlalchemy.Column(sqlalchemy.Integer)
    year = sqlalchemy.Column(sqlalchemy.Integer)
    publications = sqlalchemy.orm.relationship('CsPublication')

    def __init__(self, abbr, venue=venue, ordinal=ordinal, year=year):
        self.abbr = abbr
        self.venue = venue
        self.ordinal = ordinal
        self.year = year

    def __repr__(self):
        return "<Venue Edition (abbr='%s', edition='%s', year='%s')>" \
               % (self.abbr, self.ordinal, self.year)
