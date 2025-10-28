import pyodbc;
import sys;
import flask;
import json;
import jwt;

print(__name__);
app = flask.Flask(__name__);

class Conexion:
    cadena_conexion: str = """
        Driver={MySQL ODBC 9.0 Unicode Driver};
        Server=localhost;
        Database=db_personas;
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

            contador = 0;
            for elemento in cursor:
                temporal: dict = { };
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

@app.route('/main3/Token/<string:entrada>', methods=["GET"])
def Token(entrada: str) -> str :
    respuesta: dict = {};
    try:
        entrada = entrada.replace("'", '"');
        respuesta = json.loads(entrada);
        print(respuesta);

        if not "Usuario" in respuesta.keys():        
            respuesta["Error"] = "Falta informacion";
            return flask.jsonify(respuesta);
        # Recordar validar que exista el usuario

        key = "JHgjhge73465789345";
        respuesta["Llave"] = jwt.encode({"Token": "Hghjg384759gdjh"}, key, algorithm="HS256");
        # Recordar cambiar como se crean los tokens
        respuesta["Respuesta"] = "OK";
        return flask.jsonify(respuesta);
    except Exception as ex:
        respuesta["Error"] = str(ex);
        respuesta["Respuesta"] = "Error";
        return flask.jsonify(respuesta);

@app.route('/main3/CargarEstados/<string:entrada>', methods=["GET"])
def CargarEstados(entrada: str) -> str :
    respuesta: dict = {};
    try:
        entrada = entrada.replace("'", '"');
        respuesta = json.loads(entrada);

        conexion: Conexion = Conexion();
        respuesta["Entidades"] = conexion.CargarEstados();
        respuesta["Respuesta"] = "OK";
        return flask.jsonify(respuesta);
    except Exception as ex:
        respuesta["Error"] = str(ex);
        respuesta["Respuesta"] = "Error";
        return flask.jsonify(respuesta);

app.run('localhost', 4040);

"""
py -m pip install pyodbc
py -m pip install Flask
py -m pip install jsonify
"""