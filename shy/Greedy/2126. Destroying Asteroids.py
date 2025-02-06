class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        # python sort()和sorted() 函数默认升序排序
        asteroids.sort()
        for asteroid in asteroids:
            if asteroid > mass:
                return False
            mass += asteroid

        return True