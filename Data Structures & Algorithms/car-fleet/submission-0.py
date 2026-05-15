class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs=defaultdict(list)
        for i in range(len(position)):
            pairs[position[i]]=speed[i]
        sorted_pairs=sorted(pairs.items(),reverse=True)
        time_stack=[]
        for pos,speed in sorted_pairs:
            time=(target-pos)/speed
            if not time_stack or time>time_stack[-1]:
                time_stack.append(time)
        return len(time_stack)
        