from rest_framework.serializers import ValidationError


class SupplierValidator:
    """Валидатор для проверки отсутствия поставщика у завода и наличия поставщика у розничной сети и ИП."""

    def __init__(self, supplier, hierarchy_type):
        self.supplier = supplier
        self.hierarchy_type = hierarchy_type

    def __call__(self, value):
        tmp_supplier = dict(value).get(self.supplier)
        tmp_hierarchy_type = dict(value).get(self.hierarchy_type)
        if tmp_supplier and tmp_hierarchy_type == "factory":
            raise ValidationError(f"Завод не может иметь поставщика.")
        if tmp_hierarchy_type == "retail network" and not tmp_supplier:
            raise ValidationError(f"Розничная сеть должна иметь поставщика.")
        if tmp_hierarchy_type == "individual entrepreneur" and not tmp_supplier:
            raise ValidationError(f"ИП должен иметь поставщика.")
