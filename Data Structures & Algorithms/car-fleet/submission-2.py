class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Initialize pairs and sort according to reverse position
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        # Iterate through each pair and append to stack from closest first
        stack = []
        for p, s in pairs:
            time = (target - p) / s
            stack.append(time)
            # If the further car reaches target faster, it will merge
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)


"""
Goal: find number of fleets that reach target
- use stack to contain time taken to reach goal
- work backwards starting from the one closest to the target
position:   4   1
speed       2   3
target: 10
time taken fro car 4 to reach goal: (10-4)/2 = 3
stack: 3
time taken for car 1 to reach goal: (10-1)/3 = 3
stack: 3    3
since time taken for car 1 to reach goal <= time taken for car 2 to reach goal, they can merge (remove car 1 since it caught up)
"""