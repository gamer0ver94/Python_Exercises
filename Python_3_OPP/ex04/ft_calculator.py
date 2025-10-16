class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Dot productor of 2 vectors"""
        tmp = []
        res = 0
        for i in range(len(V1)):
            tmp.append(V1[i] * V2[i])
        for x in tmp:
            res += x
        print(f"Dot product is: {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Sum of 2 vectors"""
        res = []
        for i in range(len(V1)):
            res.append(float(V1[i] + V2[i]))
        print(f"Add Vector is: {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """The sub if 2 vectors"""
        res = []
        for i in range(len(V1)):
            res.append(float(V1[i] - V2[i]))
        print(f"Sous Vector is: {res}")
