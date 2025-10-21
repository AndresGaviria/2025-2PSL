import pyodbc;
import sys;
import flask;
import json;

print(__name__);
app = flask.Flask(__name__);

class Conexion:
    cadena_conexion: str = """
        Driver={MySQL ODBC 9.0 Unicode Driver};
        Server=localhost;
        Database=db_universidad;
        PORT=3306;
        user=user_ptyhon;
        password=Clas3s1Nt2024_!""";

    def CargarEstados(self) -> dict:
        respuesta: dict = {};
        try:
            conexion = pyodbc.connect(self.cadena_conexion);

            consulta: str = """ SELECT * FROM estados; """;
            cursor = conexion.cursor();
            cursor.execute(consulta);

            contador: int = 0;
            for elemento in cursor:
                temporal: dict = {};
                temporal["Id"] = elemento[0];
                temporal["Nombre"] = elemento[1];
                
                respuesta[str(contador)] = temporal;
                contador = contador + 1;

            cursor.close();
            conexion.close();
            return respuesta;
        except Exception as ex:
            respuesta["Error"] = str(ex);
            return respuesta;

@app.route('/main3/CargarEstados/<string:entrada>', methods=["GET"])
def CargarEstados(entrada: str) -> str :
    return "Hola mundo!";

app.run('localhost', 4040);


"""
py -m pip install pyodbc
py -m pip install Flask
py -m pip install jsonify
"""