# 895. Maximum Frequency Stack
# Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.
# Implement the FreqStack class:
# FreqStack() constructs an empty frequency stack.
# void push(int val) pushes an integer val onto the top of the stack.
# int pop() removes and returns the most frequent element in the stack.
# If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

class FreqStack:

    def __init__(self):
        self.stks = []
        self.freq = defaultdict(int)
        
    def push(self, val: int) -> None:
        self.freq[val] += 1
        if self.freq[val] > len(self.stks):
            self.stks.append([val])
        else:
            self.stks[self.freq[val]-1].append(val)
            
    def pop(self) -> int:
        val = self.stks[-1].pop()
        if not self.stks[-1]:
            self.stks.pop()
        self.freq[val] -= 1
        return val
