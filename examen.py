from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, rfc, apellidos, nombres):
        self._rfc = rfc
        self._apellidos = apellidos
        self._nombres = nombres

    def mostrar_info(self):
        return f"RFC: {self._rfc}, apellidos: {self._apellidos}, nombres: {self._nombres}"
    @abstractmethod
    def ingresos(self):
        pass
class EmpleadoVendedor(Empleado):
    def __init__(self, rfc, apellidos, nombres, monto_vendido, tasa_comision):
        super().__init__(rfc, apellidos, nombres)
        self.monto_vendido = monto_vendido
        self.tasa_comision = tasa_comision
        if monto_vendido < 150:
            raise ValueError("El monto vendido no puede ser menor a 150.")
    def calcular_ingresos(self):
        return self.monto_vendido * self.tasa_comision
#eEste es para la tasa bonificacion
    def calcular_bonificacion(self):
        ingresos = self.calcular_ingresos()
        if self.monto_vendido < 1000:
            return 0
        elif 1000 <= self.monto_vendido <= 5000: #SI ESTA ENTRE 1000 Y 5000 SERA DE 5%
            return 0.05 * ingresos
        else:
            return 0.10 * ingresos
#Este es para la taza descuento
    def calcular_descuento(self):
        ingresos = self.calcular_ingresos()
        if ingresos < 1000: # si el mmonto es menor a 1000
            return 0.11 * ingresos
        else:
            return 0.15 * ingresos
#CALCULA EL SUELDO
    def calcular_sueldo_neto(self):
        ingresos = self.calcular_ingresos()
        bonificacion = self.calcular_bonificacion()
        descuento = self.calcular_descuento()
        return ingresos + bonificacion - descuento

    def ingresos(self):
        return self.calcular_ingresos()

class EmpleadoPermanente(Empleado):
    def __init__(self, rfc, apellidos, nombres, sueldo_base, numero_seguro_social):
        super().__init__(rfc, apellidos, nombres)
        self.sueldo_base = sueldo_base
        self.numero_seguro_social = numero_seguro_social
        if sueldo_base < 150:
            raise ValueError("El sueldo base no puede ser menor a 150(<150).")

    def ingresos(self):
        return self.sueldo_base

    def calcular_descuento(self):
        return 0.11 * self.sueldo_base

    def calcular_sueldo_neto(self):
        ingresos = self.ingresos()
        descuento = self.calcular_descuento()
        return ingresos - descuento

if __name__ == "__main__":
    tipo_empleado = input("Ingrese el tipo de empleado (vendedor-permanente):").strip().lower()
    
    rfc = input("Ingrese el RFC:")
    apellidos = input("Ingrese los APELLIDOS:")
    nombres = input("Ingrese los NOMBRES:")
    try:
        if tipo_empleado == "vendedor":
            monto_vendido = float(input("Ingrese el monto vendido:"))
            tasa_comision = float(input("Ingrese la tasa de comisión (EN DECIMAL PARA CONTAR EL 10%):"))
            empleado = EmpleadoVendedor(rfc, apellidos, nombres, monto_vendido, tasa_comision)
            print(empleado.mostrar_info())
            print("Ingresos:", empleado.ingresos())
            print("Sueldo Neto:", empleado.calcular_sueldo_neto())
        
        elif tipo_empleado == "permanente":
            sueldo_base = float(input("Ingrese el sueldo base:"))
            numero_seguro_social = input("Ingrese el número de seguro social:")
            empleado = EmpleadoPermanente(rfc, apellidos, nombres, sueldo_base, numero_seguro_social)
            print(empleado.mostrar_info())
            print("Ingresos:", empleado.ingresos())
            print("Sueldo Neto:", empleado.calcular_sueldo_neto())
        
        else:
            print("Tipo de empleado no válido. Use 'vendedor' o 'permanente'")

    except ValueError as e:
        print(e)
