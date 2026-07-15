from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'miappe_gold',
     'default_range': 'string',
     'description': 'Cleaned, conformed, one-class-per-table model of a MIAPPE 1.2 '
                    'plant phenotyping dataset: Populus trichocarpa observed at '
                    'ORNL between 2024-03-26 and 2024-05-09. Facts are '
                    'de-duplicated and carry deterministic md5 surrogate keys, so '
                    'a reload reproduces identical identifiers.',
     'id': 'https://w3id.org/ornl/miappe-gold',
     'imports': ['linkml:types'],
     'name': 'miappe-gold',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'miappe_gold': {'prefix_prefix': 'miappe_gold',
                                  'prefix_reference': 'https://w3id.org/ornl/miappe-gold/'}},
     'source_file': 'src/linkml_test/schema/linkml_test.yaml',
     'title': 'MIAPPE 1.2 Gold Layer - Weston Poplar GWAS Phenotyping Experiment'} )


class GoldLayer(ConfiguredBaseModel):
    """
    Container holding one collection per Parquet file.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ornl/miappe-gold', 'tree_root': True})

    investigations: Optional[list[Investigation]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GoldLayer']} })
    studies: Optional[list[Study]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GoldLayer']} })
    persons: Optional[list[Person]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GoldLayer']} })
    environments: Optional[list[Environment]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GoldLayer']} })
    dataFiles: Optional[list[DataFile]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GoldLayer']} })
    events: Optional[list[Event]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GoldLayer']} })
    biologicalMaterials: Optional[list[BiologicalMaterial]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GoldLayer']} })
    observationUnits: Optional[list[ObservationUnit]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GoldLayer']} })
    samples: Optional[list[Sample]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GoldLayer']} })
    observedVariables: Optional[list[ObservedVariable]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GoldLayer']} })
    observations: Optional[list[Observation]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GoldLayer']} })
    images: Optional[list[Image]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GoldLayer']} })


class Investigation(ConfiguredBaseModel):
    """
    Top-level research context. A single investigation groups one or more studies.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'parquet_file': {'tag': 'parquet_file',
                                          'value': 'Investigation.parquet'},
                         'rows_in_current_data': {'tag': 'rows_in_current_data',
                                                  'value': 1}},
         'from_schema': 'https://w3id.org/ornl/miappe-gold'})

    investigationId: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Investigation', 'Study']} })
    investigationTitle: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Investigation']} })
    investigationDescription: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Investigation']} })
    submissionDate: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Investigation']} })
    publicReleaseDate: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 1 rows; Parquet defaulted the type to '
                      'string. A MIAPPE slot this study never filled.'],
         'domain_of': ['Investigation']} })
    license: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 1 rows; Parquet defaulted the type to '
                      'string. A MIAPPE slot this study never filled.'],
         'domain_of': ['Investigation']} })
    miappeVersion: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Investigation']} })
    associatedPublication: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 1 rows; Parquet defaulted the type to '
                      'string. A MIAPPE slot this study never filled.'],
         'domain_of': ['Investigation']} })


class Study(ConfiguredBaseModel):
    """
    One experiment at one site over one date range. Every other table reaches this.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'parquet_file': {'tag': 'parquet_file',
                                          'value': 'Study.parquet'},
                         'rows_in_current_data': {'tag': 'rows_in_current_data',
                                                  'value': 1}},
         'from_schema': 'https://w3id.org/ornl/miappe-gold'})

    studyId: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Study',
                       'Person',
                       'Environment',
                       'DataFile',
                       'Event',
                       'BiologicalMaterial',
                       'ObservationUnit',
                       'ObservedVariable',
                       'Observation',
                       'Image']} })
    investigationId: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Investigation', 'Study']} })
    studyTitle: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    studyDescription: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    studyStartDate: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    studyEndDate: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    contactInst: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    locationCountry: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    siteName: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    locationLatitude: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    locationLongitude: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    locationAltitude: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 1 rows; Parquet defaulted the type to '
                      'string. A MIAPPE slot this study never filled.'],
         'domain_of': ['Study']} })
    expeDesignDesc: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    expeDesignType: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 1 rows; Parquet defaulted the type to '
                      'string. A MIAPPE slot this study never filled.'],
         'domain_of': ['Study']} })
    obsUnitLevelHierarchy: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    obsUnitDesc: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    growthFacilityDesc: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    growthFacilityType: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 1 rows; Parquet defaulted the type to '
                      'string. A MIAPPE slot this study never filled.'],
         'domain_of': ['Study']} })
    culturalPractice: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    expeDesignMap: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 1 rows; Parquet defaulted the type to '
                      'string. A MIAPPE slot this study never filled.'],
         'domain_of': ['Study']} })


class Person(ConfiguredBaseModel):
    """
    A contact on the study. personId is a surrogate: md5(studyId, personName, personEmail).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'parquet_file': {'tag': 'parquet_file',
                                          'value': 'Person.parquet'},
                         'rows_in_current_data': {'tag': 'rows_in_current_data',
                                                  'value': 2}},
         'from_schema': 'https://w3id.org/ornl/miappe-gold'})

    studyId: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Study',
                       'Person',
                       'Environment',
                       'DataFile',
                       'Event',
                       'BiologicalMaterial',
                       'ObservationUnit',
                       'ObservedVariable',
                       'Observation',
                       'Image']} })
    personName: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Person']} })
    personEmail: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Null in 1 of 2 rows (50.0%).'], 'domain_of': ['Person']} })
    personId: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Person']} })
    personRole: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Person']} })
    personAffiliation: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Person']} })


class Environment(ConfiguredBaseModel):
    """
    A study-wide environment parameter, stored as a name/value pair.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'parquet_file': {'tag': 'parquet_file',
                                          'value': 'Environment.parquet'},
                         'rows_in_current_data': {'tag': 'rows_in_current_data',
                                                  'value': 2}},
         'from_schema': 'https://w3id.org/ornl/miappe-gold',
         'unique_keys': {'environment_key': {'unique_key_name': 'environment_key',
                                             'unique_key_slots': ['studyId',
                                                                  'envParam']}}})

    studyId: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Study',
                       'Person',
                       'Environment',
                       'DataFile',
                       'Event',
                       'BiologicalMaterial',
                       'ObservationUnit',
                       'ObservedVariable',
                       'Observation',
                       'Image']} })
    envParam: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Environment']} })
    envParamValue: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Environment']} })


class DataFile(ConfiguredBaseModel):
    """
    A source file the study was loaded from.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'parquet_file': {'tag': 'parquet_file',
                                          'value': 'Data_files.parquet'},
                         'rows_in_current_data': {'tag': 'rows_in_current_data',
                                                  'value': 2}},
         'from_schema': 'https://w3id.org/ornl/miappe-gold',
         'unique_keys': {'data_file_key': {'unique_key_name': 'data_file_key',
                                           'unique_key_slots': ['studyId',
                                                                'dataFileLink']}}})

    studyId: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Study',
                       'Person',
                       'Environment',
                       'DataFile',
                       'Event',
                       'BiologicalMaterial',
                       'ObservationUnit',
                       'ObservedVariable',
                       'Observation',
                       'Image']} })
    dataFileLink: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['DataFile']} })
    dataFileDesc: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['DataFile']} })
    dataFileVersion: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 2 rows; Parquet defaulted the type to '
                      'string. A MIAPPE slot this study never filled.'],
         'domain_of': ['DataFile']} })


class Event(ConfiguredBaseModel):
    """
    A dated event applied to the study, e.g. a phenotyping session. eventId is a surrogate: md5(studyId, eventType, eventDate).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'parquet_file': {'tag': 'parquet_file',
                                          'value': 'Event.parquet'},
                         'rows_in_current_data': {'tag': 'rows_in_current_data',
                                                  'value': 44}},
         'from_schema': 'https://w3id.org/ornl/miappe-gold'})

    eventId: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Event']} })
    studyId: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Study',
                       'Person',
                       'Environment',
                       'DataFile',
                       'Event',
                       'BiologicalMaterial',
                       'ObservationUnit',
                       'ObservedVariable',
                       'Observation',
                       'Image']} })
    obsUnitId: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 44 rows; Parquet defaulted the type to '
                      'int32. A MIAPPE slot this study never filled.',
                      'Named like a foreign key but never populated and not covered by '
                      'a schema.yml relationship test, so it is left as a plain scalar '
                      'here.'],
         'domain_of': ['Event', 'ObservationUnit', 'Sample', 'Observation', 'Image']} })
    eventType: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Event']} })
    eventAccNumber: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 44 rows; Parquet defaulted the type to '
                      'string. A MIAPPE slot this study never filled.'],
         'domain_of': ['Event']} })
    eventDesc: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Event']} })
    eventDate: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Event']} })


class BiologicalMaterial(ConfiguredBaseModel):
    """
    The genotype or accession an observation unit is grown from.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'parquet_file': {'tag': 'parquet_file',
                                          'value': 'Biological_material.parquet'},
                         'rows_in_current_data': {'tag': 'rows_in_current_data',
                                                  'value': 510}},
         'from_schema': 'https://w3id.org/ornl/miappe-gold'})

    studyId: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Study',
                       'Person',
                       'Environment',
                       'DataFile',
                       'Event',
                       'BiologicalMaterial',
                       'ObservationUnit',
                       'ObservedVariable',
                       'Observation',
                       'Image']} })
    biologicalMaterialId: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BiologicalMaterial', 'ObservationUnit']} })
    biologicalMaterialExtId: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BiologicalMaterial']} })
    organism: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BiologicalMaterial']} })
    genus: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BiologicalMaterial']} })
    species: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BiologicalMaterial']} })
    infraspecificName: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BiologicalMaterial']} })
    biologicalMaterialLatitude: Optional[float] = Field(default=None, description="""Latitude of the wild collection site, not the growth site.""", json_schema_extra = { "linkml_meta": {'comments': ['Null in 65 of 510 rows (12.7%).'],
         'domain_of': ['BiologicalMaterial']} })
    biologicalMaterialLongitude: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Null in 65 of 510 rows (12.7%).'],
         'domain_of': ['BiologicalMaterial']} })
    biologicalMaterialAltitude: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 510 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['BiologicalMaterial']} })
    biologicalMaterialCoordUncertainty: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 510 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['BiologicalMaterial']} })
    biologicalMaterialPreprocessing: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 510 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['BiologicalMaterial']} })
    materialSourceId: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 510 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['BiologicalMaterial']} })
    materialSourceDoi: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 510 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['BiologicalMaterial']} })
    materialSourceAccNumber: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 510 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['BiologicalMaterial']} })
    materialSourceAccName: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 510 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['BiologicalMaterial']} })
    materialSourceInstCode: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 510 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['BiologicalMaterial']} })
    materialSourceInstName: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 510 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['BiologicalMaterial']} })
    materialSourceOtherIds: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 510 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['BiologicalMaterial']} })
    materialSourceLatitude: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 510 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['BiologicalMaterial']} })
    materialSourceLongitude: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 510 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['BiologicalMaterial']} })
    materialSourceAltitude: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 510 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['BiologicalMaterial']} })
    materialSourceCoordUncertainty: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 510 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['BiologicalMaterial']} })
    materialSourceDesc: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 510 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['BiologicalMaterial']} })


class ObservationUnit(ConfiguredBaseModel):
    """
    The thing observed - here an individual plant. The grain every fact resolves to.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'parquet_file': {'tag': 'parquet_file',
                                          'value': 'Observation_Unit.parquet'},
                         'rows_in_current_data': {'tag': 'rows_in_current_data',
                                                  'value': 519}},
         'from_schema': 'https://w3id.org/ornl/miappe-gold'})

    studyId: str = Field(default=..., description="""Denormalised for filtering - also derivable via biologicalMaterialId.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study',
                       'Person',
                       'Environment',
                       'DataFile',
                       'Event',
                       'BiologicalMaterial',
                       'ObservationUnit',
                       'ObservedVariable',
                       'Observation',
                       'Image']} })
    obsUnitId: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Event', 'ObservationUnit', 'Sample', 'Observation', 'Image']} })
    biologicalMaterialId: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BiologicalMaterial', 'ObservationUnit']} })
    obsUnitType: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ObservationUnit']} })
    externalId: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ObservationUnit', 'Sample']} })
    spatialDistribution: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 519 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['ObservationUnit']} })
    obsUnitFactorValue: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 519 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['ObservationUnit']} })


class Sample(ConfiguredBaseModel):
    """
    Tissue taken from an observation unit on a date (leaf, stem, whole plant).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'parquet_file': {'tag': 'parquet_file',
                                          'value': 'Sample.parquet'},
                         'rows_in_current_data': {'tag': 'rows_in_current_data',
                                                  'value': 1491}},
         'from_schema': 'https://w3id.org/ornl/miappe-gold'})

    obsUnitId: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Event', 'ObservationUnit', 'Sample', 'Observation', 'Image']} })
    sampleId: str = Field(default=..., description="""Encodes its own lineage: SAMPLE-<obsUnitId>-<collectionDate>-<L|S|WP>.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Observation', 'Image']} })
    developmentStage: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 1491 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['Sample']} })
    anatomicalEntity: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    sampleDesc: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    collectionDate: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    externalId: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 1491 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['ObservationUnit', 'Sample']} })


class ObservedVariable(ConfiguredBaseModel):
    """
    A measured variable: trait + method + scale. Joined by every observation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'parquet_file': {'tag': 'parquet_file',
                                          'value': 'Observed_variable.parquet'},
                         'rows_in_current_data': {'tag': 'rows_in_current_data',
                                                  'value': 109}},
         'from_schema': 'https://w3id.org/ornl/miappe-gold'})

    studyId: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Study',
                       'Person',
                       'Environment',
                       'DataFile',
                       'Event',
                       'BiologicalMaterial',
                       'ObservationUnit',
                       'ObservedVariable',
                       'Observation',
                       'Image']} })
    variableId: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ObservedVariable', 'Observation']} })
    variableName: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ObservedVariable']} })
    variableAccNumber: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 109 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['ObservedVariable']} })
    traitName: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Null in 98 of 109 rows (89.9%).'],
         'domain_of': ['ObservedVariable']} })
    traitEntity: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ObservedVariable']} })
    traitEntityAccessionNumber: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ObservedVariable']} })
    traitCharacteristic: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Null in 98 of 109 rows (89.9%).'],
         'domain_of': ['ObservedVariable']} })
    traitCharacteristicAccessionNumber: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Null in 107 of 109 rows (98.2%).'],
         'domain_of': ['ObservedVariable']} })
    traitAccNumber: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 109 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['ObservedVariable']} })
    methodName: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ObservedVariable']} })
    methodAccNumber: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 109 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['ObservedVariable']} })
    methodDesc: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ObservedVariable']} })
    methodRef: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 109 rows; Parquet defaulted the type '
                      'to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['ObservedVariable']} })
    scaleName: Optional[str] = Field(default=None, description="""The unit, as free text: mm, g, cm2, umol m-2 s-1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ObservedVariable']} })
    scaleAccNumber: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Null in 107 of 109 rows (98.2%).'],
         'domain_of': ['ObservedVariable']} })
    timeScale: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Null in 107 of 109 rows (98.2%).'],
         'domain_of': ['ObservedVariable']} })


class Observation(ConfiguredBaseModel):
    """
    A single measured value. observationId is a surrogate: md5(obsUnitId, variableId, observationTimestamp).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'parquet_file': {'tag': 'parquet_file',
                                          'value': 'Observation.parquet'},
                         'rows_in_current_data': {'tag': 'rows_in_current_data',
                                                  'value': 420858}},
         'from_schema': 'https://w3id.org/ornl/miappe-gold'})

    observationId: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Observation']} })
    studyId: str = Field(default=..., description="""Denormalised for filtering - also derivable via obsUnitId.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study',
                       'Person',
                       'Environment',
                       'DataFile',
                       'Event',
                       'BiologicalMaterial',
                       'ObservationUnit',
                       'ObservedVariable',
                       'Observation',
                       'Image']} })
    obsUnitId: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Event', 'ObservationUnit', 'Sample', 'Observation', 'Image']} })
    sampleId: Optional[str] = Field(default=None, description="""Set only for point-measurement traits that need the tissue; null when the trait is measured on the whole plant.""", json_schema_extra = { "linkml_meta": {'comments': ['Null in 416409 of 420858 rows (98.9%).'],
         'domain_of': ['Sample', 'Observation', 'Image']} })
    observationTimestamp: Optional[datetime ] = Field(default=None, description="""A true timestamp, unlike the string form used by Image.observationTimestamp.""", json_schema_extra = { "linkml_meta": {'comments': ['Timezone-naive in Parquet (timestamp[ns], tz=None). '
                      'xsd:dateTime and JSON Schema date-time both want an RFC3339 '
                      'offset, so an exporter has to assign one explicitly - the zone '
                      'is genuinely absent from the data, do not silently assume UTC.'],
         'domain_of': ['Observation', 'Image']} })
    variableId: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ObservedVariable', 'Observation']} })
    observationValue: Optional[float] = Field(default=None, description="""The measured value. Its unit is Observed_variable.scaleName, not stored here.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Observation']} })
    replicate: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 420858 rows; Parquet defaulted the '
                      'type to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['Observation']} })
    qualityFlag: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 420858 rows; Parquet defaulted the '
                      'type to string. A MIAPPE slot this study never filled.'],
         'domain_of': ['Observation']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Observation', 'Image']} })


class Image(ConfiguredBaseModel):
    """
    One image-pipeline artifact: a raw frame, mask, header or analysis output. imageId is a surrogate: md5 of all business columns.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'parquet_file': {'tag': 'parquet_file',
                                          'value': 'Images.parquet'},
                         'rows_in_current_data': {'tag': 'rows_in_current_data',
                                                  'value': 552674}},
         'from_schema': 'https://w3id.org/ornl/miappe-gold'})

    imageId: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    studyId: str = Field(default=..., description="""Denormalised for filtering - also derivable via obsUnitId.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study',
                       'Person',
                       'Environment',
                       'DataFile',
                       'Event',
                       'BiologicalMaterial',
                       'ObservationUnit',
                       'ObservedVariable',
                       'Observation',
                       'Image']} })
    obsUnitId: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Event', 'ObservationUnit', 'Sample', 'Observation', 'Image']} })
    sampleId: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'comments': ['Entirely null across all 552674 rows; Parquet defaulted the '
                      'type to string. A MIAPPE slot this study never filled.',
                      'Named like a foreign key but never populated and not covered by '
                      'a schema.yml relationship test, so it is left as a plain scalar '
                      'here.'],
         'domain_of': ['Sample', 'Observation', 'Image']} })
    observationTimestamp: Optional[str] = Field(default=None, description="""Stored as a US-format string, e.g. '4/15/24 6:55'. Not the timestamp type Observation uses - normalise before joining the two on time.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Observation', 'Image']} })
    Modality: Optional[str] = Field(default=None, description="""Sensor that produced the artifact: FC1, FC2, VNIR, SWIR, MSC1, IR1, RGB1, RGB2, S3D. Capitalised to match the Parquet column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    fileType: Optional[str] = Field(default=None, description="""Artifact kind within a modality, e.g. Image, Mask, Analysis, Protocol, Image Data Header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    filePath: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Image']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Observation', 'Image']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
GoldLayer.model_rebuild()
Investigation.model_rebuild()
Study.model_rebuild()
Person.model_rebuild()
Environment.model_rebuild()
DataFile.model_rebuild()
Event.model_rebuild()
BiologicalMaterial.model_rebuild()
ObservationUnit.model_rebuild()
Sample.model_rebuild()
ObservedVariable.model_rebuild()
Observation.model_rebuild()
Image.model_rebuild()
