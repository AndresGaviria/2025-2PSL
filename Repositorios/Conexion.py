import pyodbc;
from Entidades import Estados;

class Conexion:
    cadena_conexion: str = """
        Driver={MySQL ODBC 9.0 Unicode Driver};
        Server=localhost;
        Database=db_universidad;
        PORT=3306;
        user=user_ptyhon;
        password=Clas3s1Nt2024_!""";

    def CargarEstados(self) -> None:
        conexion = pyodbc.connect(self.cadena_conexion);

        consulta: str = """ {CALL proc_select_estados();} """;
        cursor = conexion.cursor();
        cursor.execute(consulta);

        lista: list = [];
        for elemento in cursor:
            entidad: Estados.Estados = Estados.Estados();
            entidad.SetId(elemento[0]);
            entidad.SetNombre(elemento[1]);
            lista.append(entidad);

        cursor.close();
        conexion.close();

        for estado in lista:
            print(str(estado.GetId()) + ", " + estado.GetNombre());