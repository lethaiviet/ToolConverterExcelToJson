::https://github.com/pyexcel/pyexcel-io/blob/master/docs/source/pyinstaller.rst

call pyinstaller --onefile ^
--hidden-import pyexcel_io.readers.csv_in_file ^
--hidden-import pyexcel_io.readers.csv_in_memory ^
--hidden-import pyexcel_io.readers.csv_content ^
--hidden-import pyexcel_io.readers.csvz ^
--hidden-import pyexcel_io.writers.csv_in_file ^
--hidden-import pyexcel_io.writers.csv_in_memory ^
--hidden-import pyexcel_io.writers.csvz_writer ^
--hidden-import pyexcel_io.database.importers.django ^
--hidden-import pyexcel_io.database.importers.sqlalchemy ^
--hidden-import pyexcel_io.database.exporters.django ^
--hidden-import pyexcel_io.database.exporters.sqlalchemy ^
ConverterExcelAndJson.py