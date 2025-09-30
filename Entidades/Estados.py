class Estados:
    id: int = 0;

    def GetId(self) -> int:
        return self.id;
    def SetId(self, value: int) -> None:
        self.id = value;

    nombre: str = None;

    def GetNombre(self) -> str:
        return self.nombre;
    def SetNombre(self, value: str) -> None:
        self.nombre = value;