from typing import Any, Dict
from pystac import Provider, ProviderRole
from pystac.utils import str_to_datetime

COLLECTION_ID = "nalcms"
COLLECTION_EPSG = 3978
COLLECTION_TITLE = "North American Land Change Monitoring System data"
COLLECTION_LICENSE = "proprietary"

COLLECTION_DESCRIPTION = (
    "NALCMS products can be used for a variety of applications, including:"
    " carbon sequestration analysis, wildlife habitat mapping, ecosystem"
    " monitoring, environmental planning, water quality assessments, and"
    " evaluation of biofuels production potential.The maps produced under this"
    " initiative represent land cover in 2005, 2010, and 2015, & are based on"
    " either Moderate Resolution Imaging Spectroradiometer (MODIS) satellite"
    " imagery monthly composites at 250 m spatial resolution; Landsat-7; or"
    " RapidEye satellite imagery at 30 m spatial resolution. The NALCMS’"
    " nineteen land cover classes are based on the Land Cover Classification"
    " System (LCCS) standard developed by the Food & Agriculture Organization"
    " (FAO) of the United Nations.")
# [xmin, ymin, xmax, ymax]]
# [west, east, noth, south]
# SPATIAL_EXTENT = [-170.0, -50.0, 84.0, 14.0]
TEMPORAL_EXTENT = [
    str_to_datetime("2005, 1, 1"),
    None,
]

NRCAN_PROVIDER = Provider(
    name=("Natural Resources Canada | Ressources naturelles Canada / Canada"
          " Centre Mapping and Earth Observation | Centre Canadien de"
          " cartographie et d’observation de la terre"),
    roles=[ProviderRole.PRODUCER, ProviderRole.PROCESSOR],
    url="https://www.nrcan.gc.ca",
)

INEGI_PROVIDER = Provider(
    name="Instituto Nacional de Estadística y Geografía",
    roles=[ProviderRole.PRODUCER, ProviderRole.PROCESSOR],
    url="https://www.inegi.org.mx/",
)

CONAFOR_PROVIDER = Provider(
    name="Comisión Nacional Forestal",
    roles=[ProviderRole.PRODUCER, ProviderRole.PROCESSOR],
    url="https://www.gob.mx/conafor",
)

USGS_PROVIDER = Provider(
    name="U.S. Geological Survey",
    roles=[ProviderRole.PRODUCER, ProviderRole.PROCESSOR],
    url="https://www.usgs.gov",
)

CEC_PROVIDER = Provider(
    name="Commission for Environmental Cooperation",
    roles=[ProviderRole.PRODUCER, ProviderRole.PROCESSOR],
    url="http://www.cec.org/north-american-environmental-atlas/",
)

GSDS = [30, 250]

YEARS = {"30": ["2010", "2015", "2010-2015"], "250": ["2005", "2010", "2005-2010"]}

REGIONS = {
    "CAN": "Canada",
    "USA": "United States of America",
    "MEX": "Mexico",
    "NA": "North America",
    "ASK": "Alaska",
    "HI": "Hawaii",
}

HREF_DIR = ("http://www.cec.org/wp-content/uploads/wpallimport/files/Atlas/Files/")

HREFS_ZIP = {
    "30m_2010-2015_CAN": "land_cover_30m_2010-2015_landsat/lcchange_canada_2010_2015.zip",
    "30m_2010-2015_MEX": "land_cover_30m_2010-2015_landsat/lcchange_mexico_2010_2015.zip",
    "30m_2010-2015_NA": "land_cover_30m_2010-2015_landsat/lcchange_north_america_2010_2015.zip",
    "30m_2010-2015_USA": "land_cover_30m_2010-2015_landsat/lcchange_united_states_2010_2015.zip",
    "30m_2010-2015_ASK": "land_cover_30m_2010-2015_landsat/lcchange_united_states_2010_2015.zip",
    "30m_2015_CAN": "2010nalcms30m/canada_2015_v2.zip",
    "30m_2015_MEX": "2010nalcms30m/mexico_2015_v2.zip",
    "30m_2015_NA": "2010nalcms30m/north_america_2015_v2.zip",
    "30m_2015_USA": "2010nalcms30m/united_states_2015_v2.zip",
    "30m_2015_ASK": "2010nalcms30m/united_states_2015_v2.zip",
    "30m_2010_CAN": "2010nalcms30m/canada_2010.zip",
    "30m_2010_MEX": "2010nalcms30m/mexico_2010.zip",
    "30m_2010_NA": "2010nalcms30m/north_america_2010.zip",
    "30m_2010_USA": "2010nalcms30m/united_states_2010.zip",
    "30m_2010_ASK": "2010nalcms30m/united_states_2010.zip",
    "250m_2005-2010_NA": "Land_Cover_05_10/LC_05-10_change_TIFF.zip",
    "250m_2010_NA": "Land_Cover_2010/Land_Cover_2010v2_TIFF.zip",
    # "250m_2010_HI": "Land_Cover_2010/Land_Cover_2010v2_TIFF.zip",
    "250m_2005_NA": "Land_Cover_2005/Land_Cover_2005v3_TIFF.zip",
    "250m_2005_HI": "Land_Cover_2005/Land_Cover_2005v3_TIFF.zip",
}

HREFS_METADATA = {
    "30m_2010-2015": "land_cover_30m_2010-2015_landsat/metadata_nalcms_2010_2015_30m.doc",
    "30m_2015": "2010nalcms30m/nalcms_2015_30m_metadata_v2.doc",
    "30m_2010": "2010nalcms30m/nalcms_2010_30m_metadata.doc",
    "250m_2005-2010": "Land_Cover_05_10/Metadata_NALCMS_2005_2010.doc",
    "250m_2010": "Land_Cover_2010/Metadata_NALCMS_2010v2.doc",
    "250m_2005": "Land_Cover_2005/Metadata_NALCMS_2005_v3.doc",
}

PROJECTIONS: Dict[str, Any] = {
    "30m_2010-2015_NA": {
        "epsg":
        None,
        "wkt": ('PROJCS[\"WGS_1984_Lambert_Azimuthal_Equal_Area\",GEOGCS[\"WGS'
                ' 84\",DATUM[\"WGS_1984\",SPHEROID[\"WGS'
                ' 84\",6378137,298.257223563,AUTHORITY[\"EPSG\",\"7030\"]],'
                'AUTHORITY[\"EPSG\",\"6326\"]],PRIMEM[\"Greenwich\",0],UNIT'
                '[\"degree\",0.0174532925199433,AUTHORITY[\"EPSG\",\"9122\"]]'
                ',AUTHORITY[\"EPSG\",\"4326\"]],PROJECTION[\"Lambert_Azimuthal_'
                'Equal_Area\"],PARAMETER[\"latitude_of_center\",45],PARAMETER[\"'
                'longitude_of_center\",-100],PARAMETER[\"false_easting\",0],'
                'PARAMETER[\"false_northing\",0],UNIT[\"metre\",1],AXIS[\"Easting'
                '\",EAST],AXIS[\"Northing\",NORTH]]'),
        "transform": [30.0, 0.0, -4410000.000000002, 0.0, -30.0, 4309999.999999999, 0.0, 0.0, 1.0],
        "bounds": [-4410000.000000002, -3340000.000000001, 3345089.999999998, 4309999.999999999],
        "shape": [255000, 258503]
    },
    "30m_2010-2015_USA": {
        "epsg":
        None,
        "shape": (94832, 152022),
        "wkt": (
            'PROJCS["WGS_1984_Lambert_Azimuthal_Equal_Area",GEOGCS["WGS'
            ' 84",DATUM["WGS_1984",SPHEROID["WGS'
            ' 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]],PROJECTION["Lambert_Azimuthal_Equal_Area"],PARAMETER["latitude_of_center",45],PARAMETER["longitude_of_center",-100],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1],AXIS["Easting",EAST],AXIS["Northing",NORTH]]'  # noqa
        ),
        "transform": [
            30.0,
            0.0,
            -2036970.0000000019,
            0.0,
            -30.0,
            732169.9999999991,
            0.0,
            0.0,
            1.0,
        ],
        "bounds": [
            -2036970.0000000019,
            -2112790.000000001,
            2523689.999999998,
            732169.9999999991,
        ],
    },
    "30m_2010-2015_MEX": {
        "epsg":
        None,
        "shape": (69426, 106596),
        "wkt": (
            'PROJCS["WGS_1984_Lambert_Azimuthal_Equal_Area",GEOGCS["WGS'
            ' 84",DATUM["WGS_1984",SPHEROID["WGS'
            ' 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]],PROJECTION["Lambert_Azimuthal_Equal_Area"],PARAMETER["latitude_of_center",45],PARAMETER["longitude_of_center",-100],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1],AXIS["Easting",EAST],AXIS["Northing",NORTH]]'  # noqa
        ),
        "transform": [
            30.0,
            0.0,
            -1788570.0000000019,
            0.0,
            -30.0,
            -1220380.000000001,
            0.0,
            0.0,
            1.0,
        ],
        "bounds": [
            -1788570.0000000019,
            -3303160.000000001,
            1409309.9999999981,
            -1220380.000000001,
        ],
    },
    "250m_2005-2010_NA": {
        "epsg": None,
        "shape": (35000, 37000),
        "wkt":
        'PROJCS["Sphere_ARC_INFO_Lambert_Azimuthal_Equal_Area",GEOGCS["GCS_Sphere_ARC_INFO",DATUM["Sphere_ARC_INFO",SPHEROID["Sphere_ARC_INFO",6370997,0]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]]],PROJECTION["Lambert_Azimuthal_Equal_Area"],PARAMETER["latitude_of_center",45],PARAMETER["longitude_of_center",-100],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1],AXIS["Easting",EAST],AXIS["Northing",NORTH]]',  # noqa
        "transform": [250.0, 0.0, -4418000.0, 0.0, -250.0, 4876500.0, 0.0, 0.0, 1.0],
        "bounds": [-4418000.0, -3873500.0, 4832000.0, 4876500.0],
    },
    "30m_2015_NA": {
        "epsg":
        None,
        "shape": (255000, 259000),
        "wkt": (
            'PROJCS["WGS_1984_Lambert_Azimuthal_Equal_Area",GEOGCS["WGS'
            ' 84",DATUM["WGS_1984",SPHEROID["WGS'
            ' 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]],PROJECTION["Lambert_Azimuthal_Equal_Area"],PARAMETER["latitude_of_center",45],PARAMETER["longitude_of_center",-100],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1],AXIS["Easting",EAST],AXIS["Northing",NORTH]]'  # noqa
        ),
        "transform": [
            30.0,
            0.0,
            -4410000.0,
            0.0,
            -30.0,
            4310000.000000002,
            0.0,
            0.0,
            1.0,
        ],
        "bounds": [-4410000.0, -3339999.999999998, 3360000.0, 4310000.000000002],
    },
    "30m_2010_CAN": {
        "epsg":
        None,
        "shape": (152010, 188680),
        "wkt": (
            'PROJCS["WGS_1984_Lambert_Azimuthal_Equal_Area",GEOGCS["WGS'
            ' 84",DATUM["WGS_1984",SPHEROID["WGS'
            ' 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]],PROJECTION["Lambert_Azimuthal_Equal_Area"],PARAMETER["latitude_of_center",45],PARAMETER["longitude_of_center",-100],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1],AXIS["Easting",EAST],AXIS["Northing",NORTH]]'  # noqa
        ),
        "transform": [
            30.0,
            0.0,
            -2315310.0000000037,
            0.0,
            -30.0,
            4309999.999999997,
            0.0,
            0.0,
            1.0,
        ],
        "bounds": [
            -2315310.0000000037,
            -250300.0000000028,
            3345089.9999999963,
            4309999.999999997,
        ],
    },
    "30m_2015_USA": {
        "epsg":
        None,
        "shape": (94853, 152422),
        "wkt": (
            'PROJCS["WGS_1984_Lambert_Azimuthal_Equal_Area",GEOGCS["WGS'
            ' 84",DATUM["WGS_1984",SPHEROID["WGS'
            ' 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]],PROJECTION["Lambert_Azimuthal_Equal_Area"],PARAMETER["latitude_of_center",45],PARAMETER["longitude_of_center",-100],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1],AXIS["Easting",EAST],AXIS["Northing",NORTH]]'  # noqa
        ),
        "transform": [30.0, 0.0, -2043060.0, 0.0, -30.0, 732440.0, 0.0, 0.0, 1.0],
        "bounds": [-2043060.0, -2113150.0, 2529600.0, 732440.0],
    },
    "250m_2005_HI": {
        "epsg": None,
        "shape": (2746, 2747),
        "wkt":
        'PROJCS["Sphere_ARC_INFO_Lambert_Azimuthal_Equal_Area",GEOGCS["GCS_Sphere_ARC_INFO",DATUM["D_Sphere_ARC_INFO",SPHEROID["Sphere_ARC_INFO",6370997,0]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]]],PROJECTION["Lambert_Azimuthal_Equal_Area"],PARAMETER["latitude_of_center",45],PARAMETER["longitude_of_center",-100],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1],AXIS["Easting",EAST],AXIS["Northing",NORTH]]',  # noqa
        "transform": [
            250.0,
            0.0,
            -5907538.59,
            0.0,
            -250.0,
            -408235.45999999996,
            0.0,
            0.0,
            1.0,
        ],
        "bounds": [-5907538.59, -1094735.46, -5220788.59, -408235.45999999996],
    },
    "250m_2005_NA": {
        "epsg": None,
        "shape": (35000, 37000),
        "wkt":
        'PROJCS["Sphere_ARC_INFO_Lambert_Azimuthal_Equal_Area",GEOGCS["GCS_Sphere_ARC_INFO",DATUM["D_Sphere_ARC_INFO",SPHEROID["Sphere_ARC_INFO",6370997,0]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]]],PROJECTION["Lambert_Azimuthal_Equal_Area"],PARAMETER["latitude_of_center",45],PARAMETER["longitude_of_center",-100],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1],AXIS["Easting",EAST],AXIS["Northing",NORTH]]',  # noqa
        "transform": [250.0, 0.0, -4418000.0, 0.0, -250.0, 4876500.0, 0.0, 0.0, 1.0],
        "bounds": [-4418000.0, -3873500.0, 4832000.0, 4876500.0],
    },
    "30m_2010_NA": {
        "epsg":
        None,
        "shape": (255000, 259000),
        "wkt": (
            'PROJCS["WGS_1984_Lambert_Azimuthal_Equal_Area",GEOGCS["WGS'
            ' 84",DATUM["WGS_1984",SPHEROID["WGS'
            ' 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]],PROJECTION["Lambert_Azimuthal_Equal_Area"],PARAMETER["latitude_of_center",45],PARAMETER["longitude_of_center",-100],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1],AXIS["Easting",EAST],AXIS["Northing",NORTH]]'  # noqa
        ),
        "transform": [
            30.0,
            0.0,
            -4410000.0,
            0.0,
            -30.0,
            4310000.000000002,
            0.0,
            0.0,
            1.0,
        ],
        "bounds": [-4410000.0, -3339999.999999998, 3360000.0, 4310000.000000002],
    },
    "30m_2010_ASK": {
        "epsg":
        None,
        "shape": (95217, 96771),
        "wkt": (
            'PROJCS["WGS_1984_Lambert_Azimuthal_Equal_Area",GEOGCS["WGS'
            ' 84",DATUM["WGS_1984",SPHEROID["WGS'
            ' 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]],PROJECTION["Lambert_Azimuthal_Equal_Area"],PARAMETER["latitude_of_center",45],PARAMETER["longitude_of_center",-100],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1],AXIS["Easting",EAST],AXIS["Northing",NORTH]]'  # noqa
        ),
        "transform": [
            30.0,
            0.0,
            -4410000.000000002,
            0.0,
            -30.0,
            4309999.999999999,
            0.0,
            0.0,
            1.0,
        ],
        "bounds": [
            -4410000.000000002,
            1453489.999999999,
            -1506870.0000000019,
            4309999.999999999,
        ],
    },
    "30m_2010_USA": {
        "epsg":
        None,
        "shape": (94853, 152422),
        "wkt": (
            'PROJCS["WGS_1984_Lambert_Azimuthal_Equal_Area",GEOGCS["WGS'
            ' 84",DATUM["WGS_1984",SPHEROID["WGS'
            ' 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]],PROJECTION["Lambert_Azimuthal_Equal_Area"],PARAMETER["latitude_of_center",45],PARAMETER["longitude_of_center",-100],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1],AXIS["Easting",EAST],AXIS["Northing",NORTH]]'  # noqa
        ),
        "transform": [30.0, 0.0, -2043060.0, 0.0, -30.0, 732440.0, 0.0, 0.0, 1.0],
        "bounds": [-2043060.0, -2113150.0, 2529600.0, 732440.0],
    },
    "30m_2010-2015_CAN": {
        "epsg":
        None,
        "shape": (149794, 183005),
        "wkt": (
            'PROJCS["WGS_1984_Lambert_Azimuthal_Equal_Area",GEOGCS["WGS'
            ' 84",DATUM["WGS_1984",SPHEROID["WGS'
            ' 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]],PROJECTION["Lambert_Azimuthal_Equal_Area"],PARAMETER["latitude_of_center",45],PARAMETER["longitude_of_center",-100],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1],AXIS["Easting",EAST],AXIS["Northing",NORTH]]'  # noqa
        ),
        "transform": [
            30.0,
            0.0,
            -2145120.000000002,
            0.0,
            -30.0,
            4275829.999999999,
            0.0,
            0.0,
            1.0,
        ],
        "bounds": [
            -2145120.000000002,
            -217990.00000000093,
            3345029.999999998,
            4275829.999999999,
        ],
    },
    "30m_2015_CAN": {
        "epsg":
        None,
        "shape": (152010, 188680),
        "wkt": (
            'PROJCS["WGS_1984_Lambert_Azimuthal_Equal_Area",GEOGCS["WGS'
            ' 84",DATUM["WGS_1984",SPHEROID["WGS'
            ' 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]],PROJECTION["Lambert_Azimuthal_Equal_Area"],PARAMETER["latitude_of_center",45],PARAMETER["longitude_of_center",-100],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1],AXIS["Easting",EAST],AXIS["Northing",NORTH]]'  # noqa
        ),
        "transform": [
            30.0,
            0.0,
            -2315310.0000000037,
            0.0,
            -30.0,
            4309999.999999997,
            0.0,
            0.0,
            1.0,
        ],
        "bounds": [
            -2315310.0000000037,
            -250300.0000000028,
            3345089.9999999963,
            4309999.999999997,
        ],
    },
    "250m_2010_NA": {
        "epsg": None,
        "shape": (35000, 37000),
        "wkt":
        'PROJCS["Sphere_ARC_INFO_Lambert_Azimuthal_Equal_Area",GEOGCS["GCS_Sphere_ARC_INFO",DATUM["D_Sphere_ARC_INFO",SPHEROID["Sphere_ARC_INFO",6370997,0]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]]],PROJECTION["Lambert_Azimuthal_Equal_Area"],PARAMETER["latitude_of_center",45],PARAMETER["longitude_of_center",-100],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1],AXIS["Easting",EAST],AXIS["Northing",NORTH]]',  # noqa
        "transform": [250.0, 0.0, -4418000.0, 0.0, -250.0, 4876500.0, 0.0, 0.0, 1.0],
        "bounds": [-4418000.0, -3873500.0, 4832000.0, 4876500.0],
    },
    "30m_2010-2015_ASK": {
        "epsg":
        None,
        "shape": (81578, 95265),
        "wkt": (
            'PROJCS["WGS_1984_Lambert_Azimuthal_Equal_Area",GEOGCS["WGS'
            ' 84",DATUM["WGS_1984",SPHEROID["WGS'
            ' 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]],PROJECTION["Lambert_Azimuthal_Equal_Area"],PARAMETER["latitude_of_center",45],PARAMETER["longitude_of_center",-100],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1],AXIS["Easting",EAST],AXIS["Northing",NORTH]]'  # noqa
        ),
        "transform": [
            30.0,
            0.0,
            -4377270.000000002,
            0.0,
            -30.0,
            3913609.999999999,
            0.0,
            0.0,
            1.0,
        ],
        "bounds": [
            -4377270.000000002,
            1466269.999999999,
            -1519320.0000000019,
            3913609.999999999,
        ],
    },
    "30m_2015_ASK": {
        "epsg":
        None,
        "shape": (95217, 96771),
        "wkt": (
            'PROJCS["WGS_1984_Lambert_Azimuthal_Equal_Area",GEOGCS["WGS'
            ' 84",DATUM["WGS_1984",SPHEROID["WGS'
            ' 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]],PROJECTION["Lambert_Azimuthal_Equal_Area"],PARAMETER["latitude_of_center",45],PARAMETER["longitude_of_center",-100],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1],AXIS["Easting",EAST],AXIS["Northing",NORTH]]'  # noqa
        ),
        "transform": [
            30.0,
            0.0,
            -4410000.000000002,
            0.0,
            -30.0,
            4309999.999999999,
            0.0,
            0.0,
            1.0,
        ],
        "bounds": [
            -4410000.000000002,
            1453489.999999999,
            -1506870.0000000019,
            4309999.999999999,
        ],
    },
    "30m_2015_MEX": {
        "epsg":
        None,
        "shape": (70668, 106671),
        "wkt": (
            'PROJCS["WGS_1984_Lambert_Azimuthal_Equal_Area",GEOGCS["WGS'
            ' 84",DATUM["WGS_1984",SPHEROID["WGS'
            ' 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]],PROJECTION["Lambert_Azimuthal_Equal_Area"],PARAMETER["latitude_of_center",45],PARAMETER["longitude_of_center",-100],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1],AXIS["Easting",EAST],AXIS["Northing",NORTH]]'  # noqa
        ),
        "transform": [
            30.0,
            0.0,
            -1789979.9999999984,
            0.0,
            -30.0,
            -1219959.9999999972,
            0.0,
            0.0,
            1.0,
        ],
        "bounds": [
            -1789979.9999999984,
            -3339999.999999997,
            1410150.0000000016,
            -1219959.9999999972,
        ],
    },
    "30m_2010_MEX": {
        "epsg":
        None,
        "shape": (70668, 106671),
        "wkt": (
            'PROJCS["WGS_1984_Lambert_Azimuthal_Equal_Area",GEOGCS["WGS'
            ' 84",DATUM["WGS_1984",SPHEROID["WGS'
            ' 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]],PROJECTION["Lambert_Azimuthal_Equal_Area"],PARAMETER["latitude_of_center",45],PARAMETER["longitude_of_center",-100],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1],AXIS["Easting",EAST],AXIS["Northing",NORTH]]'  # noqa
        ),
        "transform": [
            30.0,
            0.0,
            -1789979.9999999984,
            0.0,
            -30.0,
            -1219959.9999999972,
            0.0,
            0.0,
            1.0,
        ],
        "bounds": [
            -1789979.9999999984,
            -3339999.999999997,
            1410150.0000000016,
            -1219959.9999999972,
        ],
    },
}

SATELLITES: Dict[str, Any] = {
    "MODIS": {
        "platform": ["Terra", "Aqua"],
        "instruments": ["MODIS"],
        "constellation": ["A-Train"],
    },
    "Landsat 7": {
        "platform": ["Landsat 7"],
        "instruments": ["ETM+"],
        "constellation": [],
    },
    "RapidEye": {
        "platform": ["RapidEye"],
        "instruments": ["REIS"],
        "constellation": ["RapidEye"],
    },
}

# [xmin, ymin, xmax, ymax]]
SPATIAL_EXTENTS = {
    '30m_2010-2015_NA':
    [6.039095198218554, -138.80536327065727, 61.779167675145786, -12.078890175164888],
    '30m_2010-2015_USA':
    [23.787483432154772, -119.85104365308925, 46.6224821324055, -65.75528285145232],
    '30m_2010-2015_MEX':
    [13.44506394052848, -115.99718179029607, 32.86560559417034, -84.92776041622263],
    '250m_2005-2010_NA':
    [1.4279751101491476, -137.9896823788992, 48.812750584693504, 4.00508993290567],
    '30m_2015_NA': [6.03909519821859, -138.80536327065724, 61.65521507065405, -11.985214988396194],
    '30m_2010_CAN':
    [39.2533440032893, -127.40853951132385, 61.779167675145786, -12.078890175164927],
    '30m_2015_USA': [23.77189977813217, -119.90865307541915, 46.60242856037363, -65.68212376216307],
    '250m_2005_HI':
    [16.590770667252958, -158.56422527873127, 25.272999705314227, -155.70334942350803],
    '250m_2005_NA': [1.4279751101491476, -137.9896823788992, 48.812750584693504, 4.00508993290567],
    '30m_2010_NA': [6.03909519821859, -138.80536327065724, 61.65521507065405, -11.985214988396194],
    '30m_2010_ASK':
    [42.11500192198557, -160.08863641682973, 76.46819003404057, -169.90718473769746],
    '30m_2010_USA': [23.77189977813217, -119.90865307541915, 46.60242856037363, -65.68212376216307],
    '30m_2010-2015_CAN':
    [40.01133370587668, -125.60914442737285, 61.73055142784825, -12.740986140994792],
    '30m_2015_CAN':
    [39.2533440032893, -127.40853951132385, 61.779167675145786, -12.078890175164927],
    '250m_2010_NA': [1.4279751101491476, -137.9896823788992, 48.812750584693504, 4.00508993290567],
    '30m_2010-2015_ASK':
    [42.39568114622015, -159.8770017408243, 74.52942862431979, -157.1492915384077],
    '30m_2015_ASK':
    [42.11500192198557, -160.08863641682973, 76.46819003404057, -169.90718473769746],
    '30m_2015_MEX':
    [13.102845359730296, -115.97332960180964, 32.86800574186697, -84.91821332299581],
    '30m_2010_MEX': [
        13.102845359730296, -115.97332960180964, 32.86800574186697, -84.91821332299581
    ]
}

KEYWORDS = ["NALCMS", "Landsat 7", "RapidEye", "North America", "MODIS"]

NODATA = {
    '30m_2010-2015_NA': 65535.0,
    '30m_2010-2015_USA': 65535.0,
    '30m_2010-2015_MEX': 65535.0,
    '250m_2005-2010_NA': None,
    '30m_2015_NA': -128.0,
    '30m_2010_CAN': -128.0,
    '30m_2015_USA': -128.0,
    '250m_2005_HI': 128.0,
    '250m_2005_NA': 128.0,
    '30m_2010_NA': 127.0,
    '30m_2010_ASK': -128.0,
    '30m_2010_USA': -128.0,
    '30m_2010-2015_CAN': 65535.0,
    '30m_2015_CAN': -128.0,
    '250m_2010_NA': -128.0,
    '30m_2010-2015_ASK': 65535.0,
    '30m_2015_ASK': 127.0,
    '30m_2015_MEX': -128.0,
    '30m_2010_MEX': -128.0,
}

DATA_TYPE: Any = {
    '30m_2010-2015_NA': 'uint16',
    '30m_2010-2015_USA': 'uint16',
    '30m_2010-2015_MEX': 'uint16',
    '250m_2005-2010_NA': 'uint16',
    '30m_2015_NA': 'int8',
    '30m_2010_CAN': 'int8',
    '30m_2015_USA': 'int8',
    '250m_2005_HI': 'int8',
    '250m_2005_NA': 'int16',
    '30m_2010_NA': 'uint8',
    '30m_2010_ASK': 'int8',
    '30m_2010_USA': 'int8',
    '30m_2010-2015_CAN': 'uint16',
    '30m_2015_CAN': 'int8',
    '250m_2010_NA': 'int8',
    '30m_2010-2015_ASK': 'uint16',
    '30m_2015_ASK': 'int8',
    '30m_2015_MEX': 'int8',
    '30m_2010_MEX': 'int8',
}

VALUES = {
    1: "Temperate or sub-polar needleleaf forest",
    2: "Sub-polar taiga needleleaf forest",
    3: "Tropical or sub-tropical broadleaf evergreen forest",
    4: "Tropical or sub-tropical broadleaf deciduous forest",
    5: "Temperate or sub-polar broadleaf deciduous forest",
    6: "Mixed forest",
    7: "Tropical or sub-tropical shrubland",
    8: "Temperate or sub-polar shrubland",
    9: "Tropical or sub-tropical grassland",
    10: "Temperate or sub-polar grassland",
    11: "Sub-polar or polar shrubland-lichen-moss",
    12: "Sub-polar or polar grassland-lichen-moss",
    13: "Sub-polar or polar barren-lichen-moss",
    14: "Wetland",
    15: "Cropland",
    16: "Barren lands",
    17: "Urban and built-up",
    18: "Water",
    19: "Snow and ice"
}

FILE_SIZES = {
    '30m_2010-2015_NA': 1674800213,
    '30m_2010-2015_USA': 588295657,
    '30m_2010-2015_MEX': 215525299,
    '250m_2005-2010_NA': 2590562610,
    '30m_2015_NA': 3726465138,
    '30m_2010_CAN': 1821927873,
    '30m_2015_USA': 1179569139,
    '250m_2005_HI': 156104,
    '250m_2005_NA': 76020586,
    '30m_2010_NA': 3331040589,
    '30m_2010_ASK': 351824554,
    '30m_2010_USA': 1178611813,
    '30m_2010-2015_CAN': 748896959,
    '30m_2015_CAN': 1835258561,
    '250m_2010_NA': 63973855,
    '30m_2010-2015_ASK': 201486837,
    '30m_2015_ASK': 313294116,
    '30m_2015_MEX': 277298245,
    '30m_2010_MEX': 242651009,
}

DOI = "10.1201/b11964-24"
CITATION = ("Latifovic, Rasim & Homer, Collin & Ressl, Rainer & Pouliot, D.A."
            " & Hossian, S. & Colditz, Rene & Olthof, Ian & Chandra, Giri & Victoria,"
            " Arturo. (2012). North American Land Change Monitoring System. Remote"
            " Sensing of Land Use and Land Cover: Principles and Applications."
            " 303-324. 10.1201/b11964-24.")
