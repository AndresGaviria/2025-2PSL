import pyodbc;

class Conexion:
    cadena_conexion: str = """
        Driver={MySQL ODBC 9.0 Unicode Driver};
        Server=localhost;
        Database=db_universidad;
        PORT=3306;
        user=user_ptyhon;
        password=Clas3s1Nt2024_!""";

    def CargarEstados(self) -> dict:
        conexion = pyodbc.connect(self.cadena_conexion);

        consulta: str = """ SELECT * FROM estados; """;
        cursor = conexion.cursor();
        cursor.execute(consulta);

        respuesta: dict = {};
        contador: int = 0;
        for elemento in cursor:
            tempotal: dict = {};
            tempotal["Id"] = elemento[0];
            tempotal["Nombre"] = elemento[1];
            
            respuesta[str(contador)] = tempotal;
            contador = contador + 1;

        cursor.close();
        conexion.close();

        return respuesta;

conexion = Conexion();
conexion.CargarEstados();


"""
py -m pip install pyodbc
py -m pip install Flask
py -m pip install jsonify
"""