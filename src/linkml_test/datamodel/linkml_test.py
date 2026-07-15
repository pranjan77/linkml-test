# Auto generated from linkml_test.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-07-15T11:44:05
# Schema: miappe-gold
#
# id: https://w3id.org/ornl/miappe-gold
# description: Cleaned, conformed, one-class-per-table model of a MIAPPE 1.2 plant phenotyping dataset: Populus trichocarpa observed at ORNL between 2024-03-26 and 2024-05-09. Facts are de-duplicated and carry deterministic md5 surrogate keys, so a reload reproduces identical identifiers.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Date, Datetime, Double, Integer, String
from linkml_runtime.utils.metamodelcore import XSDDate, XSDDateTime

metamodel_version = "1.11.0"
version = None

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MIAPPE_GOLD = CurieNamespace('miappe_gold', 'https://w3id.org/ornl/miappe-gold/')
DEFAULT_ = MIAPPE_GOLD


# Types

# Class references
class InvestigationInvestigationId(extended_str):
    pass


class StudyStudyId(extended_str):
    pass


class PersonPersonId(extended_str):
    pass


class EventEventId(extended_str):
    pass


class BiologicalMaterialBiologicalMaterialId(extended_str):
    pass


class ObservationUnitObsUnitId(extended_int):
    pass


class SampleSampleId(extended_str):
    pass


class ObservedVariableVariableId(extended_str):
    pass


class ObservationObservationId(extended_str):
    pass


class ImageImageId(extended_str):
    pass


@dataclass(repr=False)
class GoldLayer(YAMLRoot):
    """
    Container holding one collection per Parquet file.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_GOLD["GoldLayer"]
    class_class_curie: ClassVar[str] = "miappe_gold:GoldLayer"
    class_name: ClassVar[str] = "GoldLayer"
    class_model_uri: ClassVar[URIRef] = MIAPPE_GOLD.GoldLayer

    investigations: Optional[Union[dict[Union[str, InvestigationInvestigationId], Union[dict, "Investigation"]], list[Union[dict, "Investigation"]]]] = empty_dict()
    studies: Optional[Union[dict[Union[str, StudyStudyId], Union[dict, "Study"]], list[Union[dict, "Study"]]]] = empty_dict()
    persons: Optional[Union[dict[Union[str, PersonPersonId], Union[dict, "Person"]], list[Union[dict, "Person"]]]] = empty_dict()
    environments: Optional[Union[Union[dict, "Environment"], list[Union[dict, "Environment"]]]] = empty_list()
    dataFiles: Optional[Union[Union[dict, "DataFile"], list[Union[dict, "DataFile"]]]] = empty_list()
    events: Optional[Union[dict[Union[str, EventEventId], Union[dict, "Event"]], list[Union[dict, "Event"]]]] = empty_dict()
    biologicalMaterials: Optional[Union[dict[Union[str, BiologicalMaterialBiologicalMaterialId], Union[dict, "BiologicalMaterial"]], list[Union[dict, "BiologicalMaterial"]]]] = empty_dict()
    observationUnits: Optional[Union[dict[Union[int, ObservationUnitObsUnitId], Union[dict, "ObservationUnit"]], list[Union[dict, "ObservationUnit"]]]] = empty_dict()
    samples: Optional[Union[dict[Union[str, SampleSampleId], Union[dict, "Sample"]], list[Union[dict, "Sample"]]]] = empty_dict()
    observedVariables: Optional[Union[dict[Union[str, ObservedVariableVariableId], Union[dict, "ObservedVariable"]], list[Union[dict, "ObservedVariable"]]]] = empty_dict()
    observations: Optional[Union[dict[Union[str, ObservationObservationId], Union[dict, "Observation"]], list[Union[dict, "Observation"]]]] = empty_dict()
    images: Optional[Union[dict[Union[str, ImageImageId], Union[dict, "Image"]], list[Union[dict, "Image"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="investigations", slot_type=Investigation, key_name="investigationId", keyed=True)

        self._normalize_inlined_as_list(slot_name="studies", slot_type=Study, key_name="studyId", keyed=True)

        self._normalize_inlined_as_list(slot_name="persons", slot_type=Person, key_name="personId", keyed=True)

        self._normalize_inlined_as_list(slot_name="environments", slot_type=Environment, key_name="envParam", keyed=False)

        self._normalize_inlined_as_list(slot_name="dataFiles", slot_type=DataFile, key_name="dataFileLink", keyed=False)

        self._normalize_inlined_as_list(slot_name="events", slot_type=Event, key_name="eventId", keyed=True)

        self._normalize_inlined_as_list(slot_name="biologicalMaterials", slot_type=BiologicalMaterial, key_name="biologicalMaterialId", keyed=True)

        self._normalize_inlined_as_list(slot_name="observationUnits", slot_type=ObservationUnit, key_name="obsUnitId", keyed=True)

        self._normalize_inlined_as_list(slot_name="samples", slot_type=Sample, key_name="sampleId", keyed=True)

        self._normalize_inlined_as_list(slot_name="observedVariables", slot_type=ObservedVariable, key_name="variableId", keyed=True)

        self._normalize_inlined_as_list(slot_name="observations", slot_type=Observation, key_name="observationId", keyed=True)

        self._normalize_inlined_as_list(slot_name="images", slot_type=Image, key_name="imageId", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Investigation(YAMLRoot):
    """
    Top-level research context. A single investigation groups one or more studies.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_GOLD["Investigation"]
    class_class_curie: ClassVar[str] = "miappe_gold:Investigation"
    class_name: ClassVar[str] = "Investigation"
    class_model_uri: ClassVar[URIRef] = MIAPPE_GOLD.Investigation

    investigationId: Union[str, InvestigationInvestigationId] = None
    investigationTitle: Optional[str] = None
    investigationDescription: Optional[str] = None
    submissionDate: Optional[Union[str, XSDDate]] = None
    publicReleaseDate: Optional[str] = None
    license: Optional[str] = None
    miappeVersion: Optional[float] = None
    associatedPublication: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.investigationId):
            self.MissingRequiredField("investigationId")
        if not isinstance(self.investigationId, InvestigationInvestigationId):
            self.investigationId = InvestigationInvestigationId(self.investigationId)

        if self.investigationTitle is not None and not isinstance(self.investigationTitle, str):
            self.investigationTitle = str(self.investigationTitle)

        if self.investigationDescription is not None and not isinstance(self.investigationDescription, str):
            self.investigationDescription = str(self.investigationDescription)

        if self.submissionDate is not None and not isinstance(self.submissionDate, XSDDate):
            self.submissionDate = XSDDate(self.submissionDate)

        if self.publicReleaseDate is not None and not isinstance(self.publicReleaseDate, str):
            self.publicReleaseDate = str(self.publicReleaseDate)

        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.miappeVersion is not None and not isinstance(self.miappeVersion, float):
            self.miappeVersion = float(self.miappeVersion)

        if self.associatedPublication is not None and not isinstance(self.associatedPublication, str):
            self.associatedPublication = str(self.associatedPublication)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Study(YAMLRoot):
    """
    One experiment at one site over one date range. Every other table reaches this.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_GOLD["Study"]
    class_class_curie: ClassVar[str] = "miappe_gold:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = MIAPPE_GOLD.Study

    studyId: Union[str, StudyStudyId] = None
    investigationId: Union[str, InvestigationInvestigationId] = None
    studyTitle: Optional[str] = None
    studyDescription: Optional[str] = None
    studyStartDate: Optional[Union[str, XSDDate]] = None
    studyEndDate: Optional[Union[str, XSDDate]] = None
    contactInst: Optional[str] = None
    locationCountry: Optional[str] = None
    siteName: Optional[str] = None
    locationLatitude: Optional[float] = None
    locationLongitude: Optional[float] = None
    locationAltitude: Optional[str] = None
    expeDesignDesc: Optional[str] = None
    expeDesignType: Optional[str] = None
    obsUnitLevelHierarchy: Optional[str] = None
    obsUnitDesc: Optional[str] = None
    growthFacilityDesc: Optional[str] = None
    growthFacilityType: Optional[str] = None
    culturalPractice: Optional[str] = None
    expeDesignMap: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.studyId):
            self.MissingRequiredField("studyId")
        if not isinstance(self.studyId, StudyStudyId):
            self.studyId = StudyStudyId(self.studyId)

        if self._is_empty(self.investigationId):
            self.MissingRequiredField("investigationId")
        if not isinstance(self.investigationId, InvestigationInvestigationId):
            self.investigationId = InvestigationInvestigationId(self.investigationId)

        if self.studyTitle is not None and not isinstance(self.studyTitle, str):
            self.studyTitle = str(self.studyTitle)

        if self.studyDescription is not None and not isinstance(self.studyDescription, str):
            self.studyDescription = str(self.studyDescription)

        if self.studyStartDate is not None and not isinstance(self.studyStartDate, XSDDate):
            self.studyStartDate = XSDDate(self.studyStartDate)

        if self.studyEndDate is not None and not isinstance(self.studyEndDate, XSDDate):
            self.studyEndDate = XSDDate(self.studyEndDate)

        if self.contactInst is not None and not isinstance(self.contactInst, str):
            self.contactInst = str(self.contactInst)

        if self.locationCountry is not None and not isinstance(self.locationCountry, str):
            self.locationCountry = str(self.locationCountry)

        if self.siteName is not None and not isinstance(self.siteName, str):
            self.siteName = str(self.siteName)

        if self.locationLatitude is not None and not isinstance(self.locationLatitude, float):
            self.locationLatitude = float(self.locationLatitude)

        if self.locationLongitude is not None and not isinstance(self.locationLongitude, float):
            self.locationLongitude = float(self.locationLongitude)

        if self.locationAltitude is not None and not isinstance(self.locationAltitude, str):
            self.locationAltitude = str(self.locationAltitude)

        if self.expeDesignDesc is not None and not isinstance(self.expeDesignDesc, str):
            self.expeDesignDesc = str(self.expeDesignDesc)

        if self.expeDesignType is not None and not isinstance(self.expeDesignType, str):
            self.expeDesignType = str(self.expeDesignType)

        if self.obsUnitLevelHierarchy is not None and not isinstance(self.obsUnitLevelHierarchy, str):
            self.obsUnitLevelHierarchy = str(self.obsUnitLevelHierarchy)

        if self.obsUnitDesc is not None and not isinstance(self.obsUnitDesc, str):
            self.obsUnitDesc = str(self.obsUnitDesc)

        if self.growthFacilityDesc is not None and not isinstance(self.growthFacilityDesc, str):
            self.growthFacilityDesc = str(self.growthFacilityDesc)

        if self.growthFacilityType is not None and not isinstance(self.growthFacilityType, str):
            self.growthFacilityType = str(self.growthFacilityType)

        if self.culturalPractice is not None and not isinstance(self.culturalPractice, str):
            self.culturalPractice = str(self.culturalPractice)

        if self.expeDesignMap is not None and not isinstance(self.expeDesignMap, str):
            self.expeDesignMap = str(self.expeDesignMap)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(YAMLRoot):
    """
    A contact on the study. personId is a surrogate: md5(studyId, personName, personEmail).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_GOLD["Person"]
    class_class_curie: ClassVar[str] = "miappe_gold:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = MIAPPE_GOLD.Person

    personId: Union[str, PersonPersonId] = None
    studyId: Union[str, StudyStudyId] = None
    personName: Optional[str] = None
    personEmail: Optional[str] = None
    personRole: Optional[str] = None
    personAffiliation: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.personId):
            self.MissingRequiredField("personId")
        if not isinstance(self.personId, PersonPersonId):
            self.personId = PersonPersonId(self.personId)

        if self._is_empty(self.studyId):
            self.MissingRequiredField("studyId")
        if not isinstance(self.studyId, StudyStudyId):
            self.studyId = StudyStudyId(self.studyId)

        if self.personName is not None and not isinstance(self.personName, str):
            self.personName = str(self.personName)

        if self.personEmail is not None and not isinstance(self.personEmail, str):
            self.personEmail = str(self.personEmail)

        if self.personRole is not None and not isinstance(self.personRole, str):
            self.personRole = str(self.personRole)

        if self.personAffiliation is not None and not isinstance(self.personAffiliation, str):
            self.personAffiliation = str(self.personAffiliation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Environment(YAMLRoot):
    """
    A study-wide environment parameter, stored as a name/value pair.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_GOLD["Environment"]
    class_class_curie: ClassVar[str] = "miappe_gold:Environment"
    class_name: ClassVar[str] = "Environment"
    class_model_uri: ClassVar[URIRef] = MIAPPE_GOLD.Environment

    studyId: Union[str, StudyStudyId] = None
    envParam: str = None
    envParamValue: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.studyId):
            self.MissingRequiredField("studyId")
        if not isinstance(self.studyId, StudyStudyId):
            self.studyId = StudyStudyId(self.studyId)

        if self._is_empty(self.envParam):
            self.MissingRequiredField("envParam")
        if not isinstance(self.envParam, str):
            self.envParam = str(self.envParam)

        if self.envParamValue is not None and not isinstance(self.envParamValue, str):
            self.envParamValue = str(self.envParamValue)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataFile(YAMLRoot):
    """
    A source file the study was loaded from.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_GOLD["DataFile"]
    class_class_curie: ClassVar[str] = "miappe_gold:DataFile"
    class_name: ClassVar[str] = "DataFile"
    class_model_uri: ClassVar[URIRef] = MIAPPE_GOLD.DataFile

    studyId: Union[str, StudyStudyId] = None
    dataFileLink: str = None
    dataFileDesc: Optional[str] = None
    dataFileVersion: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.studyId):
            self.MissingRequiredField("studyId")
        if not isinstance(self.studyId, StudyStudyId):
            self.studyId = StudyStudyId(self.studyId)

        if self._is_empty(self.dataFileLink):
            self.MissingRequiredField("dataFileLink")
        if not isinstance(self.dataFileLink, str):
            self.dataFileLink = str(self.dataFileLink)

        if self.dataFileDesc is not None and not isinstance(self.dataFileDesc, str):
            self.dataFileDesc = str(self.dataFileDesc)

        if self.dataFileVersion is not None and not isinstance(self.dataFileVersion, str):
            self.dataFileVersion = str(self.dataFileVersion)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Event(YAMLRoot):
    """
    A dated event applied to the study, e.g. a phenotyping session. eventId is a surrogate: md5(studyId, eventType,
    eventDate).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_GOLD["Event"]
    class_class_curie: ClassVar[str] = "miappe_gold:Event"
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = MIAPPE_GOLD.Event

    eventId: Union[str, EventEventId] = None
    studyId: Union[str, StudyStudyId] = None
    obsUnitId: Optional[int] = None
    eventType: Optional[str] = None
    eventAccNumber: Optional[str] = None
    eventDesc: Optional[str] = None
    eventDate: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.eventId):
            self.MissingRequiredField("eventId")
        if not isinstance(self.eventId, EventEventId):
            self.eventId = EventEventId(self.eventId)

        if self._is_empty(self.studyId):
            self.MissingRequiredField("studyId")
        if not isinstance(self.studyId, StudyStudyId):
            self.studyId = StudyStudyId(self.studyId)

        if self.obsUnitId is not None and not isinstance(self.obsUnitId, int):
            self.obsUnitId = int(self.obsUnitId)

        if self.eventType is not None and not isinstance(self.eventType, str):
            self.eventType = str(self.eventType)

        if self.eventAccNumber is not None and not isinstance(self.eventAccNumber, str):
            self.eventAccNumber = str(self.eventAccNumber)

        if self.eventDesc is not None and not isinstance(self.eventDesc, str):
            self.eventDesc = str(self.eventDesc)

        if self.eventDate is not None and not isinstance(self.eventDate, XSDDate):
            self.eventDate = XSDDate(self.eventDate)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalMaterial(YAMLRoot):
    """
    The genotype or accession an observation unit is grown from.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_GOLD["BiologicalMaterial"]
    class_class_curie: ClassVar[str] = "miappe_gold:BiologicalMaterial"
    class_name: ClassVar[str] = "BiologicalMaterial"
    class_model_uri: ClassVar[URIRef] = MIAPPE_GOLD.BiologicalMaterial

    biologicalMaterialId: Union[str, BiologicalMaterialBiologicalMaterialId] = None
    studyId: Union[str, StudyStudyId] = None
    biologicalMaterialExtId: Optional[str] = None
    organism: Optional[str] = None
    genus: Optional[str] = None
    species: Optional[str] = None
    infraspecificName: Optional[str] = None
    biologicalMaterialLatitude: Optional[float] = None
    biologicalMaterialLongitude: Optional[float] = None
    biologicalMaterialAltitude: Optional[str] = None
    biologicalMaterialCoordUncertainty: Optional[str] = None
    biologicalMaterialPreprocessing: Optional[str] = None
    materialSourceId: Optional[str] = None
    materialSourceDoi: Optional[str] = None
    materialSourceAccNumber: Optional[str] = None
    materialSourceAccName: Optional[str] = None
    materialSourceInstCode: Optional[str] = None
    materialSourceInstName: Optional[str] = None
    materialSourceOtherIds: Optional[str] = None
    materialSourceLatitude: Optional[str] = None
    materialSourceLongitude: Optional[str] = None
    materialSourceAltitude: Optional[str] = None
    materialSourceCoordUncertainty: Optional[str] = None
    materialSourceDesc: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.biologicalMaterialId):
            self.MissingRequiredField("biologicalMaterialId")
        if not isinstance(self.biologicalMaterialId, BiologicalMaterialBiologicalMaterialId):
            self.biologicalMaterialId = BiologicalMaterialBiologicalMaterialId(self.biologicalMaterialId)

        if self._is_empty(self.studyId):
            self.MissingRequiredField("studyId")
        if not isinstance(self.studyId, StudyStudyId):
            self.studyId = StudyStudyId(self.studyId)

        if self.biologicalMaterialExtId is not None and not isinstance(self.biologicalMaterialExtId, str):
            self.biologicalMaterialExtId = str(self.biologicalMaterialExtId)

        if self.organism is not None and not isinstance(self.organism, str):
            self.organism = str(self.organism)

        if self.genus is not None and not isinstance(self.genus, str):
            self.genus = str(self.genus)

        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

        if self.infraspecificName is not None and not isinstance(self.infraspecificName, str):
            self.infraspecificName = str(self.infraspecificName)

        if self.biologicalMaterialLatitude is not None and not isinstance(self.biologicalMaterialLatitude, float):
            self.biologicalMaterialLatitude = float(self.biologicalMaterialLatitude)

        if self.biologicalMaterialLongitude is not None and not isinstance(self.biologicalMaterialLongitude, float):
            self.biologicalMaterialLongitude = float(self.biologicalMaterialLongitude)

        if self.biologicalMaterialAltitude is not None and not isinstance(self.biologicalMaterialAltitude, str):
            self.biologicalMaterialAltitude = str(self.biologicalMaterialAltitude)

        if self.biologicalMaterialCoordUncertainty is not None and not isinstance(self.biologicalMaterialCoordUncertainty, str):
            self.biologicalMaterialCoordUncertainty = str(self.biologicalMaterialCoordUncertainty)

        if self.biologicalMaterialPreprocessing is not None and not isinstance(self.biologicalMaterialPreprocessing, str):
            self.biologicalMaterialPreprocessing = str(self.biologicalMaterialPreprocessing)

        if self.materialSourceId is not None and not isinstance(self.materialSourceId, str):
            self.materialSourceId = str(self.materialSourceId)

        if self.materialSourceDoi is not None and not isinstance(self.materialSourceDoi, str):
            self.materialSourceDoi = str(self.materialSourceDoi)

        if self.materialSourceAccNumber is not None and not isinstance(self.materialSourceAccNumber, str):
            self.materialSourceAccNumber = str(self.materialSourceAccNumber)

        if self.materialSourceAccName is not None and not isinstance(self.materialSourceAccName, str):
            self.materialSourceAccName = str(self.materialSourceAccName)

        if self.materialSourceInstCode is not None and not isinstance(self.materialSourceInstCode, str):
            self.materialSourceInstCode = str(self.materialSourceInstCode)

        if self.materialSourceInstName is not None and not isinstance(self.materialSourceInstName, str):
            self.materialSourceInstName = str(self.materialSourceInstName)

        if self.materialSourceOtherIds is not None and not isinstance(self.materialSourceOtherIds, str):
            self.materialSourceOtherIds = str(self.materialSourceOtherIds)

        if self.materialSourceLatitude is not None and not isinstance(self.materialSourceLatitude, str):
            self.materialSourceLatitude = str(self.materialSourceLatitude)

        if self.materialSourceLongitude is not None and not isinstance(self.materialSourceLongitude, str):
            self.materialSourceLongitude = str(self.materialSourceLongitude)

        if self.materialSourceAltitude is not None and not isinstance(self.materialSourceAltitude, str):
            self.materialSourceAltitude = str(self.materialSourceAltitude)

        if self.materialSourceCoordUncertainty is not None and not isinstance(self.materialSourceCoordUncertainty, str):
            self.materialSourceCoordUncertainty = str(self.materialSourceCoordUncertainty)

        if self.materialSourceDesc is not None and not isinstance(self.materialSourceDesc, str):
            self.materialSourceDesc = str(self.materialSourceDesc)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObservationUnit(YAMLRoot):
    """
    The thing observed - here an individual plant. The grain every fact resolves to.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_GOLD["ObservationUnit"]
    class_class_curie: ClassVar[str] = "miappe_gold:ObservationUnit"
    class_name: ClassVar[str] = "ObservationUnit"
    class_model_uri: ClassVar[URIRef] = MIAPPE_GOLD.ObservationUnit

    obsUnitId: Union[int, ObservationUnitObsUnitId] = None
    studyId: Union[str, StudyStudyId] = None
    biologicalMaterialId: Union[str, BiologicalMaterialBiologicalMaterialId] = None
    obsUnitType: Optional[str] = None
    externalId: Optional[int] = None
    spatialDistribution: Optional[str] = None
    obsUnitFactorValue: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.obsUnitId):
            self.MissingRequiredField("obsUnitId")
        if not isinstance(self.obsUnitId, ObservationUnitObsUnitId):
            self.obsUnitId = ObservationUnitObsUnitId(self.obsUnitId)

        if self._is_empty(self.studyId):
            self.MissingRequiredField("studyId")
        if not isinstance(self.studyId, StudyStudyId):
            self.studyId = StudyStudyId(self.studyId)

        if self._is_empty(self.biologicalMaterialId):
            self.MissingRequiredField("biologicalMaterialId")
        if not isinstance(self.biologicalMaterialId, BiologicalMaterialBiologicalMaterialId):
            self.biologicalMaterialId = BiologicalMaterialBiologicalMaterialId(self.biologicalMaterialId)

        if self.obsUnitType is not None and not isinstance(self.obsUnitType, str):
            self.obsUnitType = str(self.obsUnitType)

        if self.externalId is not None and not isinstance(self.externalId, int):
            self.externalId = int(self.externalId)

        if self.spatialDistribution is not None and not isinstance(self.spatialDistribution, str):
            self.spatialDistribution = str(self.spatialDistribution)

        if self.obsUnitFactorValue is not None and not isinstance(self.obsUnitFactorValue, str):
            self.obsUnitFactorValue = str(self.obsUnitFactorValue)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sample(YAMLRoot):
    """
    Tissue taken from an observation unit on a date (leaf, stem, whole plant).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_GOLD["Sample"]
    class_class_curie: ClassVar[str] = "miappe_gold:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = MIAPPE_GOLD.Sample

    sampleId: Union[str, SampleSampleId] = None
    obsUnitId: Union[int, ObservationUnitObsUnitId] = None
    developmentStage: Optional[str] = None
    anatomicalEntity: Optional[str] = None
    sampleDesc: Optional[str] = None
    collectionDate: Optional[str] = None
    externalId: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.sampleId):
            self.MissingRequiredField("sampleId")
        if not isinstance(self.sampleId, SampleSampleId):
            self.sampleId = SampleSampleId(self.sampleId)

        if self._is_empty(self.obsUnitId):
            self.MissingRequiredField("obsUnitId")
        if not isinstance(self.obsUnitId, ObservationUnitObsUnitId):
            self.obsUnitId = ObservationUnitObsUnitId(self.obsUnitId)

        if self.developmentStage is not None and not isinstance(self.developmentStage, str):
            self.developmentStage = str(self.developmentStage)

        if self.anatomicalEntity is not None and not isinstance(self.anatomicalEntity, str):
            self.anatomicalEntity = str(self.anatomicalEntity)

        if self.sampleDesc is not None and not isinstance(self.sampleDesc, str):
            self.sampleDesc = str(self.sampleDesc)

        if self.collectionDate is not None and not isinstance(self.collectionDate, str):
            self.collectionDate = str(self.collectionDate)

        if self.externalId is not None and not isinstance(self.externalId, str):
            self.externalId = str(self.externalId)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObservedVariable(YAMLRoot):
    """
    A measured variable: trait + method + scale. Joined by every observation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_GOLD["ObservedVariable"]
    class_class_curie: ClassVar[str] = "miappe_gold:ObservedVariable"
    class_name: ClassVar[str] = "ObservedVariable"
    class_model_uri: ClassVar[URIRef] = MIAPPE_GOLD.ObservedVariable

    variableId: Union[str, ObservedVariableVariableId] = None
    studyId: Union[str, StudyStudyId] = None
    variableName: Optional[str] = None
    variableAccNumber: Optional[str] = None
    traitName: Optional[str] = None
    traitEntity: Optional[str] = None
    traitEntityAccessionNumber: Optional[str] = None
    traitCharacteristic: Optional[str] = None
    traitCharacteristicAccessionNumber: Optional[str] = None
    traitAccNumber: Optional[str] = None
    methodName: Optional[str] = None
    methodAccNumber: Optional[str] = None
    methodDesc: Optional[str] = None
    methodRef: Optional[str] = None
    scaleName: Optional[str] = None
    scaleAccNumber: Optional[str] = None
    timeScale: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.variableId):
            self.MissingRequiredField("variableId")
        if not isinstance(self.variableId, ObservedVariableVariableId):
            self.variableId = ObservedVariableVariableId(self.variableId)

        if self._is_empty(self.studyId):
            self.MissingRequiredField("studyId")
        if not isinstance(self.studyId, StudyStudyId):
            self.studyId = StudyStudyId(self.studyId)

        if self.variableName is not None and not isinstance(self.variableName, str):
            self.variableName = str(self.variableName)

        if self.variableAccNumber is not None and not isinstance(self.variableAccNumber, str):
            self.variableAccNumber = str(self.variableAccNumber)

        if self.traitName is not None and not isinstance(self.traitName, str):
            self.traitName = str(self.traitName)

        if self.traitEntity is not None and not isinstance(self.traitEntity, str):
            self.traitEntity = str(self.traitEntity)

        if self.traitEntityAccessionNumber is not None and not isinstance(self.traitEntityAccessionNumber, str):
            self.traitEntityAccessionNumber = str(self.traitEntityAccessionNumber)

        if self.traitCharacteristic is not None and not isinstance(self.traitCharacteristic, str):
            self.traitCharacteristic = str(self.traitCharacteristic)

        if self.traitCharacteristicAccessionNumber is not None and not isinstance(self.traitCharacteristicAccessionNumber, str):
            self.traitCharacteristicAccessionNumber = str(self.traitCharacteristicAccessionNumber)

        if self.traitAccNumber is not None and not isinstance(self.traitAccNumber, str):
            self.traitAccNumber = str(self.traitAccNumber)

        if self.methodName is not None and not isinstance(self.methodName, str):
            self.methodName = str(self.methodName)

        if self.methodAccNumber is not None and not isinstance(self.methodAccNumber, str):
            self.methodAccNumber = str(self.methodAccNumber)

        if self.methodDesc is not None and not isinstance(self.methodDesc, str):
            self.methodDesc = str(self.methodDesc)

        if self.methodRef is not None and not isinstance(self.methodRef, str):
            self.methodRef = str(self.methodRef)

        if self.scaleName is not None and not isinstance(self.scaleName, str):
            self.scaleName = str(self.scaleName)

        if self.scaleAccNumber is not None and not isinstance(self.scaleAccNumber, str):
            self.scaleAccNumber = str(self.scaleAccNumber)

        if self.timeScale is not None and not isinstance(self.timeScale, str):
            self.timeScale = str(self.timeScale)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Observation(YAMLRoot):
    """
    A single measured value. observationId is a surrogate: md5(obsUnitId, variableId, observationTimestamp).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_GOLD["Observation"]
    class_class_curie: ClassVar[str] = "miappe_gold:Observation"
    class_name: ClassVar[str] = "Observation"
    class_model_uri: ClassVar[URIRef] = MIAPPE_GOLD.Observation

    observationId: Union[str, ObservationObservationId] = None
    studyId: Union[str, StudyStudyId] = None
    obsUnitId: Union[int, ObservationUnitObsUnitId] = None
    variableId: Union[str, ObservedVariableVariableId] = None
    sampleId: Optional[Union[str, SampleSampleId]] = None
    observationTimestamp: Optional[Union[str, XSDDateTime]] = None
    observationValue: Optional[float] = None
    replicate: Optional[str] = None
    qualityFlag: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.observationId):
            self.MissingRequiredField("observationId")
        if not isinstance(self.observationId, ObservationObservationId):
            self.observationId = ObservationObservationId(self.observationId)

        if self._is_empty(self.studyId):
            self.MissingRequiredField("studyId")
        if not isinstance(self.studyId, StudyStudyId):
            self.studyId = StudyStudyId(self.studyId)

        if self._is_empty(self.obsUnitId):
            self.MissingRequiredField("obsUnitId")
        if not isinstance(self.obsUnitId, ObservationUnitObsUnitId):
            self.obsUnitId = ObservationUnitObsUnitId(self.obsUnitId)

        if self._is_empty(self.variableId):
            self.MissingRequiredField("variableId")
        if not isinstance(self.variableId, ObservedVariableVariableId):
            self.variableId = ObservedVariableVariableId(self.variableId)

        if self.sampleId is not None and not isinstance(self.sampleId, SampleSampleId):
            self.sampleId = SampleSampleId(self.sampleId)

        if self.observationTimestamp is not None and not isinstance(self.observationTimestamp, XSDDateTime):
            self.observationTimestamp = XSDDateTime(self.observationTimestamp)

        if self.observationValue is not None and not isinstance(self.observationValue, float):
            self.observationValue = float(self.observationValue)

        if self.replicate is not None and not isinstance(self.replicate, str):
            self.replicate = str(self.replicate)

        if self.qualityFlag is not None and not isinstance(self.qualityFlag, str):
            self.qualityFlag = str(self.qualityFlag)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Image(YAMLRoot):
    """
    One image-pipeline artifact: a raw frame, mask, header or analysis output. imageId is a surrogate: md5 of all
    business columns.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_GOLD["Image"]
    class_class_curie: ClassVar[str] = "miappe_gold:Image"
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = MIAPPE_GOLD.Image

    imageId: Union[str, ImageImageId] = None
    studyId: Union[str, StudyStudyId] = None
    obsUnitId: Union[int, ObservationUnitObsUnitId] = None
    sampleId: Optional[str] = None
    observationTimestamp: Optional[str] = None
    Modality: Optional[str] = None
    fileType: Optional[str] = None
    filePath: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.imageId):
            self.MissingRequiredField("imageId")
        if not isinstance(self.imageId, ImageImageId):
            self.imageId = ImageImageId(self.imageId)

        if self._is_empty(self.studyId):
            self.MissingRequiredField("studyId")
        if not isinstance(self.studyId, StudyStudyId):
            self.studyId = StudyStudyId(self.studyId)

        if self._is_empty(self.obsUnitId):
            self.MissingRequiredField("obsUnitId")
        if not isinstance(self.obsUnitId, ObservationUnitObsUnitId):
            self.obsUnitId = ObservationUnitObsUnitId(self.obsUnitId)

        if self.sampleId is not None and not isinstance(self.sampleId, str):
            self.sampleId = str(self.sampleId)

        if self.observationTimestamp is not None and not isinstance(self.observationTimestamp, str):
            self.observationTimestamp = str(self.observationTimestamp)

        if self.Modality is not None and not isinstance(self.Modality, str):
            self.Modality = str(self.Modality)

        if self.fileType is not None and not isinstance(self.fileType, str):
            self.fileType = str(self.fileType)

        if self.filePath is not None and not isinstance(self.filePath, str):
            self.filePath = str(self.filePath)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.goldLayer__investigations = Slot(uri=MIAPPE_GOLD.investigations, name="goldLayer__investigations", curie=MIAPPE_GOLD.curie('investigations'),
                   model_uri=MIAPPE_GOLD.goldLayer__investigations, domain=None, range=Optional[Union[dict[Union[str, InvestigationInvestigationId], Union[dict, Investigation]], list[Union[dict, Investigation]]]])

slots.goldLayer__studies = Slot(uri=MIAPPE_GOLD.studies, name="goldLayer__studies", curie=MIAPPE_GOLD.curie('studies'),
                   model_uri=MIAPPE_GOLD.goldLayer__studies, domain=None, range=Optional[Union[dict[Union[str, StudyStudyId], Union[dict, Study]], list[Union[dict, Study]]]])

slots.goldLayer__persons = Slot(uri=MIAPPE_GOLD.persons, name="goldLayer__persons", curie=MIAPPE_GOLD.curie('persons'),
                   model_uri=MIAPPE_GOLD.goldLayer__persons, domain=None, range=Optional[Union[dict[Union[str, PersonPersonId], Union[dict, Person]], list[Union[dict, Person]]]])

slots.goldLayer__environments = Slot(uri=MIAPPE_GOLD.environments, name="goldLayer__environments", curie=MIAPPE_GOLD.curie('environments'),
                   model_uri=MIAPPE_GOLD.goldLayer__environments, domain=None, range=Optional[Union[Union[dict, Environment], list[Union[dict, Environment]]]])

slots.goldLayer__dataFiles = Slot(uri=MIAPPE_GOLD.dataFiles, name="goldLayer__dataFiles", curie=MIAPPE_GOLD.curie('dataFiles'),
                   model_uri=MIAPPE_GOLD.goldLayer__dataFiles, domain=None, range=Optional[Union[Union[dict, DataFile], list[Union[dict, DataFile]]]])

slots.goldLayer__events = Slot(uri=MIAPPE_GOLD.events, name="goldLayer__events", curie=MIAPPE_GOLD.curie('events'),
                   model_uri=MIAPPE_GOLD.goldLayer__events, domain=None, range=Optional[Union[dict[Union[str, EventEventId], Union[dict, Event]], list[Union[dict, Event]]]])

slots.goldLayer__biologicalMaterials = Slot(uri=MIAPPE_GOLD.biologicalMaterials, name="goldLayer__biologicalMaterials", curie=MIAPPE_GOLD.curie('biologicalMaterials'),
                   model_uri=MIAPPE_GOLD.goldLayer__biologicalMaterials, domain=None, range=Optional[Union[dict[Union[str, BiologicalMaterialBiologicalMaterialId], Union[dict, BiologicalMaterial]], list[Union[dict, BiologicalMaterial]]]])

slots.goldLayer__observationUnits = Slot(uri=MIAPPE_GOLD.observationUnits, name="goldLayer__observationUnits", curie=MIAPPE_GOLD.curie('observationUnits'),
                   model_uri=MIAPPE_GOLD.goldLayer__observationUnits, domain=None, range=Optional[Union[dict[Union[int, ObservationUnitObsUnitId], Union[dict, ObservationUnit]], list[Union[dict, ObservationUnit]]]])

slots.goldLayer__samples = Slot(uri=MIAPPE_GOLD.samples, name="goldLayer__samples", curie=MIAPPE_GOLD.curie('samples'),
                   model_uri=MIAPPE_GOLD.goldLayer__samples, domain=None, range=Optional[Union[dict[Union[str, SampleSampleId], Union[dict, Sample]], list[Union[dict, Sample]]]])

slots.goldLayer__observedVariables = Slot(uri=MIAPPE_GOLD.observedVariables, name="goldLayer__observedVariables", curie=MIAPPE_GOLD.curie('observedVariables'),
                   model_uri=MIAPPE_GOLD.goldLayer__observedVariables, domain=None, range=Optional[Union[dict[Union[str, ObservedVariableVariableId], Union[dict, ObservedVariable]], list[Union[dict, ObservedVariable]]]])

slots.goldLayer__observations = Slot(uri=MIAPPE_GOLD.observations, name="goldLayer__observations", curie=MIAPPE_GOLD.curie('observations'),
                   model_uri=MIAPPE_GOLD.goldLayer__observations, domain=None, range=Optional[Union[dict[Union[str, ObservationObservationId], Union[dict, Observation]], list[Union[dict, Observation]]]])

slots.goldLayer__images = Slot(uri=MIAPPE_GOLD.images, name="goldLayer__images", curie=MIAPPE_GOLD.curie('images'),
                   model_uri=MIAPPE_GOLD.goldLayer__images, domain=None, range=Optional[Union[dict[Union[str, ImageImageId], Union[dict, Image]], list[Union[dict, Image]]]])

slots.investigation__investigationId = Slot(uri=MIAPPE_GOLD.investigationId, name="investigation__investigationId", curie=MIAPPE_GOLD.curie('investigationId'),
                   model_uri=MIAPPE_GOLD.investigation__investigationId, domain=None, range=URIRef)

slots.investigation__investigationTitle = Slot(uri=MIAPPE_GOLD.investigationTitle, name="investigation__investigationTitle", curie=MIAPPE_GOLD.curie('investigationTitle'),
                   model_uri=MIAPPE_GOLD.investigation__investigationTitle, domain=None, range=Optional[str])

slots.investigation__investigationDescription = Slot(uri=MIAPPE_GOLD.investigationDescription, name="investigation__investigationDescription", curie=MIAPPE_GOLD.curie('investigationDescription'),
                   model_uri=MIAPPE_GOLD.investigation__investigationDescription, domain=None, range=Optional[str])

slots.investigation__submissionDate = Slot(uri=MIAPPE_GOLD.submissionDate, name="investigation__submissionDate", curie=MIAPPE_GOLD.curie('submissionDate'),
                   model_uri=MIAPPE_GOLD.investigation__submissionDate, domain=None, range=Optional[Union[str, XSDDate]])

slots.investigation__publicReleaseDate = Slot(uri=MIAPPE_GOLD.publicReleaseDate, name="investigation__publicReleaseDate", curie=MIAPPE_GOLD.curie('publicReleaseDate'),
                   model_uri=MIAPPE_GOLD.investigation__publicReleaseDate, domain=None, range=Optional[str])

slots.investigation__license = Slot(uri=MIAPPE_GOLD.license, name="investigation__license", curie=MIAPPE_GOLD.curie('license'),
                   model_uri=MIAPPE_GOLD.investigation__license, domain=None, range=Optional[str])

slots.investigation__miappeVersion = Slot(uri=MIAPPE_GOLD.miappeVersion, name="investigation__miappeVersion", curie=MIAPPE_GOLD.curie('miappeVersion'),
                   model_uri=MIAPPE_GOLD.investigation__miappeVersion, domain=None, range=Optional[float])

slots.investigation__associatedPublication = Slot(uri=MIAPPE_GOLD.associatedPublication, name="investigation__associatedPublication", curie=MIAPPE_GOLD.curie('associatedPublication'),
                   model_uri=MIAPPE_GOLD.investigation__associatedPublication, domain=None, range=Optional[str])

slots.study__studyId = Slot(uri=MIAPPE_GOLD.studyId, name="study__studyId", curie=MIAPPE_GOLD.curie('studyId'),
                   model_uri=MIAPPE_GOLD.study__studyId, domain=None, range=URIRef)

slots.study__investigationId = Slot(uri=MIAPPE_GOLD.investigationId, name="study__investigationId", curie=MIAPPE_GOLD.curie('investigationId'),
                   model_uri=MIAPPE_GOLD.study__investigationId, domain=None, range=Union[str, InvestigationInvestigationId])

slots.study__studyTitle = Slot(uri=MIAPPE_GOLD.studyTitle, name="study__studyTitle", curie=MIAPPE_GOLD.curie('studyTitle'),
                   model_uri=MIAPPE_GOLD.study__studyTitle, domain=None, range=Optional[str])

slots.study__studyDescription = Slot(uri=MIAPPE_GOLD.studyDescription, name="study__studyDescription", curie=MIAPPE_GOLD.curie('studyDescription'),
                   model_uri=MIAPPE_GOLD.study__studyDescription, domain=None, range=Optional[str])

slots.study__studyStartDate = Slot(uri=MIAPPE_GOLD.studyStartDate, name="study__studyStartDate", curie=MIAPPE_GOLD.curie('studyStartDate'),
                   model_uri=MIAPPE_GOLD.study__studyStartDate, domain=None, range=Optional[Union[str, XSDDate]])

slots.study__studyEndDate = Slot(uri=MIAPPE_GOLD.studyEndDate, name="study__studyEndDate", curie=MIAPPE_GOLD.curie('studyEndDate'),
                   model_uri=MIAPPE_GOLD.study__studyEndDate, domain=None, range=Optional[Union[str, XSDDate]])

slots.study__contactInst = Slot(uri=MIAPPE_GOLD.contactInst, name="study__contactInst", curie=MIAPPE_GOLD.curie('contactInst'),
                   model_uri=MIAPPE_GOLD.study__contactInst, domain=None, range=Optional[str])

slots.study__locationCountry = Slot(uri=MIAPPE_GOLD.locationCountry, name="study__locationCountry", curie=MIAPPE_GOLD.curie('locationCountry'),
                   model_uri=MIAPPE_GOLD.study__locationCountry, domain=None, range=Optional[str])

slots.study__siteName = Slot(uri=MIAPPE_GOLD.siteName, name="study__siteName", curie=MIAPPE_GOLD.curie('siteName'),
                   model_uri=MIAPPE_GOLD.study__siteName, domain=None, range=Optional[str])

slots.study__locationLatitude = Slot(uri=MIAPPE_GOLD.locationLatitude, name="study__locationLatitude", curie=MIAPPE_GOLD.curie('locationLatitude'),
                   model_uri=MIAPPE_GOLD.study__locationLatitude, domain=None, range=Optional[float])

slots.study__locationLongitude = Slot(uri=MIAPPE_GOLD.locationLongitude, name="study__locationLongitude", curie=MIAPPE_GOLD.curie('locationLongitude'),
                   model_uri=MIAPPE_GOLD.study__locationLongitude, domain=None, range=Optional[float])

slots.study__locationAltitude = Slot(uri=MIAPPE_GOLD.locationAltitude, name="study__locationAltitude", curie=MIAPPE_GOLD.curie('locationAltitude'),
                   model_uri=MIAPPE_GOLD.study__locationAltitude, domain=None, range=Optional[str])

slots.study__expeDesignDesc = Slot(uri=MIAPPE_GOLD.expeDesignDesc, name="study__expeDesignDesc", curie=MIAPPE_GOLD.curie('expeDesignDesc'),
                   model_uri=MIAPPE_GOLD.study__expeDesignDesc, domain=None, range=Optional[str])

slots.study__expeDesignType = Slot(uri=MIAPPE_GOLD.expeDesignType, name="study__expeDesignType", curie=MIAPPE_GOLD.curie('expeDesignType'),
                   model_uri=MIAPPE_GOLD.study__expeDesignType, domain=None, range=Optional[str])

slots.study__obsUnitLevelHierarchy = Slot(uri=MIAPPE_GOLD.obsUnitLevelHierarchy, name="study__obsUnitLevelHierarchy", curie=MIAPPE_GOLD.curie('obsUnitLevelHierarchy'),
                   model_uri=MIAPPE_GOLD.study__obsUnitLevelHierarchy, domain=None, range=Optional[str])

slots.study__obsUnitDesc = Slot(uri=MIAPPE_GOLD.obsUnitDesc, name="study__obsUnitDesc", curie=MIAPPE_GOLD.curie('obsUnitDesc'),
                   model_uri=MIAPPE_GOLD.study__obsUnitDesc, domain=None, range=Optional[str])

slots.study__growthFacilityDesc = Slot(uri=MIAPPE_GOLD.growthFacilityDesc, name="study__growthFacilityDesc", curie=MIAPPE_GOLD.curie('growthFacilityDesc'),
                   model_uri=MIAPPE_GOLD.study__growthFacilityDesc, domain=None, range=Optional[str])

slots.study__growthFacilityType = Slot(uri=MIAPPE_GOLD.growthFacilityType, name="study__growthFacilityType", curie=MIAPPE_GOLD.curie('growthFacilityType'),
                   model_uri=MIAPPE_GOLD.study__growthFacilityType, domain=None, range=Optional[str])

slots.study__culturalPractice = Slot(uri=MIAPPE_GOLD.culturalPractice, name="study__culturalPractice", curie=MIAPPE_GOLD.curie('culturalPractice'),
                   model_uri=MIAPPE_GOLD.study__culturalPractice, domain=None, range=Optional[str])

slots.study__expeDesignMap = Slot(uri=MIAPPE_GOLD.expeDesignMap, name="study__expeDesignMap", curie=MIAPPE_GOLD.curie('expeDesignMap'),
                   model_uri=MIAPPE_GOLD.study__expeDesignMap, domain=None, range=Optional[str])

slots.person__studyId = Slot(uri=MIAPPE_GOLD.studyId, name="person__studyId", curie=MIAPPE_GOLD.curie('studyId'),
                   model_uri=MIAPPE_GOLD.person__studyId, domain=None, range=Union[str, StudyStudyId])

slots.person__personName = Slot(uri=MIAPPE_GOLD.personName, name="person__personName", curie=MIAPPE_GOLD.curie('personName'),
                   model_uri=MIAPPE_GOLD.person__personName, domain=None, range=Optional[str])

slots.person__personEmail = Slot(uri=MIAPPE_GOLD.personEmail, name="person__personEmail", curie=MIAPPE_GOLD.curie('personEmail'),
                   model_uri=MIAPPE_GOLD.person__personEmail, domain=None, range=Optional[str])

slots.person__personId = Slot(uri=MIAPPE_GOLD.personId, name="person__personId", curie=MIAPPE_GOLD.curie('personId'),
                   model_uri=MIAPPE_GOLD.person__personId, domain=None, range=URIRef)

slots.person__personRole = Slot(uri=MIAPPE_GOLD.personRole, name="person__personRole", curie=MIAPPE_GOLD.curie('personRole'),
                   model_uri=MIAPPE_GOLD.person__personRole, domain=None, range=Optional[str])

slots.person__personAffiliation = Slot(uri=MIAPPE_GOLD.personAffiliation, name="person__personAffiliation", curie=MIAPPE_GOLD.curie('personAffiliation'),
                   model_uri=MIAPPE_GOLD.person__personAffiliation, domain=None, range=Optional[str])

slots.environment__studyId = Slot(uri=MIAPPE_GOLD.studyId, name="environment__studyId", curie=MIAPPE_GOLD.curie('studyId'),
                   model_uri=MIAPPE_GOLD.environment__studyId, domain=None, range=Union[str, StudyStudyId])

slots.environment__envParam = Slot(uri=MIAPPE_GOLD.envParam, name="environment__envParam", curie=MIAPPE_GOLD.curie('envParam'),
                   model_uri=MIAPPE_GOLD.environment__envParam, domain=None, range=str)

slots.environment__envParamValue = Slot(uri=MIAPPE_GOLD.envParamValue, name="environment__envParamValue", curie=MIAPPE_GOLD.curie('envParamValue'),
                   model_uri=MIAPPE_GOLD.environment__envParamValue, domain=None, range=Optional[str])

slots.dataFile__studyId = Slot(uri=MIAPPE_GOLD.studyId, name="dataFile__studyId", curie=MIAPPE_GOLD.curie('studyId'),
                   model_uri=MIAPPE_GOLD.dataFile__studyId, domain=None, range=Union[str, StudyStudyId])

slots.dataFile__dataFileLink = Slot(uri=MIAPPE_GOLD.dataFileLink, name="dataFile__dataFileLink", curie=MIAPPE_GOLD.curie('dataFileLink'),
                   model_uri=MIAPPE_GOLD.dataFile__dataFileLink, domain=None, range=str)

slots.dataFile__dataFileDesc = Slot(uri=MIAPPE_GOLD.dataFileDesc, name="dataFile__dataFileDesc", curie=MIAPPE_GOLD.curie('dataFileDesc'),
                   model_uri=MIAPPE_GOLD.dataFile__dataFileDesc, domain=None, range=Optional[str])

slots.dataFile__dataFileVersion = Slot(uri=MIAPPE_GOLD.dataFileVersion, name="dataFile__dataFileVersion", curie=MIAPPE_GOLD.curie('dataFileVersion'),
                   model_uri=MIAPPE_GOLD.dataFile__dataFileVersion, domain=None, range=Optional[str])

slots.event__eventId = Slot(uri=MIAPPE_GOLD.eventId, name="event__eventId", curie=MIAPPE_GOLD.curie('eventId'),
                   model_uri=MIAPPE_GOLD.event__eventId, domain=None, range=URIRef)

slots.event__studyId = Slot(uri=MIAPPE_GOLD.studyId, name="event__studyId", curie=MIAPPE_GOLD.curie('studyId'),
                   model_uri=MIAPPE_GOLD.event__studyId, domain=None, range=Union[str, StudyStudyId])

slots.event__obsUnitId = Slot(uri=MIAPPE_GOLD.obsUnitId, name="event__obsUnitId", curie=MIAPPE_GOLD.curie('obsUnitId'),
                   model_uri=MIAPPE_GOLD.event__obsUnitId, domain=None, range=Optional[int])

slots.event__eventType = Slot(uri=MIAPPE_GOLD.eventType, name="event__eventType", curie=MIAPPE_GOLD.curie('eventType'),
                   model_uri=MIAPPE_GOLD.event__eventType, domain=None, range=Optional[str])

slots.event__eventAccNumber = Slot(uri=MIAPPE_GOLD.eventAccNumber, name="event__eventAccNumber", curie=MIAPPE_GOLD.curie('eventAccNumber'),
                   model_uri=MIAPPE_GOLD.event__eventAccNumber, domain=None, range=Optional[str])

slots.event__eventDesc = Slot(uri=MIAPPE_GOLD.eventDesc, name="event__eventDesc", curie=MIAPPE_GOLD.curie('eventDesc'),
                   model_uri=MIAPPE_GOLD.event__eventDesc, domain=None, range=Optional[str])

slots.event__eventDate = Slot(uri=MIAPPE_GOLD.eventDate, name="event__eventDate", curie=MIAPPE_GOLD.curie('eventDate'),
                   model_uri=MIAPPE_GOLD.event__eventDate, domain=None, range=Optional[Union[str, XSDDate]])

slots.biologicalMaterial__studyId = Slot(uri=MIAPPE_GOLD.studyId, name="biologicalMaterial__studyId", curie=MIAPPE_GOLD.curie('studyId'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__studyId, domain=None, range=Union[str, StudyStudyId])

slots.biologicalMaterial__biologicalMaterialId = Slot(uri=MIAPPE_GOLD.biologicalMaterialId, name="biologicalMaterial__biologicalMaterialId", curie=MIAPPE_GOLD.curie('biologicalMaterialId'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__biologicalMaterialId, domain=None, range=URIRef)

slots.biologicalMaterial__biologicalMaterialExtId = Slot(uri=MIAPPE_GOLD.biologicalMaterialExtId, name="biologicalMaterial__biologicalMaterialExtId", curie=MIAPPE_GOLD.curie('biologicalMaterialExtId'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__biologicalMaterialExtId, domain=None, range=Optional[str])

slots.biologicalMaterial__organism = Slot(uri=MIAPPE_GOLD.organism, name="biologicalMaterial__organism", curie=MIAPPE_GOLD.curie('organism'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__organism, domain=None, range=Optional[str])

slots.biologicalMaterial__genus = Slot(uri=MIAPPE_GOLD.genus, name="biologicalMaterial__genus", curie=MIAPPE_GOLD.curie('genus'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__genus, domain=None, range=Optional[str])

slots.biologicalMaterial__species = Slot(uri=MIAPPE_GOLD.species, name="biologicalMaterial__species", curie=MIAPPE_GOLD.curie('species'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__species, domain=None, range=Optional[str])

slots.biologicalMaterial__infraspecificName = Slot(uri=MIAPPE_GOLD.infraspecificName, name="biologicalMaterial__infraspecificName", curie=MIAPPE_GOLD.curie('infraspecificName'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__infraspecificName, domain=None, range=Optional[str])

slots.biologicalMaterial__biologicalMaterialLatitude = Slot(uri=MIAPPE_GOLD.biologicalMaterialLatitude, name="biologicalMaterial__biologicalMaterialLatitude", curie=MIAPPE_GOLD.curie('biologicalMaterialLatitude'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__biologicalMaterialLatitude, domain=None, range=Optional[float])

slots.biologicalMaterial__biologicalMaterialLongitude = Slot(uri=MIAPPE_GOLD.biologicalMaterialLongitude, name="biologicalMaterial__biologicalMaterialLongitude", curie=MIAPPE_GOLD.curie('biologicalMaterialLongitude'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__biologicalMaterialLongitude, domain=None, range=Optional[float])

slots.biologicalMaterial__biologicalMaterialAltitude = Slot(uri=MIAPPE_GOLD.biologicalMaterialAltitude, name="biologicalMaterial__biologicalMaterialAltitude", curie=MIAPPE_GOLD.curie('biologicalMaterialAltitude'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__biologicalMaterialAltitude, domain=None, range=Optional[str])

slots.biologicalMaterial__biologicalMaterialCoordUncertainty = Slot(uri=MIAPPE_GOLD.biologicalMaterialCoordUncertainty, name="biologicalMaterial__biologicalMaterialCoordUncertainty", curie=MIAPPE_GOLD.curie('biologicalMaterialCoordUncertainty'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__biologicalMaterialCoordUncertainty, domain=None, range=Optional[str])

slots.biologicalMaterial__biologicalMaterialPreprocessing = Slot(uri=MIAPPE_GOLD.biologicalMaterialPreprocessing, name="biologicalMaterial__biologicalMaterialPreprocessing", curie=MIAPPE_GOLD.curie('biologicalMaterialPreprocessing'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__biologicalMaterialPreprocessing, domain=None, range=Optional[str])

slots.biologicalMaterial__materialSourceId = Slot(uri=MIAPPE_GOLD.materialSourceId, name="biologicalMaterial__materialSourceId", curie=MIAPPE_GOLD.curie('materialSourceId'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__materialSourceId, domain=None, range=Optional[str])

slots.biologicalMaterial__materialSourceDoi = Slot(uri=MIAPPE_GOLD.materialSourceDoi, name="biologicalMaterial__materialSourceDoi", curie=MIAPPE_GOLD.curie('materialSourceDoi'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__materialSourceDoi, domain=None, range=Optional[str])

slots.biologicalMaterial__materialSourceAccNumber = Slot(uri=MIAPPE_GOLD.materialSourceAccNumber, name="biologicalMaterial__materialSourceAccNumber", curie=MIAPPE_GOLD.curie('materialSourceAccNumber'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__materialSourceAccNumber, domain=None, range=Optional[str])

slots.biologicalMaterial__materialSourceAccName = Slot(uri=MIAPPE_GOLD.materialSourceAccName, name="biologicalMaterial__materialSourceAccName", curie=MIAPPE_GOLD.curie('materialSourceAccName'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__materialSourceAccName, domain=None, range=Optional[str])

slots.biologicalMaterial__materialSourceInstCode = Slot(uri=MIAPPE_GOLD.materialSourceInstCode, name="biologicalMaterial__materialSourceInstCode", curie=MIAPPE_GOLD.curie('materialSourceInstCode'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__materialSourceInstCode, domain=None, range=Optional[str])

slots.biologicalMaterial__materialSourceInstName = Slot(uri=MIAPPE_GOLD.materialSourceInstName, name="biologicalMaterial__materialSourceInstName", curie=MIAPPE_GOLD.curie('materialSourceInstName'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__materialSourceInstName, domain=None, range=Optional[str])

slots.biologicalMaterial__materialSourceOtherIds = Slot(uri=MIAPPE_GOLD.materialSourceOtherIds, name="biologicalMaterial__materialSourceOtherIds", curie=MIAPPE_GOLD.curie('materialSourceOtherIds'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__materialSourceOtherIds, domain=None, range=Optional[str])

slots.biologicalMaterial__materialSourceLatitude = Slot(uri=MIAPPE_GOLD.materialSourceLatitude, name="biologicalMaterial__materialSourceLatitude", curie=MIAPPE_GOLD.curie('materialSourceLatitude'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__materialSourceLatitude, domain=None, range=Optional[str])

slots.biologicalMaterial__materialSourceLongitude = Slot(uri=MIAPPE_GOLD.materialSourceLongitude, name="biologicalMaterial__materialSourceLongitude", curie=MIAPPE_GOLD.curie('materialSourceLongitude'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__materialSourceLongitude, domain=None, range=Optional[str])

slots.biologicalMaterial__materialSourceAltitude = Slot(uri=MIAPPE_GOLD.materialSourceAltitude, name="biologicalMaterial__materialSourceAltitude", curie=MIAPPE_GOLD.curie('materialSourceAltitude'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__materialSourceAltitude, domain=None, range=Optional[str])

slots.biologicalMaterial__materialSourceCoordUncertainty = Slot(uri=MIAPPE_GOLD.materialSourceCoordUncertainty, name="biologicalMaterial__materialSourceCoordUncertainty", curie=MIAPPE_GOLD.curie('materialSourceCoordUncertainty'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__materialSourceCoordUncertainty, domain=None, range=Optional[str])

slots.biologicalMaterial__materialSourceDesc = Slot(uri=MIAPPE_GOLD.materialSourceDesc, name="biologicalMaterial__materialSourceDesc", curie=MIAPPE_GOLD.curie('materialSourceDesc'),
                   model_uri=MIAPPE_GOLD.biologicalMaterial__materialSourceDesc, domain=None, range=Optional[str])

slots.observationUnit__studyId = Slot(uri=MIAPPE_GOLD.studyId, name="observationUnit__studyId", curie=MIAPPE_GOLD.curie('studyId'),
                   model_uri=MIAPPE_GOLD.observationUnit__studyId, domain=None, range=Union[str, StudyStudyId])

slots.observationUnit__obsUnitId = Slot(uri=MIAPPE_GOLD.obsUnitId, name="observationUnit__obsUnitId", curie=MIAPPE_GOLD.curie('obsUnitId'),
                   model_uri=MIAPPE_GOLD.observationUnit__obsUnitId, domain=None, range=URIRef)

slots.observationUnit__biologicalMaterialId = Slot(uri=MIAPPE_GOLD.biologicalMaterialId, name="observationUnit__biologicalMaterialId", curie=MIAPPE_GOLD.curie('biologicalMaterialId'),
                   model_uri=MIAPPE_GOLD.observationUnit__biologicalMaterialId, domain=None, range=Union[str, BiologicalMaterialBiologicalMaterialId])

slots.observationUnit__obsUnitType = Slot(uri=MIAPPE_GOLD.obsUnitType, name="observationUnit__obsUnitType", curie=MIAPPE_GOLD.curie('obsUnitType'),
                   model_uri=MIAPPE_GOLD.observationUnit__obsUnitType, domain=None, range=Optional[str])

slots.observationUnit__externalId = Slot(uri=MIAPPE_GOLD.externalId, name="observationUnit__externalId", curie=MIAPPE_GOLD.curie('externalId'),
                   model_uri=MIAPPE_GOLD.observationUnit__externalId, domain=None, range=Optional[int])

slots.observationUnit__spatialDistribution = Slot(uri=MIAPPE_GOLD.spatialDistribution, name="observationUnit__spatialDistribution", curie=MIAPPE_GOLD.curie('spatialDistribution'),
                   model_uri=MIAPPE_GOLD.observationUnit__spatialDistribution, domain=None, range=Optional[str])

slots.observationUnit__obsUnitFactorValue = Slot(uri=MIAPPE_GOLD.obsUnitFactorValue, name="observationUnit__obsUnitFactorValue", curie=MIAPPE_GOLD.curie('obsUnitFactorValue'),
                   model_uri=MIAPPE_GOLD.observationUnit__obsUnitFactorValue, domain=None, range=Optional[str])

slots.sample__obsUnitId = Slot(uri=MIAPPE_GOLD.obsUnitId, name="sample__obsUnitId", curie=MIAPPE_GOLD.curie('obsUnitId'),
                   model_uri=MIAPPE_GOLD.sample__obsUnitId, domain=None, range=Union[int, ObservationUnitObsUnitId])

slots.sample__sampleId = Slot(uri=MIAPPE_GOLD.sampleId, name="sample__sampleId", curie=MIAPPE_GOLD.curie('sampleId'),
                   model_uri=MIAPPE_GOLD.sample__sampleId, domain=None, range=URIRef)

slots.sample__developmentStage = Slot(uri=MIAPPE_GOLD.developmentStage, name="sample__developmentStage", curie=MIAPPE_GOLD.curie('developmentStage'),
                   model_uri=MIAPPE_GOLD.sample__developmentStage, domain=None, range=Optional[str])

slots.sample__anatomicalEntity = Slot(uri=MIAPPE_GOLD.anatomicalEntity, name="sample__anatomicalEntity", curie=MIAPPE_GOLD.curie('anatomicalEntity'),
                   model_uri=MIAPPE_GOLD.sample__anatomicalEntity, domain=None, range=Optional[str])

slots.sample__sampleDesc = Slot(uri=MIAPPE_GOLD.sampleDesc, name="sample__sampleDesc", curie=MIAPPE_GOLD.curie('sampleDesc'),
                   model_uri=MIAPPE_GOLD.sample__sampleDesc, domain=None, range=Optional[str])

slots.sample__collectionDate = Slot(uri=MIAPPE_GOLD.collectionDate, name="sample__collectionDate", curie=MIAPPE_GOLD.curie('collectionDate'),
                   model_uri=MIAPPE_GOLD.sample__collectionDate, domain=None, range=Optional[str])

slots.sample__externalId = Slot(uri=MIAPPE_GOLD.externalId, name="sample__externalId", curie=MIAPPE_GOLD.curie('externalId'),
                   model_uri=MIAPPE_GOLD.sample__externalId, domain=None, range=Optional[str])

slots.observedVariable__studyId = Slot(uri=MIAPPE_GOLD.studyId, name="observedVariable__studyId", curie=MIAPPE_GOLD.curie('studyId'),
                   model_uri=MIAPPE_GOLD.observedVariable__studyId, domain=None, range=Union[str, StudyStudyId])

slots.observedVariable__variableId = Slot(uri=MIAPPE_GOLD.variableId, name="observedVariable__variableId", curie=MIAPPE_GOLD.curie('variableId'),
                   model_uri=MIAPPE_GOLD.observedVariable__variableId, domain=None, range=URIRef)

slots.observedVariable__variableName = Slot(uri=MIAPPE_GOLD.variableName, name="observedVariable__variableName", curie=MIAPPE_GOLD.curie('variableName'),
                   model_uri=MIAPPE_GOLD.observedVariable__variableName, domain=None, range=Optional[str])

slots.observedVariable__variableAccNumber = Slot(uri=MIAPPE_GOLD.variableAccNumber, name="observedVariable__variableAccNumber", curie=MIAPPE_GOLD.curie('variableAccNumber'),
                   model_uri=MIAPPE_GOLD.observedVariable__variableAccNumber, domain=None, range=Optional[str])

slots.observedVariable__traitName = Slot(uri=MIAPPE_GOLD.traitName, name="observedVariable__traitName", curie=MIAPPE_GOLD.curie('traitName'),
                   model_uri=MIAPPE_GOLD.observedVariable__traitName, domain=None, range=Optional[str])

slots.observedVariable__traitEntity = Slot(uri=MIAPPE_GOLD.traitEntity, name="observedVariable__traitEntity", curie=MIAPPE_GOLD.curie('traitEntity'),
                   model_uri=MIAPPE_GOLD.observedVariable__traitEntity, domain=None, range=Optional[str])

slots.observedVariable__traitEntityAccessionNumber = Slot(uri=MIAPPE_GOLD.traitEntityAccessionNumber, name="observedVariable__traitEntityAccessionNumber", curie=MIAPPE_GOLD.curie('traitEntityAccessionNumber'),
                   model_uri=MIAPPE_GOLD.observedVariable__traitEntityAccessionNumber, domain=None, range=Optional[str])

slots.observedVariable__traitCharacteristic = Slot(uri=MIAPPE_GOLD.traitCharacteristic, name="observedVariable__traitCharacteristic", curie=MIAPPE_GOLD.curie('traitCharacteristic'),
                   model_uri=MIAPPE_GOLD.observedVariable__traitCharacteristic, domain=None, range=Optional[str])

slots.observedVariable__traitCharacteristicAccessionNumber = Slot(uri=MIAPPE_GOLD.traitCharacteristicAccessionNumber, name="observedVariable__traitCharacteristicAccessionNumber", curie=MIAPPE_GOLD.curie('traitCharacteristicAccessionNumber'),
                   model_uri=MIAPPE_GOLD.observedVariable__traitCharacteristicAccessionNumber, domain=None, range=Optional[str])

slots.observedVariable__traitAccNumber = Slot(uri=MIAPPE_GOLD.traitAccNumber, name="observedVariable__traitAccNumber", curie=MIAPPE_GOLD.curie('traitAccNumber'),
                   model_uri=MIAPPE_GOLD.observedVariable__traitAccNumber, domain=None, range=Optional[str])

slots.observedVariable__methodName = Slot(uri=MIAPPE_GOLD.methodName, name="observedVariable__methodName", curie=MIAPPE_GOLD.curie('methodName'),
                   model_uri=MIAPPE_GOLD.observedVariable__methodName, domain=None, range=Optional[str])

slots.observedVariable__methodAccNumber = Slot(uri=MIAPPE_GOLD.methodAccNumber, name="observedVariable__methodAccNumber", curie=MIAPPE_GOLD.curie('methodAccNumber'),
                   model_uri=MIAPPE_GOLD.observedVariable__methodAccNumber, domain=None, range=Optional[str])

slots.observedVariable__methodDesc = Slot(uri=MIAPPE_GOLD.methodDesc, name="observedVariable__methodDesc", curie=MIAPPE_GOLD.curie('methodDesc'),
                   model_uri=MIAPPE_GOLD.observedVariable__methodDesc, domain=None, range=Optional[str])

slots.observedVariable__methodRef = Slot(uri=MIAPPE_GOLD.methodRef, name="observedVariable__methodRef", curie=MIAPPE_GOLD.curie('methodRef'),
                   model_uri=MIAPPE_GOLD.observedVariable__methodRef, domain=None, range=Optional[str])

slots.observedVariable__scaleName = Slot(uri=MIAPPE_GOLD.scaleName, name="observedVariable__scaleName", curie=MIAPPE_GOLD.curie('scaleName'),
                   model_uri=MIAPPE_GOLD.observedVariable__scaleName, domain=None, range=Optional[str])

slots.observedVariable__scaleAccNumber = Slot(uri=MIAPPE_GOLD.scaleAccNumber, name="observedVariable__scaleAccNumber", curie=MIAPPE_GOLD.curie('scaleAccNumber'),
                   model_uri=MIAPPE_GOLD.observedVariable__scaleAccNumber, domain=None, range=Optional[str])

slots.observedVariable__timeScale = Slot(uri=MIAPPE_GOLD.timeScale, name="observedVariable__timeScale", curie=MIAPPE_GOLD.curie('timeScale'),
                   model_uri=MIAPPE_GOLD.observedVariable__timeScale, domain=None, range=Optional[str])

slots.observation__observationId = Slot(uri=MIAPPE_GOLD.observationId, name="observation__observationId", curie=MIAPPE_GOLD.curie('observationId'),
                   model_uri=MIAPPE_GOLD.observation__observationId, domain=None, range=URIRef)

slots.observation__studyId = Slot(uri=MIAPPE_GOLD.studyId, name="observation__studyId", curie=MIAPPE_GOLD.curie('studyId'),
                   model_uri=MIAPPE_GOLD.observation__studyId, domain=None, range=Union[str, StudyStudyId])

slots.observation__obsUnitId = Slot(uri=MIAPPE_GOLD.obsUnitId, name="observation__obsUnitId", curie=MIAPPE_GOLD.curie('obsUnitId'),
                   model_uri=MIAPPE_GOLD.observation__obsUnitId, domain=None, range=Union[int, ObservationUnitObsUnitId])

slots.observation__sampleId = Slot(uri=MIAPPE_GOLD.sampleId, name="observation__sampleId", curie=MIAPPE_GOLD.curie('sampleId'),
                   model_uri=MIAPPE_GOLD.observation__sampleId, domain=None, range=Optional[Union[str, SampleSampleId]])

slots.observation__observationTimestamp = Slot(uri=MIAPPE_GOLD.observationTimestamp, name="observation__observationTimestamp", curie=MIAPPE_GOLD.curie('observationTimestamp'),
                   model_uri=MIAPPE_GOLD.observation__observationTimestamp, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.observation__variableId = Slot(uri=MIAPPE_GOLD.variableId, name="observation__variableId", curie=MIAPPE_GOLD.curie('variableId'),
                   model_uri=MIAPPE_GOLD.observation__variableId, domain=None, range=Union[str, ObservedVariableVariableId])

slots.observation__observationValue = Slot(uri=MIAPPE_GOLD.observationValue, name="observation__observationValue", curie=MIAPPE_GOLD.curie('observationValue'),
                   model_uri=MIAPPE_GOLD.observation__observationValue, domain=None, range=Optional[float])

slots.observation__replicate = Slot(uri=MIAPPE_GOLD.replicate, name="observation__replicate", curie=MIAPPE_GOLD.curie('replicate'),
                   model_uri=MIAPPE_GOLD.observation__replicate, domain=None, range=Optional[str])

slots.observation__qualityFlag = Slot(uri=MIAPPE_GOLD.qualityFlag, name="observation__qualityFlag", curie=MIAPPE_GOLD.curie('qualityFlag'),
                   model_uri=MIAPPE_GOLD.observation__qualityFlag, domain=None, range=Optional[str])

slots.observation__notes = Slot(uri=MIAPPE_GOLD.notes, name="observation__notes", curie=MIAPPE_GOLD.curie('notes'),
                   model_uri=MIAPPE_GOLD.observation__notes, domain=None, range=Optional[str])

slots.image__imageId = Slot(uri=MIAPPE_GOLD.imageId, name="image__imageId", curie=MIAPPE_GOLD.curie('imageId'),
                   model_uri=MIAPPE_GOLD.image__imageId, domain=None, range=URIRef)

slots.image__studyId = Slot(uri=MIAPPE_GOLD.studyId, name="image__studyId", curie=MIAPPE_GOLD.curie('studyId'),
                   model_uri=MIAPPE_GOLD.image__studyId, domain=None, range=Union[str, StudyStudyId])

slots.image__obsUnitId = Slot(uri=MIAPPE_GOLD.obsUnitId, name="image__obsUnitId", curie=MIAPPE_GOLD.curie('obsUnitId'),
                   model_uri=MIAPPE_GOLD.image__obsUnitId, domain=None, range=Union[int, ObservationUnitObsUnitId])

slots.image__sampleId = Slot(uri=MIAPPE_GOLD.sampleId, name="image__sampleId", curie=MIAPPE_GOLD.curie('sampleId'),
                   model_uri=MIAPPE_GOLD.image__sampleId, domain=None, range=Optional[str])

slots.image__observationTimestamp = Slot(uri=MIAPPE_GOLD.observationTimestamp, name="image__observationTimestamp", curie=MIAPPE_GOLD.curie('observationTimestamp'),
                   model_uri=MIAPPE_GOLD.image__observationTimestamp, domain=None, range=Optional[str])

slots.image__Modality = Slot(uri=MIAPPE_GOLD.Modality, name="image__Modality", curie=MIAPPE_GOLD.curie('Modality'),
                   model_uri=MIAPPE_GOLD.image__Modality, domain=None, range=Optional[str])

slots.image__fileType = Slot(uri=MIAPPE_GOLD.fileType, name="image__fileType", curie=MIAPPE_GOLD.curie('fileType'),
                   model_uri=MIAPPE_GOLD.image__fileType, domain=None, range=Optional[str])

slots.image__filePath = Slot(uri=MIAPPE_GOLD.filePath, name="image__filePath", curie=MIAPPE_GOLD.curie('filePath'),
                   model_uri=MIAPPE_GOLD.image__filePath, domain=None, range=Optional[str])

slots.image__notes = Slot(uri=MIAPPE_GOLD.notes, name="image__notes", curie=MIAPPE_GOLD.curie('notes'),
                   model_uri=MIAPPE_GOLD.image__notes, domain=None, range=Optional[str])
