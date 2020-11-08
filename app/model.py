from pydantic import AnyHttpUrl
from pydantic.dataclasses import dataclass
from typing import List, Optional, Union
from datetime import date, datetime


@dataclass
class HelpfulInformation:
    id: str
    name: str
    description: Optional[str] = None
    url: Optional[AnyHttpUrl] = None


@dataclass
class Location:
    id: str
    name: str
    description: Optional[str] = None
    info: Optional[HelpfulInformation] = None


@dataclass
class ActivityCategory:
    id: str
    name: str
    description: Optional[str] = None


@dataclass
class Activity:
    id: str
    name: str
    description: Optional[str] = None
    category: Optional[ActivityCategory]
    cost: Optional[float] = None
    currency: Optional[str] = None
    location: Optional[Location] = None
    info: Optional[HelpfulInformation] = None


@dataclass
class Visit:
    id: str
    name: str
    description: Optional[str] = None
    start: Optional[Union[date, datetime]] = None
    end: Optional[Union[date, datetime]] = None
    location: Optional[Location] = None
    activities: List[Activity] = []


@dataclass
class Roadmap:
    id: str
    name: str
    description: Optional[str] = None
    visits: List[Visit] = []


@dataclass
class Travel:
    id: str
    name: str
    description: Optional[str] = None
    roadmaps: List[Roadmap] = []
