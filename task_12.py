from typing import Union
from task_11 import Dessert


class JellyBean(Dessert):
    """ Class for JellyBean dessert. Has flavor attribute """

    _SPECIAL_TASTES = ["black licorice", ]

    def __init__(self, name: str = "dessert_name",
                 calories: Union[float, int] = 0,
                 flavor="jelly bean"):
        super().__init__(name, calories)
        self.flavor = flavor

    @staticmethod
    def __is_flavor_of_type_str(flavor):
        return isinstance(flavor, str)

    @property
    def flavor(self):
        return self.__flavor

    @flavor.setter
    def flavor(self, flavor: str):
        if not JellyBean.__is_flavor_of_type_str(flavor):
            raise ValueError("Flavor of the dessert has to be of type 'str")
        self.__flavor = flavor

    def is_delicious(self):
        if self.flavor in JellyBean._SPECIAL_TASTES:
            return False
        return True

    def __str__(self):
        return f"Dessert '{self.name}' has '{self.calories}' calories in it and '{self.flavor}' flavor."


if __name__ == "__main__":
    j_bean = JellyBean("jelly bean", 200, "pistachio")
    print("Name:", j_bean.name, "Calories:", j_bean.calories,
          "Is healthy:", j_bean.is_healthy(), "Is delicious", j_bean.is_delicious())

    j_bean_licorice = JellyBean()
    j_bean_licorice.name = "jelly bean licorice"
    j_bean_licorice.calories = 201
    j_bean_licorice.flavor = "black licorice"
    print(j_bean_licorice, "Is healthy:", j_bean_licorice.is_healthy(),
          "Is delicious", j_bean_licorice.is_delicious())
