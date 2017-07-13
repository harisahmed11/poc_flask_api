# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, SmallInteger, String, Unicode, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mssql.base import BIT
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Country(Base):
    __tablename__ = 'Countries'

    CountryID = Column(SmallInteger, primary_key=True)
    CountryNameAr = Column(Unicode(128))
    CountryNameEn = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CurrencyID = Column(ForeignKey('Currencies.CurrencyID'))
    RegionID = Column(ForeignKey('Regions.RegionID'))
    ArgaamID = Column(SmallInteger)
    CountryCode = Column(Unicode(5))
    DisplaySeqNo = Column(Integer)

    Currency = relationship('Currency')
    Region = relationship('Region')


class Currency(Base):
    __tablename__ = 'Currencies'

    CurrencyID = Column(SmallInteger, primary_key=True)
    CurrencyNameAr = Column(Unicode(64))
    CurrencyNameEn = Column(String(64, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    ArgaamID = Column(SmallInteger)


class Market(Base):
    __tablename__ = 'Markets'

    MarketID = Column(SmallInteger, primary_key=True)
    CountryID = Column(ForeignKey('Countries.CountryID'), nullable=False)
    CurrencyID = Column(SmallInteger, nullable=False)
    MarketNameAr = Column(Unicode(64), nullable=False)
    MarketNameEn = Column(String(64, 'SQL_Latin1_General_CP1_CI_AS'))
    GeneralIndexSymbol = Column(String(32, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    DisplaySeqNo = Column(SmallInteger, nullable=False)
    IsActive = Column(BIT, nullable=False)
    IsTrading = Column(BIT, nullable=False)
    DisplayInPP = Column(BIT, nullable=False)
    TickerChartID = Column(Integer)
    TickerChartGeneralIndexCompanyID = Column(Integer)
    ArgaamID = Column(SmallInteger)
    MarketStartTime = Column(DateTime)
    MarketEndTime = Column(DateTime)
    HasIntraday = Column(BIT, nullable=False, server_default=text("((0))"))

    Country = relationship('Country')


class Region(Base):
    __tablename__ = 'Regions'

    RegionID = Column(SmallInteger, primary_key=True)
    RegionNameAr = Column(Unicode(32))
    RegionNameEn = Column(String(32, 'SQL_Latin1_General_CP1_CI_AS'))
