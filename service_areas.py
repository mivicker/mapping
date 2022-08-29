from pathlib import Path
from tableauhyperapi import (
    HyperProcess, 
    Telemetry, 
    Connection, 
    CreateMode, 
    DatabaseName,
    TableName,
)
import pantab

base_path = (
        Path.home() / 
        "projects" / 
        "gleaners" / 
        "census" /
        "Service Areas 12-02-2020" /
        "Data"
    )

path = base_path / "Service Areas 2019-12-17 - Copy.twb Files" / "federated.hyper"

with HyperProcess(telemetry=Telemetry.DO_NOT_SEND_USAGE_DATA_TO_TABLEAU) as hyper:
    with Connection(hyper.endpoint, path) as connection:
        result = connection.catalog.get_schema_names()
        table_name = connection.catalog.get_table_names(result[0])[0]

df = pantab.frame_from_hyper(path, table=table_name)
print(df.columns)

path = base_path / "TableauTemp" / "TEMP_1we6e6w0sz1uab16yyird12t8707.hyper"

with HyperProcess(telemetry=Telemetry.DO_NOT_SEND_USAGE_DATA_TO_TABLEAU) as hyper:
    with Connection(hyper.endpoint, path) as connection:
        result = connection.catalog.get_schema_names()
        table_name = connection.catalog.get_table_names(result[0])[0]

        result = connection.execute_query(query=f"SELECT * from {table_name}")
        print(result)

df = pantab.frame_from_hyper(path, table=table_name)
for item in df.iloc[0].index:
    print(item)
