class mamal():
    __legs: int
    __baby_feed: str="breast feeding"
    __walking: str

    def __init__(self, legs_in, walking_in):
        self.__legs=legs_in
        self.__walking=walking_in

    def set_legs(self, legs_in):
        self.__legs=legs_in

    def get_legs(self):
        return self.__legs

    def set_baby_feed(self, baby_feed_in):
        self.__baby_feed=baby_feed_in

    def get_baby_feed(self):
        return self.__baby_feed

    def set_walking(self, walking_in):
        self.__walking=walking_in

    def get_walking(self):
        return self.__walking




class dog(mamal):
    type: str="hoskey"
    ears: int=2
    __age: int             #in action encapsulation
    _color: str           #litterally encapsulation

    def __init__(self, legs_in, color_in="white", age_in=5):
        super().__init__(legs_in=legs_in, walking_in="on feet and hands")
        self._color=color_in
        self.__age=age_in

    def introduce(self):
        print("\n\n(animal_attributes)")
        print("baby_feed: ", self.get_baby_feed())
        print("legs num: ", self.get_legs())
        print("walking: ", self.get_walking(), "\n")

        print("(dog attributes)")
        print("type: ", self.type)
        print("ears num: ", self.ears)
        print("age: ", self.__age)
        print("color: ", self._color)
