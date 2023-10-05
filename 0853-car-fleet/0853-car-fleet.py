class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        # List comprehension
        pairs = [[p, s] for p, s in zip(position, speed)]
        
        for p, s in sorted(pairs)[::-1]:
            time = (target - p) / s
            stack.append(time)
            
            # Collision happens when:
            # + There are at least 2 cars
            # + Time to arrive dest of the behind car is <= the front car
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)